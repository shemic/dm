#!/usr/bin/env sh
set -e

start_logstash()
{
	logstash -f $LOGSTASH_HOME/config/logstash.conf -d
}

stop_logstash()
{
	true
}

monit_logstash()
{
	process_monit logstash
}