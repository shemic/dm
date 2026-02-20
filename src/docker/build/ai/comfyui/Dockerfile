FROM nvidia/cuda:12.8.1-cudnn-runtime-ubuntu24.04

MAINTAINER Rabin "https://github.com/shemic"
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /opt

# CA certs
RUN apt update && apt install -y ca-certificates && update-ca-certificates

# USTC APT 源（deb822）
RUN mkdir -p /etc/apt/sources.list.d && \
    printf "Types: deb\nURIs: https://mirrors.ustc.edu.cn/ubuntu/\nSuites: noble noble-updates noble-backports noble-security\nComponents: main restricted universe multiverse\nSigned-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg\n" \
    > /etc/apt/sources.list.d/ubuntu.sources

# 运行 + 编译必需
# cuda-toolkit-12-8 含 nvcc，保证运行时能编 FA2
RUN apt update && apt install -y \
    bash \
    python3 python3-venv python3-pip python3-dev \
    git curl wget \
    build-essential ninja-build \
    cuda-toolkit-12-8 \
    libgl1 libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# pip 国内源 + 关闭 PEP668
RUN pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
    rm -f /usr/lib/python3.12/EXTERNALLY-MANAGED && \
    pip3 config set global.break-system-packages true

# 安装 PyTorch cu128（三件套对齐）
RUN pip3 install --no-cache-dir \
  torch==2.9.0 torchvision==0.24.0 torchaudio==2.9.0 \
  --index-url https://download.pytorch.org/whl/cu128

# 安装 xformers（有 wheel 就装；失败不阻断）
RUN pip3 install --no-cache-dir --prefer-binary xformers \
    --extra-index-url https://download.pytorch.org/whl/cu128 \
    || echo "xformers wheel/build not available, fallback to SDPA"

# 拉 ComfyUI
RUN git clone https://github.com/comfyanonymous/ComfyUI.git /opt/ComfyUI
WORKDIR /opt/ComfyUI

# 安装 ComfyUI requirements（加 cu128 额外源避免 torch CPU 覆盖）
RUN pip3 install --no-cache-dir -r requirements.txt \
    --extra-index-url https://download.pytorch.org/whl/cu128

# 运行期优化（通用）
ENV PYTORCH_ALLOC_CONF=expandable_segments:True,max_split_size_mb:256
ENV CUDA_MODULE_LOADING=LAZY
ENV TORCH_LOGS=off

# 全局 TF32 + cudnn benchmark（推理免费提速）
RUN python3 - <<'PY'
import site, os
p = site.getsitepackages()[0]
sc = os.path.join(p, 'sitecustomize.py')
with open(sc, 'w') as f:
    f.write('import torch\n')
    f.write('torch.backends.cuda.matmul.allow_tf32 = True\n')
    f.write('torch.backends.cudnn.allow_tf32 = True\n')
    f.write('torch.backends.cudnn.benchmark = True\n')
print('written', sc)
PY

# 拷贝入口脚本
COPY entrypoint.sh /opt/entrypoint.sh
RUN chmod +x /opt/entrypoint.sh

EXPOSE 8188
SHELL ["/bin/bash", "-c"]

ENTRYPOINT ["/opt/entrypoint.sh"]
