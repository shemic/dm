FROM daocloud.io/library/ubuntu:16.04

MAINTAINER Rabin "https://github.com/shemic"

RUN sed -i "s/http:\/\/archive.ubuntu.com/http:\/\/mirrors.163.com/g" /etc/apt/sources.list && apt-get update -y && apt-get -y upgrade && DEBIAN_FRONTEND=noninteractive apt-get -y install git tar vim-nox net-tools wget --no-install-recommends && apt-get clean  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*