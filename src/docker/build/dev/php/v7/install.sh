#!/usr/bin/env sh
set -e
lib="php7-dev m4 autoconf gcc g++ make openssl-dev curl"
apk add --no-cache --update $lib
if [ -n "$2" ];then
	rely=$2
    apk add --no-cache --update ${rely//,/" "}
fi
curl -O http://pecl.php.net/get/$1.tgz
tar -xzvf $1.tgz
cd $1
phpize
./configure --with-php-config=/usr/bin/php-config
make
make install
echo extension=$3.so > /etc/php7/conf.d/10_$3.ini
killall php-fpm7
php-fpm7
#apk del $lib