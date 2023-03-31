#!/usr/bin/env sh
set -e

if [ -n "$1" ];then
	docker images|grep $1|awk '{print $1}'|xargs docker rmi -f
else
	docker images|awk '{print $3}'|xargs docker rmi -f
fi