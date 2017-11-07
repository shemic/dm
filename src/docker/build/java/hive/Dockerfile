FROM docker.dever.cc/java/base:latest

MAINTAINER Rabin "https://github.com/shemic"

# set environment variable
ENV HADOOP_HOME=/share/lib/hadoop
ENV SPARK_HOME=/share/lib/spark
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$SPARK_HOME/bin

ENV HIVE_HOME=/usr/local/hive
ENV HIVE_VERSION=2.1.1
ENV PATH=$PATH:$HIVE_HOME/bin

# install
RUN curl -O ${MIRRORS}apache/hive/hive-$HIVE_VERSION/apache-hive-$HIVE_VERSION-bin.tar.gz && tar -xzvf apache-hive-$HIVE_VERSION-bin.tar.gz && mv apache-hive-$HIVE_VERSION-bin HIVE_HOME && rm apache-hive-$HIVE_VERSION-bin.tar.gz && \
	mkdir -p /root/hive/tmp && \
	mkdir -p /root/hive/logs

#COPY apache-hive-$HIVE_VERSION-bin $HIVE_HOME
COPY hive.sh /entrypoint/hive.sh
COPY plugin/* $HIVE_HOME/lib/

VOLUME ["/usr/local/hive/conf"]