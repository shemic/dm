#!/usr/bin/env sh
set -e

#https://caffe2.ai/docs/getting-started.html?platform=ubuntu&configuration=compile
#openmpi-dev@testing libiomp-dev
#http://fabiorehm.com/blog/2015/07/22/building-a-minimum-viable-phantomjs-2-docker-image/

apk add build-base cmake git glog-dev gtest-dev leveldb-dev@testing openmpi-dev@testing openmpi-doc@testing lmdb-dev snappy-dev protobuf-dev protobuf-c python3-dev
pip3 install future
pip3 install numpy
pip3 install protobuf


git clone --recursive https://github.com/caffe2/caffe2.git
cd caffe2
make
cd build
make install