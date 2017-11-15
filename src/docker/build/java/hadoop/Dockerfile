FROM docker.dever.cc/java/base:latest

MAINTAINER Rabin "https://github.com/shemic"

# set environment variable
ENV HADOOP_HOME=/usr/local/hadoop
ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
ENV HADOOP_VERSION=2.7.4
ENV HADOOP_LOG_DIR=/root/hadoop/logs
ENV YARN_CONF_DIR=$HADOOP_CONF_DIR
ENV YARN_LOG_DIR=/root/yarn/logs
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HADOOP_HOME/lib/native
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

# install hadoop
RUN mkdir -p /root/hdfs/namenode && \ 
    mkdir -p /root/hdfs/datanode && \
    mkdir -p /root/hadoop/tmp && \
    mkdir -p /root/hadoop/logs && \
    mkdir -p /root/yarn/logs && \
    curl -O ${MIRRORS}apache/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz && \
    tar -xzvf hadoop-$HADOOP_VERSION.tar.gz && \
    rm -rf hadoop-$HADOOP_VERSION/share/doc hadoop-$HADOOP_VERSION/share/hadoop/common/jdiff && \
    mv hadoop-$HADOOP_VERSION $HADOOP_HOME && \
    rm hadoop-$HADOOP_VERSION.tar.gz

COPY hadoop.sh /entrypoint/hadoop.sh

VOLUME ["/usr/local/hadoop/etc/hadoop"]