#!/usr/bin/env sh
set -e

export CC=/usr/bin/clang
export CXX=/usr/bin/clang++
export OPENCV_VERSION=3.3.0
#echo -e '@testing http://mirrors.ustc.edu.cn/alpine/edge/testing' >> /etc/apk/repositories

#apk update && apk update && apk del lapack-dev && apk add --no-cache build-base openblas-dev unzip wget cmake python3-dev libtbb@testing libtbb-dev@testing libjpeg libjpeg-turbo-dev libpng-dev jasper-dev tiff-dev libwebp-dev clang-dev linux-headers
#pip3 install numpy
#mkdir /opt && cd /opt
#wget https://github.com/opencv/opencv/archive/${OPENCV_VERSION}.zip
#unzip ${OPENCV_VERSION}.zip
#rm -rf ${OPENCV_VERSION}.zip
#mkdir -p /opt/opencv-${OPENCV_VERSION}/build
cd /opt/opencv-${OPENCV_VERSION}/build
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D BUILD_OPENCV_HAL=OFF -D WITH_FFMPEG=NO -D WITH_IPP=NO -D WITH_OPENEXR=NO -D WITH_TBB=YES -D BUILD_EXAMPLES=NO -D BUILD_ANDROID_EXAMPLES=NO -D INSTALL_PYTHON_EXAMPLES=NO -D BUILD_DOCS=NO -D BUILD_opencv_python2=NO -D BUILD_opencv_python3=ON -D PYTHON3_EXECUTABLE=/usr/bin/python3 -D PYTHON3_INCLUDE_DIR=/usr/include/python3.6m/ -D PYTHON3_LIBRARY=/usr/lib/libpython3.so -D PYTHON_LIBRARY=/usr/lib/libpython3.so -D PYTHON3_PACKAGES_PATH=/usr/lib/python3.6/site-packages/ -D PYTHON3_NUMPY_INCLUDE_DIRS=/usr/lib/python3.6/site-packages/numpy/core/include/ ..
make VERBOSE=1
make
make install
rm -rf /opt/opencv-${OPENCV_VERSION}
#apk del cmake build-base