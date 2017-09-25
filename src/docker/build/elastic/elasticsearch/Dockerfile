FROM docker.shemic.com/os/alpine/glibc:latest

MAINTAINER Rabin "https://github.com/shemic"

# set environment variable
ENV ES_HOME=/usr/local/elasticsearch
ENV ELASTICSEARCH_VERSION=5.5.1
ENV PATH=$PATH:$ES_HOME/bin
ENV JAVA_HOME=/share/lib/jdk
ENV PATH=${PATH}:${JAVA_HOME}/bin:${JAVA_HOME}/sbin

# install elasticsearch
RUN apk add --no-cache --update bash curl procps ncurses openjdk8 && \
	curl -O https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-${ELASTICSEARCH_VERSION}.tar.gz && \
    tar -xzvf elasticsearch-${ELASTICSEARCH_VERSION}.tar.gz && \
    mv elasticsearch-${ELASTICSEARCH_VERSION} $ES_HOME && \
    rm elasticsearch-${ELASTICSEARCH_VERSION}.tar.gz && \
    adduser es -D && \
    mkdir -p /elasticsearch/data && \
    mkdir -p /elasticsearch/logs && \
    mkdir -p /share/process/elasticsearch && \
    chown -R es:es $ES_HOME /elasticsearch /tmp && \
    chmod -R 777 /tmp /elasticsearch /share/process/elasticsearch $ES_HOME/config/scripts/ && \
    cd $ES_HOME && \
    echo y | elasticsearch-plugin install x-pack && \
    apk del curl openjdk8

USER es

COPY elasticsearch.sh /entrypoint/elasticsearch.sh

VOLUME ["/usr/local/elasticsearch/config"]