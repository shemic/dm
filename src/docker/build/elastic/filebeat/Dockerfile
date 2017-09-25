FROM docker.shemic.com/java/base:latest

MAINTAINER Rabin "https://github.com/shemic"

# set environment variable
ENV FILEBEAT_HOME=/usr/local/filebeat
ENV FILEBEAT_VERSION=5.5.1
ENV PATH=$PATH:$FILEBEAT_HOME

# install filebeat
RUN curl -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-${FILEBEAT_VERSION}-linux-x86_64.tar.gz && \
    tar -xzvf filebeat-${FILEBEAT_VERSION}-linux-x86_64.tar.gz && \
    mv filebeat-${FILEBEAT_VERSION}-linux-x86_64 $FILEBEAT_HOME && \
    rm filebeat-${FILEBEAT_VERSION}-linux-x86_64.tar.gz && \
    mkdir -p /root/filebeat

COPY filebeat.sh /entrypoint/filebeat.sh

VOLUME ["/usr/local/filebeat/config", "/root/filebeat"]