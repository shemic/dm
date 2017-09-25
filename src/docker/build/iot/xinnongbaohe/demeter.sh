#!/usr/bin/env sh
set -e
start_demeter()
{
    #supervisord -c /etc/supervisor/supervisord.conf
    cd $DEMETER_LIB
    git pull
    cd $DEMETER_HOME
    git reset --hard
    git pull
    chmod -R +x $DEMETER_HOME/*.py
    install.py
    process_start admin.py
    process_start front.py
    process_start web.py
    process_start sub.py
    process_start cron.py
    #supervisorctl start admin
    #supervisorctl start front
    #supervisorctl start sub
    #supervisorctl start daemon
}

stop_demeter()
{
	process_stop admin.py
    process_stop front.py
    process_stop web.py
    process_stop sub.py
    process_stop cron.py
	#supervisorctl stop admin
    #supervisorctl stop front
    #supervisorctl stop sub
    #supervisorctl stop daemon
}

monit_demeter()
{
    process_monit admin.py
    process_monit front.py
    process_monit web.py
    process_monit sub.py
    process_monit cron.py
}