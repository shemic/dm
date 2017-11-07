FROM docker.dever.cc/java/base:latest

MAINTAINER Rabin "https://github.com/shemic"

# set environment variable
ENV HADOOP_HOME=/share/lib/hadoop
ENV SPARK_HOME=/share/lib/spark
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$SPARK_HOME/bin

ENV ZEPPELIN_HOME=/usr/local/zeppelin
ENV ZEPPELIN_VERSION=0.7.2
ENV ZEPPELIN_TYPE=all
ENV PATH=$PATH:$ZEPPELIN_HOME/bin

# install zeppelin
#RUN curl -O ${MIRRORS}apache/zeppelin/zeppelin-$ZEPPELIN_VERSION/zeppelin-$ZEPPELIN_VERSION-bin-$ZEPPELIN_TYPE.tgz && tar -xzvf zeppelin-$ZEPPELIN_VERSION-bin-$ZEPPELIN_TYPE && mv zeppelin-$ZEPPELIN_VERSION-bin-$ZEPPELIN_TYPE.tgz $ZEPPELIN_HOME && rm zeppelin-$ZEPPELIN_VERSION-bin-$ZEPPELIN_TYPE.tgz

COPY zeppelin-$ZEPPELIN_VERSION-bin-$ZEPPELIN_TYPE $ZEPPELIN_HOME

COPY zeppelin.sh /entrypoint/zeppelin.sh

VOLUME ["/usr/local/zeppelin/conf"]
