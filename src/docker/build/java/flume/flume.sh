#!/bin/bash
set -e

start_flume()
{
	check hadoop
	hadoop_mkdir flume
	#flume-ng agent -n agent1 -c conf -f /usr/local/flume/conf/flume.conf -Dflume.root.logger=DEBUG,console
	if [ "$1" != '' ]; then
		flume-ng agent -n $1 -c conf -f /usr/local/flume/conf/flume.conf 
	else
		flume-ng agent -n agent -c conf -f /usr/local/flume/conf/flume.conf 
	fi
}

stop_flume()
{
	true
}

monit_flume()
{
	process_monit flume-ng
}