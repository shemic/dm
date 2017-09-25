#!/usr/bin/env sh
set -e

start_oauth2()
{
	process_start /root/oauth2/start.sh
}

monit_oauth2()
{
	process_monit /root/oauth2/start.sh
}