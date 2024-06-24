FROM docker.dever.cc/os/alpine:latest

MAINTAINER Rabin "https://github.com/shemic"

ENV COMPOSER_HOME=/share/lib/php

RUN apk add --no-cache --update curl php83-fpm php83-pear php83-mysqli php83-session php83-pgsql php83-pdo_mysql php83-pdo_pgsql php83-gd php83-curl php83-json php83-zlib php83-xml php83-xmlwriter php83-iconv php83-zip php83-phar  php83-openssl php83-dom php83-mbstring php83-simplexml php83-sockets php83-pcntl php83-fileinfo  php83-tokenizer php83-opcache php83-posix php83-ctype php-pecl-imagick && curl -sS https://getcomposer.org/installer | php && mv composer.phar /usr/bin/composer && apk del curl && composer config -g repo.packagist composer https://packagist.phpcomposer.com

#php83-memcached php83-redis php-pecl-imagick

COPY php.sh /entrypoint/php.sh
COPY install.sh /install.sh

VOLUME ["/www", "/etc/php83"]

EXPOSE 9000

CMD ["php"]