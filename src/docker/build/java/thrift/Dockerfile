FROM docker.dever.cc/java/base:latest

MAINTAINER Rabin "https://github.com/shemic"

ENV THRIFT_HOME=/usr/local/thrift \
	THRIFT_VERSION=0.10.0
ENV PATH=$PATH:$THRIFT_HOME/bin

RUN apk add --no-cache --update automake bison g++ git libevent-dev libressl-dev libtool make pkgconf php7-dev && \
	curl -O ${MIRRORS}apache/thrift/$THRIFT_VERSION/thrift-$THRIFT_VERSION.tar.gz && \
	tar -zxvf thrift-$THRIFT_VERSION.tar.gz && \
	cd thrift-$THRIFT_VERSION && \
	./configure --prefix=$THRIFT_HOME && make && make install && \
	cd .. && \
	rm -rf thrift-$THRIFT_VERSION* && \
	apk del automake bison g++ git libevent-dev libressl-dev libtool make