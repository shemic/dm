#!/usr/bin/env sh
set -e

start_elasticsearch()
{
	chmod -R 777 /share/process/elasticsearch
	chmod -R 777 $ES_HOME/config/scripts/
   	process_start elasticsearch -d
}

stop_elasticsearch()
{
	true
}

monit_elasticsearch()
{
	process_monit elasticsearch
}