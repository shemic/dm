#!/usr/bin/env sh
set -e


#pip3 uninstall http://download.pytorch.org/whl/cpu/torch-0.3.0.post4-cp36-cp36m-linux_x86_64.whl 
#pip3 uninstall torchvision

apk add build-base python3-dev yaml-dev py3-yaml cmake git

mkdir -p /tmp/pytorch

git clone --recursive https://github.com/pytorch/pytorch /tmp/pytorch

cd /tmp/pytorch

python3 setup.py install

rm -rf /tmp/*