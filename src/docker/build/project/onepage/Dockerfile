FROM docker.dever.cc/os/alpine/v3.4:latest

MAINTAINER Rabin "https://github.com/shemic"

RUN apk add --no-cache --update nginx

COPY onepage.sh /entrypoint/onepage.sh
COPY install.sh /install.sh

VOLUME ["/www", "/etc/nginx", "/var/log/nginx", "/etc/php5"]

ENV COMPOSER_HOME=/share/lib/php

RUN apk add --no-cache --update curl git php5-fpm php5-pear php5-mysql php5-pgsql php5-pdo_mysql php5-pdo_pgsql php5-gd php5-curl php5-mcrypt php5-json php5-zlib php5-xml php5-iconv php5-zip php5-phar php5-openssl php5-dom php5-sockets php5-pcntl php5-mysqli && curl -sS https://getcomposer.org/installer | php && mv composer.phar /usr/bin/composer && git clone http://git.dever.cc:3000/other/onepage.git /www/onepage && mkdir /www/onepage/tm/compile_dir && chmod 777 /www/onepage/tm/compile_dir/ && chmod -R 777 /www/onepage/kissy/public/upload/ && apk del curl git && composer config -g repo.packagist composer https://packagist.phpcomposer.com && chmod +x install.sh && ./install.sh memcached-2.2.0 memcached curl-dev,libmemcached-dev,cyrus-sasl-dev

EXPOSE 80
EXPOSE 443
EXPOSE 9000