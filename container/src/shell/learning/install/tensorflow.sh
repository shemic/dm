#!/usr/bin/env sh
set -e

#apk add build-base python3-dev libc6-compat

#curl -O https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.5.0rc1-cp36-cp36m-linux_x86_64.whl

#pip3 install tensorflow-1.5.0rc1-cp36-cp36m-linux_x86_64.whl

# 必须重新编译了
export JAVA_HOME=/usr/lib/jvm/java-1.8-openjdk
export LOCAL_RESOURCES=2048,.5,1.0

export BAZEL_VERSION=0.7.0
export TENSORFLOW_VERSION=1.4.0

apk add --no-cache python3-tkinter imagemagick graphviz
apk add --no-cache --virtual=.build-deps bash cmake curl freetype-dev g++ libjpeg-turbo-dev libpng-dev linux-headers makemusl-dev openblas-dev openjdk8 patch perl python3-dev py-numpy-dev rsync sed swig zip
cd /tmp
pip3 install --no-cache-dir wheel
curl -SLO https://github.com/bazelbuild/bazel/releases/download/${BAZEL_VERSION}/bazel-${BAZEL_VERSION}-dist.zip
mkdir bazel-${BAZEL_VERSION}
unzip -qd bazel-${BAZEL_VERSION} bazel-${BAZEL_VERSION}-dist.zip
cd bazel-${BAZEL_VERSION}
sed -i -e '/"-std=c++0x"/{h;s//"-fpermissive"/;x;G}' tools/cpp/cc_configure.bzl
sed -i -e '/#endif /\/ COMPILER_MSVC/{h;s//#else/;G;s//#include <sys\/stat.h>/;G;}' third_party/ijar/common.h
bash compile.sh
cp -p output/bazel /usr/bin/
cd /tmp
curl -SL https://github.com/tensorflow/tensorflow/archive/v${TENSORFLOW_VERSION}.tar.gz | tar xzf -
cd tensorflow-${TENSORFLOW_VERSION}
sed -i -e '/JEMALLOC_HAVE_SECURE_GETENV/d' third_party/jemalloc.BUILD
PYTHON_BIN_PATH=/usr/bin/python3
PYTHON_LIB_PATH=/usr/lib/python3.6/site-packages
CC_OPT_FLAGS="-march=native"
TF_NEED_JEMALLOC=1
TF_NEED_GCP=0
TF_NEED_HDFS=0
TF_NEED_S3=0
TF_ENABLE_XLA=0
TF_NEED_GDR=0
TF_NEED_VERBS=0
TF_NEED_OPENCL=0
TF_NEED_CUDA=0
TF_NEED_MPI=0
bash configure
bazel build -c opt --local_resources ${LOCAL_RESOURCES} //tensorflow/tools/pip_package:build_pip_package
./bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_pkg
cd
pip3 install --no-cache-dir /tmp/tensorflow_pkg/tensorflow-${TENSORFLOW_VERSION}-cp36-cp36m-linux_x86_64.whl
pip3 install --no-cache-dir google-api-python-client
apk del .build-deps
rm -f /usr/bin/bazel
rm -rf /tmp/* /root/.cache