#!/usr/bin/env sh
set -e
lib="php5-dev m4 autoconf gcc g++ make openssl-dev curl"
apk add --no-cache --update $lib
if [ -n "$3" ];then
	rely=$3
    apk add --no-cache --update ${rely//,/" "}
fi
curl -O http://pecl.php.net/get/$1.tgz
tar -xzvf $1.tgz
cd $1
phpize
./configure --with-php-config=/usr/bin/php-config $4
make
make install
echo extension=$2.so > /etc/php7/conf.d/$2.ini
killall php-fpm
php-fpm
#apk del $lib