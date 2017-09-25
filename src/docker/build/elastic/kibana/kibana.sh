#!/usr/bin/env sh
set -e

start_kibana()
{
	kibana >/dev/null &
}

stop_kibana()
{
	true
}

monit_kibana()
{
	process_monit kibana
}