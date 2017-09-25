FROM alpine:3.4

MAINTAINER Rabin "https://github.com/shemic"

ENV CHINA_MIRRORS=http://mirrors.ustc.edu.cn/
ENV FAU_MIRRORS=http://ftp.fau.de/
ENV MIRRORS=$CHINA_MIRRORS

RUN sed -i "s/http:\/\/dl-cdn.alpinelinux.org/http:\/\/mirrors.ustc.edu.cn/g" /etc/apk/repositories && apk --no-cache --update add tzdata && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && date && apk del tzdata && mkdir /entrypoint && mkdir /share

VOLUME ["/share"]

COPY entrypoint.sh /entrypoint.sh
COPY process.sh /entrypoint/process.sh

ENTRYPOINT ["/entrypoint.sh"]