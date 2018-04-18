#!/usr/bin/env sh
set -e
PHP="php-fpm"
start_nginx()
{
	process_start nginx
	process_start $PHP
}

stop_nginx()
{
    nginx -s stop
    process_stop $PHP
}

monit_nginx()
{
	process_monit nginx
	process_monit $PHP
}