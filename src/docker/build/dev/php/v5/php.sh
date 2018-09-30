#!/usr/bin/env sh
set -e
PHP="php-fpm5"
start_php()
{
	# 使用exec 将替换主进程，信号检测将失效，无法执行end_php
	#exec php-fpm
	process_start $PHP
	process_start crond
}

stop_php()
{
	process_stop $PHP
	process_stop crond
}

monit_php()
{
	process_monit $PHP
	process_monit crond
}