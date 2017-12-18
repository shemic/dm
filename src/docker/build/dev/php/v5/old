FROM docker.dever.cc/os/alpine/v3.4:latest

MAINTAINER Rabin "https://github.com/shemic"

ENV COMPOSER_HOME=/share/lib/php

RUN apk add --no-cache --update curl php5-fpm php5-pear php5-mysql php5-pgsql php5-pdo_mysql php5-pdo_pgsql php5-gd php5-curl php5-mcrypt php5-json php5-zlib php5-xml php5-iconv php5-zip php5-phar php5-openssl php5-dom && curl -sS https://getcomposer.org/installer | php && mv composer.phar /usr/bin/composer && apk del curl && composer config -g repo.packagist composer https://packagist.phpcomposer.com
	# && apk add --no-cache --update php5-dev m4 autoconf gcc g++ make openssl-dev curl && \
	#cd /tmp && \
	#curl -O http://www.dever.cc/file/php/php-redis-3.1.2.tgz && \
	#tar -xzvf php-redis-3.1.2.tgz && \
	#cd redis-3.1.2 && \
	#phpize && \
	#./configure --with-php-config=/usr/bin/php-config && \
	#make && \
	#make install && \
	#cd .. && \

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

	#apk del php5-dev m4 autoconf gcc g++ make openssl-dev curl git && \
	#rm -rf /tmp/* /var/cache/apk/*

COPY php.sh /entrypoint/php.sh
COPY install.sh /install.sh

VOLUME ["/www", "/etc/php5"]

EXPOSE 9000

CMD ["php"]