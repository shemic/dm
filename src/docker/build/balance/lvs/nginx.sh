#!/usr/bin/env sh
set -e

start_nginx()
{
	#exec nginx
	nginx &
}

stop_nginx()
{
    nginx -s stop
}