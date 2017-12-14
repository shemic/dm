FROM docker.dever.cc/dev/php/v7:latest

MAINTAINER Rabin "https://github.com/shemic"

RUN apk add --no-cache --update libaio-dev php7-dev autoconf gcc g++ make openssl-dev curl git && \
	cd /tmp && \
	#git clone https://github.com/swoole/swoole-src.git && \
	git clone https://gitee.com/swoole/swoole swoole-src && \
	cd swoole-src && \
	phpize && \
	./configure --with-php-config=/usr/bin/php-config --enable-coroutine && \
	make && \
	make install && \
	cd .. && rm -rf swoole-src && \
	apk del php7-dev m4 autoconf gcc g++ make openssl-dev curl git && \
	rm -rf /tmp/* /var/cache/apk/*