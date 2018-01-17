#!/usr/bin/env sh
set -e
start_buy()
{
    pip install -U git+http://git.dever.cc:3000/python/demeter.git
    cd $DEMETER_HOME
    git reset --hard FETCH_HEAD
    git pull
    chmod -R +x $DEMETER_HOME/*.py
    install.py
    process_start admin.py
    process_start cron.py
}

stop_buy()
{
	process_stop admin.py
    process_stop cron.py
}

monit_buy()
{
    process_monit admin.py
    process_monit cron.py
}