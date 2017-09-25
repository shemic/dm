FROM docker.shemic.com/java/base:latest

MAINTAINER Rabin "https://github.com/shemic"

# set environment variable
ENV KAFKA_HOME=/usr/local/kafka
ENV KAFKA_VERSION=2.11
ENV KAFKA_PATH=0.9.0.1
ENV PATH=$PATH:$KAFKA_HOME/bin

# install
RUN curl -O ${MIRRORS}apache/kafka/$KAFKA_PATH/kafka_$KAFKA_VERSION-$KAFKA_PATH.tgz && \
	tar -xzvf kafka_$KAFKA_VERSION-$KAFKA_PATH.tgz && \
	mv kafka_$KAFKA_VERSION-$KAFKA_PATH $KAFKA_HOME && \
	rm kafka_$KAFKA_VERSION-$KAFKA_PATH.tgz && \
	mkdir -p /root/kafka/logs

COPY kafka.sh /entrypoint/kafka.sh

VOLUME ["/usr/local/kafka/conf"]