#!/usr/bin/env sh
set -e
start_admin()
{
    cd $ADMIN_LIB
    git pull
    cd $ADMIN_HOME
    git reset --hard FETCH_HEAD
    git pull
    chmod -R +x $ADMIN_HOME/*.py
    python install.py
    process_start admin.py
    process_start cron.py
}

stop_admin()
{
	process_stop admin.py
    process_stop cron.py
}

monit_admin()
{
    process_monit admin.py
    process_monit cron.py
}