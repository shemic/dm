#!/usr/bin/env sh
set -e

start_nginx()
{
	#exec nginx
	process_start nginx
}

stop_nginx()
{
	process_stop nginx
}

monit_nginx()
{
	process_monit nginx
}