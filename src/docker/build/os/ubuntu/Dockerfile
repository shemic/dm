FROM ubuntu:14.04

MAINTAINER Rabin "https://github.com/shemic"

RUN sed -i "s/http:\/\/dl-cdn.alpinelinux.org/https:\/\/mirror.tuna.tsinghua.edu.cn/g" /etc/apk/repositories && apk update && apk add tzdata && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && date && apk del tzdata

ENTRYPOINT ["sh"]