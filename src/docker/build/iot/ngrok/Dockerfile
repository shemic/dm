FROM golang:1.7.1-alpine

MAINTAINER Rabin "https://github.com/shemic"

ENV NG_DOMAIN="ngrok.dever.cc"
ENV NG_NAME=ngrok
ENV NG_HOME=/usr/local/$NG_NAME
ENV PATH=$PATH:$NG_HOME/bin

RUN sed -i "s/http:\/\/dl-cdn.alpinelinux.org/http:\/\/mirrors.ustc.edu.cn/g" /etc/apk/repositories && apk --no-cache --update add tzdata && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && date && apk del tzdata && mkdir /entrypoint && mkdir /share

VOLUME ["/share"]

RUN apk add --no-cache --update git make openssl  && \
	git clone https://github.com/inconshreveable/ngrok.git --depth=1 $NG_HOME

ADD build.sh /
RUN sh /build.sh

EXPOSE 8081

COPY ngrok.sh /entrypoint/ngrok.sh