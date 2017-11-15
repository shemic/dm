FROM docker.dever.cc/java/base:latest

MAINTAINER Rabin "https://github.com/shemic"

# set environment variable
ENV HADOOP_HOME=/share/lib/hadoop
ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
ENV YARN_CONF_DIR=$HADOOP_CONF_DIR
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HADOOP_HOME/lib/native
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

ENV SPARK_HOME=/usr/local/spark
ENV SPARK_VERSION=2.1.2
ENV SPARK_HADOOP=hadoop2.7
ENV PATH=$PATH:$SPARK_HOME/bin

# install spark
RUN  apk add --no-cache --update python && \
	curl -O ${MIRRORS}apache/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-$SPARK_HADOOP.tgz && \
	tar -xzvf spark-$SPARK_VERSION-bin-$SPARK_HADOOP.tgz && \
	mv spark-$SPARK_VERSION-bin-$SPARK_HADOOP $SPARK_HOME && \
	rm spark-$SPARK_VERSION-bin-$SPARK_HADOOP.tgz && \
	mkdir -p /root/spark/logs

COPY spark.sh /entrypoint/spark.sh

VOLUME ["/usr/local/spark/conf"]