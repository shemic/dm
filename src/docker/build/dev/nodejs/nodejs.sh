#!/usr/bin/env sh
set -e

start_nodejs()
{
	npm install
	npm install -g pm2
	pm2 start main.js --watch
	echo 'Nodejs web init process complete; ready for start up.'
	if [ "$1" == "reload" ]; then
		/entrypoint/reload.sh reload &
	fi
}

stop_nodejs()
{
	pm2 kill
}

monit_nodejs()
{
	process_monit pm2
}