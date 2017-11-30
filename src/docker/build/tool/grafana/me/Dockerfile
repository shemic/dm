FROM docker.dever.cc/os/alpine:latest

MAINTAINER Rabin "https://github.com/shemic"

ENV GRAFANA_HOME=/usr/local/grafana
ENV GRAFANA_VERSION=4.6.2
ENV GRAFANA_LIB=/var/lib/grafana
ENV PATH=$PATH:$GRAFANA_HOME/bin

RUN apk add --no-cache --update curl && \
	mkdir -p $GRAFANA_HOME && \
	curl -O https://s3-us-west-2.amazonaws.com/grafana-releases/release/grafana-${GRAFANA_VERSION}.linux-x64.tar.gz && \
	tar -zxvf grafana-${GRAFANA_VERSION}.linux-x64.tar.gz -C $GRAFANA_HOME --strip-components=1 && \
	rm -rf grafana-${GRAFANA_VERSION}.linux-x64.tar.gz && \
	apk del curl
