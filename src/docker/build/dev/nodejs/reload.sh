#!/usr/bin/env sh
set -e

if [ $1 == "reload" ]; then
	while true
	do
		pm2 reload all
		sleep 3
	done
fi