#!/bin/bash
set -e

start_zookeeper()
{
	check spark
	#ln -s /share/lib/hbase /usr/local/hbase
    if [ "$1" != '' ]; then
        echo $1 > /root/zookeeper/tmp/myid
    fi
    zkServer.sh start
    #hdfs zkfc -formatZK
}

stop_zookeeper()
{
	#rm -rf /usr/local/hbase
	zkServer.sh stop
}