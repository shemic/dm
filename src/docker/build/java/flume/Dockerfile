FROM docker.dever.cc/java/base:latest

MAINTAINER Rabin "https://github.com/shemic"

# set environment variable
ENV HADOOP_HOME=/share/lib/hadoop
ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
ENV YARN_CONF_DIR=$HADOOP_CONF_DIR
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

ENV FLUME_HOME=/usr/local/flume
ENV FLUME_VERSION=1.7.0
ENV PATH=$PATH:$FLUME_HOME/bin

# install
RUN curl -O ${MIRRORS}apache/flume/$FLUME_VERSION/apache-flume-$FLUME_VERSION-bin.tar.gz && \
	tar -xzvf apache-flume-$FLUME_VERSION-bin.tar.gz && \
	mv apache-flume-$FLUME_VERSION-bin $FLUME_HOME && \
	rm apache-flume-$FLUME_VERSION-bin.tar.gz && \
	mkdir -p /root/flume/input && \
	mkdir -p /root/flume/output

COPY flume.sh /entrypoint/flume.sh

VOLUME ["/usr/local/flume/conf", "/root/flume/input", "/root/flume/output"]