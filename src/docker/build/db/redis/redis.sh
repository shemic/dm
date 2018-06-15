#!/usr/bin/env sh
set -e

start_redis()
{
	redis-server /etc/redis.conf &
	cd /usr/local/redislive/src/
	./redis-monitor.py --duration=120 > /dev/null &
	./redis-live.py > /dev/null &	
}

stop_redis()
{
    nginx -s stop
}

monit_redis()
{
	process_monit redis-server /etc/redis.conf
}