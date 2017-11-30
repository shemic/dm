FROM docker.dever.cc/os/alpine:latest

MAINTAINER Rabin "https://github.com/shemic"

ENV GOPATH=/usr/local/golang

RUN apk add --no-cache --update go g++ git make
RUN mkdir /src
RUN mkdir /usr/local/golang

VOLUME ["/src"]