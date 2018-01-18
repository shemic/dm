#!/usr/bin/env sh
set -e
start_buy()
{
    pip install -U git+http://git.dever.cc:3000/python/demeter.git
    cd $DEMETER_HOME
    git reset --hard FETCH_HEAD
    git pull
    chmod -R +x $DEMETER_HOME/*.py
    python install.py
    process_start python admin.py
    process_start python cron.py
}

stop_buy()
{
	process_stop python admin.py
    process_stop python cron.py
}

monit_buy()
{
    process_monit python admin.py
    process_monit python cron.py
}