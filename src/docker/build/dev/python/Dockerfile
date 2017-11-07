FROM docker.dever.cc/os/alpine:latest

MAINTAINER Rabin "https://github.com/shemic"

RUN apk update && apk add --no-cache bash python py-pip && \
	pip install --upgrade pip && \
	mkdir /src && \
	mkdir /root/.pip && \
	echo -e "[global]\nindex-url = https://pypi.tuna.tsinghua.edu.cn/simple" > /root/.pip/pip.conf

VOLUME ["/src"]