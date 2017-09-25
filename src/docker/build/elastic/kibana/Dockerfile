FROM docker.shemic.com/java/base:latest

MAINTAINER Rabin "https://github.com/shemic"

# set environment variable
ENV KIBANA_HOME=/usr/local/kibana
ENV KIBANA_VERSION=5.5.1
ENV PATH=$PATH:$KIBANA_HOME/bin

# install kibana
RUN apk add --no-cache --update libstdc++ openjdk8 nodejs && \
	curl -O https://artifacts.elastic.co/downloads/kibana/kibana-${KIBANA_VERSION}-linux-x86_64.tar.gz && \
    tar -xzvf kibana-${KIBANA_VERSION}-linux-x86_64.tar.gz && \
    mv kibana-${KIBANA_VERSION}-linux-x86_64 $KIBANA_HOME && \
    rm kibana-${KIBANA_VERSION}-linux-x86_64.tar.gz && \
    cd $KIBANA_HOME && \
    sed -i 's/NODE="${DIR}\/node\/bin\/node"/NODE="node"/g' $KIBANA_HOME/bin/kibana && \
    sed -i 's/NODE="${DIR}\/node\/bin\/node"/NODE="node"/g' $KIBANA_HOME/bin/kibana-plugin && \
    kibana-plugin install x-pack && \
    apk del openjdk8

COPY kibana.sh /entrypoint/kibana.sh

VOLUME ["/usr/local/kibana/config"]