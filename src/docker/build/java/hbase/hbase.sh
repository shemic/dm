#!/usr/bin/env sh
set -e

start_share_hbase()
{
    share $HBASE_HOME hbase
}

stop_share_hbase()
{
    true
}

start_hbase()
{
	#share $HBASE_HOME hbase
	check hadoop
	hadoop_mkdir hbase
    start-hbase.sh
}

stop_hbase()
{
	stop-hbase.sh &
}