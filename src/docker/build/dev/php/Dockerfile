FROM docker.dever.cc/dev/php/base:latest

MAINTAINER Rabin "https://github.com/shemic"

RUN apk add --no-cache --update php5-dev m4 autoconf gcc g++ make openssl-dev curl && \
	cd /tmp && \
	curl -O http://www.dever.cc/file/php/php-mongo-1.6.14.tgz && \
	tar -xzvf php-mongo-1.6.14.tgz && \
	cd mongo-1.6.14 && \
	phpize && \
	./configure --with-php-config=/usr/bin/php-config && \
	make && \
	make install && \
	cd .. && \
	curl -O http://www.dever.cc/file/php/php-redis-3.1.2.tgz && \
	tar -xzvf php-redis-3.1.2.tgz && \
	cd redis-3.1.2 && \
	phpize && \
	./configure --with-php-config=/usr/bin/php-config && \
	make && \
	make install && \
	cd .. && \

	#curl -O https://launchpadlibrarian.net/165454254/libmemcached-1.0.18.tar.gz && \
	#tar -xzvf libmemcached-1.0.18.tar.gz && \
	#cd libmemcached-1.0.18 && \
	#./configure --prefix=/usr/local/libmemcached --with-memcached && \
	#make && make install && \
	#cd .. && \
	#curl -O http://pecl.php.net/get/memcached-3.0.3.tgz && \
	#tar -xzvf memcached-3.0.3.tgz && \
	#cd memcached-3.0.3 && \
	#phpize && \
	#./configure --with-php-config=/usr/bin/php-config && \
	#make && \
	#make install && \
	#cd .. && \

	apk del php5-dev m4 autoconf gcc g++ make openssl-dev curl git && \
	rm -rf /tmp/* /var/cache/apk/*