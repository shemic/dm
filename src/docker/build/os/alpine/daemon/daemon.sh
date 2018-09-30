#!/usr/bin/env sh
set -e
commands="daemon"
start_daemon()
{
	process_start $commands
}

stop_daemon()
{
	process_stop $commands
}

monit_daemon()
{
	process_monit $commands
}