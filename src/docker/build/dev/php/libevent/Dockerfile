FROM docker.dever.cc/dev/php/v7:latest

MAINTAINER Rabin "https://github.com/shemic"

RUN apk add --no-cache --update php7-dev m4 autoconf gcc g++ make openssl-dev curl && \
	cd /tmp && \
	curl -O http://pecl.php.net/get/event-2.3.0.tgz && \
	tar -xzvf event-2.3.0.tgz && \
	cd event-2.3.0 && \
	phpize && \
	./configure --with-php-config=/usr/bin/php-config && \
	make && \
	make install && \
	cd .. && \

	apk del php7-dev m4 autoconf gcc g++ make openssl-dev curl && \
	rm -rf /tmp/* /var/cache/apk/*