#!/usr/bin/env sh
set -e
lib="php5-dev m4 autoconf gcc g++ make openssl-dev curl wget"
apk add --no-cache --update $lib
if [ -n "$3" ];then
	rely=$3
    apk add --no-cache --update ${rely//,/" "}
fi
curl -O http://pecl.php.net/get/$1.tgz
tar -xzvf $1.tgz
rm -rf $1.tgz
cd $1
phpize
if [ -n "$4" ];then
	config=$4
	./configure --with-php-config=/usr/bin/php-config ${config//,/" "}
else
	./configure --with-php-config=/usr/bin/php-config
fi
make
make install
echo extension=$2.so > /etc/php5/conf.d/$2.ini
killall -9 php-fpm && php-fpm &
#apk del $lib