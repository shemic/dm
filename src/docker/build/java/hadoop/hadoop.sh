#!/usr/bin/env sh
set -e

start_share_hadoop()
{
    share $HADOOP_HOME hadoop
}

stop_share_hadoop()
{
    true
}

start_hadoop()
{
	if [ "$1" == "share" ]; then
        start_share_hadoop
    fi
    rm -rf /root/hdfs/*
    rm -rf /root/hadoop/tmp/*
    $HADOOP_HOME/bin/hdfs namenode -format &
    $HADOOP_HOME/sbin/start-dfs.sh &
    $HADOOP_HOME/sbin/start-yarn.sh &
    #$HADOOP_HOME/sbin/start-all.sh &
} 

stop_hadoop()
{
	stop-all.sh &
}

monit_hadoop()
{
    process_monit hdfs
}