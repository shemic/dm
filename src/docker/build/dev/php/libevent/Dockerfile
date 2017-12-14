FROM docker.dever.cc/dev/php:latest

MAINTAINER Rabin "https://github.com/shemic"

RUN apk add --no-cache --update libevent-dev php5-xml && \
	pecl install channel://pecl.php.net/libevent-0.1.0 && \
	tar -zxvf libevent-0.1.0.tgz && \
	echo extension=libevent.so > /etc/php5/conf.d/libevent.ini