#!/usr/bin/env sh
set -e
start_iot()
{
    cd $IOT_HOME
    git reset --hard FETCH_HEAD
    git pull
    install.py
    process_start python3 admin.py
    process_start python3 front.py
    process_start python3 modbus.py -m tcp_start
    process_start python3 modbus.py -m rtu_start
    process_start python3 cron.py -m control
    process_start python3 cron.py -m device
    process_start python3 cron.py -m loop
    process_start python3 cron.py -m queue
    process_start python3 cron.py -m queuedrop
    process_start python3 cron.py -m savepic
    process_start python3 cron.py -m timesync
    process_start python3 cron.py -m timing
    process_start python3 cron.py -m mqtt_sub
    #process_start cron.py -m mqtt_pub
    process_start ngrok -subdomain="f$IOT_FARM" -config="ngrok.cfg" 8091
}

stop_iot()
{
	process_stop python3 admin.py
    process_stop python3 front.py
    process_stop python3 modbus.py -m tcp_start
    process_stop python3 modbus.py -m rtu_start
    process_stop python3 cron.py -m control
    process_stop python3 cron.py -m device
    process_stop python3 cron.py -m loop
    process_stop python3 cron.py -m queue
    process_stop python3 cron.py -m queuedrop
    process_stop python3 cron.py -m savepic
    process_stop python3 cron.py -m timesync
    process_stop python3 cron.py -m timing
    process_stop python3 cron.py -m mqtt_sub
}

monit_iot()
{
    process_monit python3 admin.py
    process_monit python3 front.py
    process_monit python3 modbus.py -m tcp_start
    process_monit python3 modbus.py -m rtu_start
    process_monit python3 cron.py -m control
    process_monit python3 cron.py -m device
    process_monit python3 cron.py -m loop
    process_monit python3 cron.py -m queue
    process_monit python3 cron.py -m queuedrop
    process_monit python3 cron.py -m savepic
    process_monit python3 cron.py -m timesync
    process_monit python3 cron.py -m timing
    process_monit python3 cron.py -m mqtt_sub
    process_monit ngrok -subdomain="f$IOT_FARM" -config="ngrok.cfg" 8091
}