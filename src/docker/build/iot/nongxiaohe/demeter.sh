#!/usr/bin/env sh
set -e
start_demeter()
{
    cd $DEMETER_LIB
    git pull
    cd $DEMETER_HOME
    git reset --hard FETCH_HEAD
    git pull
    chmod -R +x $DEMETER_HOME/*.py
    install.py
    process_start admin.py
    process_start web.py
    process_start front.py
    process_start sub.py
}

stop_demeter()
{
	process_stop admin.py
    process_stop web.py
    process_stop front.py
    process_stop sub.py
}

monit_demeter()
{
    process_monit admin.py
    process_monit web.py
    process_monit front.py
    process_monit sub.py
}