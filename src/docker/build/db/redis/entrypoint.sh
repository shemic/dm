#!/bin/bash
set -e

dever_start()
{
	redis-server &
	cd /usr/local/redislive/src/
	./redis-monitor.py --duration=120 > /dev/null &
	./redis-live.py > /dev/null &	
}

if [ "$1" = 'redis' ]; then
	d=6379
	dever_start $d
fi

exec sh