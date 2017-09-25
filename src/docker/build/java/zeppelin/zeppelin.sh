#!/bin/sh
set -e

start_zeppelin()
{
    $ZEPPELIN_HOME/bin/zeppelin-daemon.sh start
}

stop_zeppelin()
{
	echo "end"
}