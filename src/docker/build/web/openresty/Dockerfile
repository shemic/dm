FROM docker.shemic.com/os/alpine/v3.4:latest

MAINTAINER Rabin "https://github.com/shemic"

ENV OR_HOME=/usr/local/openresty
ENV OR_VERSION=1.11.2.5
ENV PATH=$PATH:$OR_HOME/bin

RUN apk add --no-cache --update curl gcc make perl libpcre32 libressl-dev openssl musl-dev pcre-dev zlib-dev && \
	curl -O https://openresty.org/download/openresty-{$OR_VERSION}.tar.gz && \
	tar -zxvf openresty-{$OR_VERSION}.tar.gz && \
	cd openresty-{$OR_VERSION} && \
	./configure && \
	make && make install && \
	apk del curl gcc make perl libpcre32 libressl-dev openssl musl-dev pcre-dev

COPY openresty.sh /entrypoint/openresty.sh