#!/usr/bin/env sh
set -e
start_demeter()
{
    install.py
    cd $DEMETER_HOME
    git pull
    process_start admin.py
}

stop_demeter()
{
	process_stop admin.py
}

monit_demeter()
{
    process_monit admin.py
}