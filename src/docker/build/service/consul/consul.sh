#!/bin/bash
set -e

start_consul()
{
	process_start consul agent -server -bootstrap-expect 1 -data-dir /root/consul/data -config-dir /root/consul/config -client 0.0.0.0
	#consul members
}

stop_consul()
{
	true
}

monit_consul()
{
	process_monit consul
}