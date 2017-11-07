FROM docker.dever.cc/dev/php:latest

MAINTAINER Rabin "https://github.com/shemic"

RUN apk add --no-cache --update libaio-dev php5-dev autoconf gcc g++ make openssl-dev curl git && \
	cd /tmp && \
	git clone https://github.com/swoole/swoole-src.git && \
	cd swoole-src && \
	phpize && \
	./configure --with-php-config=/usr/bin/php-config && \
	make && \
	make install && \
	cd .. && rm -rf swoole-src && \
	apk del php5-dev m4 autoconf gcc g++ make openssl-dev curl git && \
	rm -rf /tmp/* /var/cache/apk/*