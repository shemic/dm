#!/usr/bin/env sh
set -e

start_convert()
{
    mysqladmin -hoffice_mysql -uroot -p create office_convert
    cd $DEMETER_HOME
    git reset --hard FETCH_HEAD
    git pull
    chmod -R +x $DEMETER_HOME/*.py
    install.py
    process_start nginx
    process_start admin.py
    process_start front.py
    process_start cron.py
}

stop_convert()
{
    process_stop nginx
    process_stop admin.py
    process_stop front.py
    process_stop cron.py
}

monit_convert()
{
    process_monit nginx
	process_monit admin.py
    process_monit front.py
    process_monit cron.py
}