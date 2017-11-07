FROM docker.dever.cc/java/base:latest

MAINTAINER Rabin "https://github.com/shemic"

# set environment variable
ENV ZOOKEEPER_HOME=/usr/local/zookeeper
ENV ZOOKEEPER_VERSION=3.5.2-alpha
ENV PATH=$PATH:$ZOOKEEPER_HOME/bin

# install
RUN curl -O ${MIRRORS}apache/zookeeper/zookeeper-$ZOOKEEPER_VERSION/zookeeper-$ZOOKEEPER_VERSION.tar.gz && \
	tar -xzvf zookeeper-$ZOOKEEPER_VERSION.tar.gz && \
	mv zookeeper-$ZOOKEEPER_VERSION $ZOOKEEPER_HOME && \
	rm zookeeper-$ZOOKEEPER_VERSION.tar.gz && \
	mkdir -p /root/zookeeper/tmp

COPY zookeeper.sh /entrypoint/zookeeper.sh

VOLUME ["/usr/local/zookeeper/conf"]