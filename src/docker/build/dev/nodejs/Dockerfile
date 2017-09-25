FROM docker.shemic.com/os/alpine:latest

MAINTAINER Rabin "https://github.com/shemic"

RUN mkdir /src
VOLUME ["/src"]
WORKDIR /src

RUN apk add --no-cache --update nodejs nodejs-npm

EXPOSE 8080

COPY nodejs.sh /entrypoint/nodejs.sh
COPY reload.sh /entrypoint/reload.sh