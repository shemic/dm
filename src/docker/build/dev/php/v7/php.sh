#!/usr/bin/env sh
set -e
PHP="php-fpm7"
start_php()
{
	# 使用exec 将替换主进程，信号检测将失效，无法执行end_php
	#exec php-fpm
	process_start $PHP
}

stop_php()
{
	process_stop $PHP
}

monit_php()
{
	process_monit $PHP
}