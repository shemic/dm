#!/usr/bin/env sh
set -e
start_rsync()
{
	process_start crond
}

stop_rsync()
{
	process_stop crond
}

monit_rsync()
{
	process_monit crond
}