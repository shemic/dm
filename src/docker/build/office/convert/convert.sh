#!/usr/bin/env sh
set -e

start_convert()
{
    mysqladmin -hoffice-mysql -uroot -p123456 create office_convert
    pip install -U git+http://git.dever.cc:3000/python/demeter.git
    cd $DEMETER_HOME
    git pull
    chmod -R +x $DEMETER_HOME/*.py
    python install.py
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