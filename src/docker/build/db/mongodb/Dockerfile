FROM docker.shemic.com/os/alpine:latest

MAINTAINER Rabin "https://github.com/shemic"

RUN echo 'http://dl-3.alpinelinux.org/alpine/edge/testing'>>/etc/apk/repositories
RUN apk update
RUN wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-3.4.5.tgz

RUN mkdir /data

VOLUME ["/data"]

ENTRYPOINT ["sh"]