FROM docker.shemic.com/os/alpine:latest

MAINTAINER Rabin "https://github.com/shemic"

# set environment variable
ENV CONSUL_VERSION=0.9.2

# install
RUN apk add --no-cache --update curl unzip && \
	curl -O https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip && \
	unzip consul_${CONSUL_VERSION}_linux_amd64.zip && \
	mv consul /usr/bin/ && \
	rm consul_${CONSUL_VERSION}_linux_amd64.zip && \
	apk del curl unzip && \
	mkdir -p /root/consul/data && \
	mkdir -p /root/consul/config

COPY consul.sh /entrypoint/consul.sh

VOLUME ["/root/consul/config"]