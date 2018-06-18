#!/bin/bash
set -e

start_consul()
{
	if [ "$1" == "server" ]; then
		process_start consul agent -server -bootstrap-expect 1 -data-dir /root/consul/data -config-dir /root/consul/config -client 0.0.0.0
	elif [ "$1" == "client" ]; then
		process_start consul agent -client -config-dir /root/consul/config -join 0.0.0.0
    else
        process_start consul agent $@
	fi
	#consul members
}

stop_consul()
{
	true
}

monit_consul()
{
	true
}