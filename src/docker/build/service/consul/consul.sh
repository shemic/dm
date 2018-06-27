#!/usr/bin/env sh
set -e

start_consul()
{
	ip=`get_ip 10`
	if [ "$1" == "server" ]; then
		process_start consul agent -server -bootstrap-expect 1 -data-dir /root/consul/data -config-dir /root/consul/config -client 0.0.0.0
	elif [ "$1" == "client" ]; then
		process_start consul agent -client -config-dir /root/consul/config -join 0.0.0.0
	elif [ `echo $@|grep bind|wc -l` -eq 1 ];then
		process_start consul agent $@
	elif [ `echo $@|grep node|wc -l` -eq 1 ];then
		process_start consul agent $@ -bind=$ip
	else
		process_start consul agent $@ -bind=$ip -node=$ip
	fi
	#consul members
}

stop_consul()
{
	process_stop consul
}

monit_consul()
{
	process_monit consul
}