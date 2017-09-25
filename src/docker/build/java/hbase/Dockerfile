FROM docker.shemic.com/java/base:latest

MAINTAINER Rabin "https://github.com/shemic"

# set environment variable
ENV HADOOP_HOME=/share/lib/hadoop
ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
ENV YARN_CONF_DIR=$HADOOP_CONF_DIR
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

ENV HBASE_HOME=/usr/local/hbase
ENV HBASE_VERSION=1.2.6
ENV HBASE_MANAGES_ZK=false
ENV HBASE_LOG_DIR=/root/hbase/logs
ENV PATH=$PATH:$HBASE_HOME/bin

# install
RUN curl -O ${MIRRORS}apache/hbase/$HBASE_VERSION/hbase-$HBASE_VERSION-bin.tar.gz && \
	tar -xzvf hbase-$HBASE_VERSION-bin.tar.gz && \
	mv hbase-$HBASE_VERSION $HBASE_HOME && \
	rm hbase-$HBASE_VERSION-bin.tar.gz && \
	mkdir -p $HBASE_LOG_DIR && \
	rm -rf $HBASE_HOME/docs/

COPY hbase.sh /entrypoint/hbase.sh

VOLUME ["/usr/local/hbase/conf"]