#!/usr/bin/env sh
set -e

start_nginx()
{
	#exec nginx
	process_start nginx
}

stop_nginx()
{
    nginx -s stop
}

monit_nginx()
{
	process_monit nginx
}