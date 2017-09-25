#!/usr/bin/env sh
set -e

start_hive()
{
	check hadoop
	hadoop fs -mkdir -p /hive/warehouse
	hadoop fs -mkdir -p /hive/tmp
	hadoop fs -chmod -R 777 /hive
	hive --service metastore &
	hive --service hiveserver2 &
    echo "start hive"
}

stop_hive()
{
	echo "stop hive"
}