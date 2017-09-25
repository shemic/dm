#!/usr/bin/env sh
set -e

start_filebeat()
{
	cp -R $FILEBEAT_HOME/config/filebeat.yml $FILEBEAT_HOME/filebeat.yml
	$FILEBEAT_HOME/filebeat -c $FILEBEAT_HOME/filebeat.yml &
}

monit_filebeat()
{
	process_monit filebeat
}