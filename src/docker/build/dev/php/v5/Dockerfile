FROM docker.dever.cc/os/alpine:latest

MAINTAINER Rabin "https://github.com/shemic"

ENV COMPOSER_HOME=/share/lib/php

RUN apk add --no-cache --update curl php5-fpm php5-pear php5-mysql php5-pgsql php5-pdo_mysql php5-pdo_pgsql php5-gd php5-curl php5-mcrypt php5-json php5-zlib php5-xml php5-iconv php5-zip php5-phar php5-openssl php5-dom php5-sockets php5-pcntl && ln /usr/bin/php5 /usr/bin/php && curl -sS https://getcomposer.org/installer | php5 && mv composer.phar /usr/bin/composer && apk del curl && composer config -g repo.packagist composer https://packagist.phpcomposer.com

COPY php.sh /entrypoint/php.sh
COPY install.sh /install.sh

VOLUME ["/www", "/etc/php5"]

EXPOSE 9000

CMD ["php"]