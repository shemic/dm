FROM docker.shemic.com/dev/php:latest

MAINTAINER Rabin "https://github.com/shemic"

RUN apk add --no-cache --update mosquitto-dev php5-dev autoconf gcc g++ make openssl-dev curl git && \
	cd /tmp && \
	git clone https://github.com/mgdm/Mosquitto-PHP && \
	cd Mosquitto-PHP && \
	phpize && \
	./configure --with-php-config=/usr/bin/php-config && \
	make && \
	make install && \
	cd .. && rm -rf Mosquitto-PHP && \
	apk del php5-dev m4 autoconf gcc g++ make openssl-dev curl git && \
	rm -rf /tmp/* /var/cache/apk/*