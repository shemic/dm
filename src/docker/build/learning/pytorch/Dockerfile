FROM docker.dever.cc/learning/opencv:latest

MAINTAINER Rabin "https://github.com/shemic"

RUN apk add --no-cache --virtual=.build-deps build-base python3-dev yaml-dev py3-yaml cmake git && \
    mkdir -p /tmp/pytorch && \
    git clone --recursive https://github.com/pytorch/pytorch /tmp/pytorch && \
    cd /tmp/pytorch && \
    python3 setup.py install && \
    apk del .build-deps && \
    rm -rf /tmp/* /root/.cache