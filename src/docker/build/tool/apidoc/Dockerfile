FROM docker.shemic.com/dev/nodejs:latest

MAINTAINER Rabin "https://github.com/shemic"

ENV APIDOC_HOME=/usr/lib/node_modules/npm/node_modules/apidoc
ENV PATH=$PATH:$APIDOC_HOME/bin

RUN cd /usr/lib/node_modules/npm && npm install apidoc && \
	mkdir -p /root/input && \
	mkdir -p /root/output && \
	mkdir -p /root/config