#!/usr/bin/env sh
set -e

if [ -n "$2" ];then
	docker tag $1 $2
	docker push $2
	docker rmi -f $2
else
	docker push $1
fi