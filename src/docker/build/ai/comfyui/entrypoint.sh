#!/usr/bin/env bash
set -euo pipefail

# ------------------------------------------------------------
# 自动检测 GPU compute capability -> 生成 FLASH_ATTN_CUDA_ARCHS
# ------------------------------------------------------------
detect_flash_attn_archs() {
  # 如果没有 nvidia-smi（没挂 GPU），就回退到 89
  if ! command -v nvidia-smi >/dev/null 2>&1; then
    echo "89"
    return
  fi

  # 取所有 GPU 的 compute capability，例如：
  # 8.6 (3090/A10), 8.9 (4090), 9.0 (H100/H20)
  local caps
  caps=$(nvidia-smi --query-gpu=compute_cap --format=csv,noheader 2>/dev/null | tr -d ' ' || true)

  if [[ -z "${caps}" ]]; then
    echo "89"
    return
  fi

  local archs=()
  while IFS= read -r cap; do
    case "${cap}" in
      8.0|8.1) archs+=("80") ;;   # A100/A800 等
      8.6|8.7) archs+=("86") ;;   # RTX30 / A10
      8.9)     archs+=("89") ;;   # RTX40
      9.0)     archs+=("90") ;;   # H100/H20/H800
      *)
        # 兜底：把 "8.6" 这种转成 "86"
        archs+=("${cap/./}")
        ;;
    esac
  done <<< "${caps}"

  # 去重 + 排序后用 ; 拼起来
  printf "%s\n" "${archs[@]}" | sort -u | paste -sd ';' -
}

# 用户没手动传 FLASH_ATTN_CUDA_ARCHS 才自动检测
if [[ -z "${FLASH_ATTN_CUDA_ARCHS:-}" ]]; then
  export FLASH_ATTN_CUDA_ARCHS="$(detect_flash_attn_archs)"
fi

echo "[entrypoint] FLASH_ATTN_CUDA_ARCHS=${FLASH_ATTN_CUDA_ARCHS}"

# ------------------------------------------------------------
# USE_FA2=1 时编译并启用 FA2，否则默认 xformers/SDPA
# ------------------------------------------------------------
USE_FA2="${USE_FA2:-0}"

if [[ "${USE_FA2}" == "1" ]]; then
  echo "[entrypoint] USE_FA2=1 detected. Building flash-attn from source..."
  export MAX_JOBS="${MAX_JOBS:-2}"

  # 依赖
  pip install --no-cache-dir packaging

  # 编译安装 FA2
  if pip install --no-cache-dir flash-attn --no-build-isolation; then
    echo "[entrypoint] flash-attn installed OK. Launching ComfyUI with FA2."
    exec python3 main.py --listen 0.0.0.0 --port 8188 --use-flash-attention
  else
    echo "[entrypoint] flash-attn build failed. Fallback to xformers/SDPA."
    exec python3 main.py --listen 0.0.0.0 --port 8188 --use-xformers
  fi
else
  echo "[entrypoint] default: use xformers/SDPA."
  exec python3 main.py --listen 0.0.0.0 --port 8188 --use-xformers
fi
