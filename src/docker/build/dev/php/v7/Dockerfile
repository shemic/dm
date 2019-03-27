FROM docker.dever.cc/os/alpine:latest

MAINTAINER Rabin "https://github.com/shemic"

ENV COMPOSER_HOME=/share/lib/php

RUN apk add --no-cache --update curl php7-fpm php7-pear php7-mysqli php7-session php7-pgsql php7-pdo_mysql php7-pdo_pgsql php7-gd php7-curl php7-mcrypt php7-json php7-zlib php7-xml php7-xmlwriter php7-iconv php7-zip php7-phar  php7-openssl php7-dom php7-mbstring php7-simplexml php7-sockets php7-pcntl php7-fileinfo  php7-tokenizer php7-opcache php7-redis php7-imagick && curl -sS https://getcomposer.org/installer | php && mv composer.phar /usr/bin/composer && apk del curl && composer config -g repo.packagist composer https://packagist.phpcomposer.com

#php7-memcached php7-redis 

COPY php.sh /entrypoint/php.sh
COPY install.sh /install.sh

VOLUME ["/www", "/etc/php7"]

EXPOSE 9000

CMD ["php"]