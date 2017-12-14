FROM docker.dever.cc/dev/php/v7:latest

MAINTAINER Rabin "https://github.com/shemic"

RUN apk add --no-cache --update php7-dev libevent-dev php7-xml && \
	pecl install event && \
	echo extension=event.so > /etc/php7/conf.d/30-event.ini