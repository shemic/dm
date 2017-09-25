FROM docker.shemic.com/os/alpine:latest

MAINTAINER Rabin "https://github.com/shemic"

RUN apk update && apk add --no-cache bash python3 py-pip && \
	pip install --upgrade pip && \
	mkdir /src

VOLUME ["/src"]