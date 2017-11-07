FROM docker.dever.cc/java/base:latest

MAINTAINER Rabin "https://github.com/shemic"

# set environment variable
ENV LOGSTASH_HOME=/usr/local/logstash
ENV LOGSTASH_VERSION=5.5.1
ENV PATH=$PATH:$LOGSTASH_HOME/bin

# install logstash
RUN curl -O https://artifacts.elastic.co/downloads/logstash/logstash-${LOGSTASH_VERSION}.tar.gz && \
    tar -xzvf logstash-${LOGSTASH_VERSION}.tar.gz && \
    mv logstash-${LOGSTASH_VERSION} $LOGSTASH_HOME && \
    rm logstash-${LOGSTASH_VERSION}.tar.gz && \
    mkdir -p /root/logstash

COPY logstash.sh /entrypoint/logstash.sh

VOLUME ["/usr/local/logstash/config", "/root/logstash"]