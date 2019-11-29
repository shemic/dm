#!/usr/bin/env sh
set -e
start_iot()
{
    cd $IOT_HOME
    git reset --hard FETCH_HEAD
    git pull
    install.py
    process_start admin.py
    process_start front.py
    process_start modbus.py -m tcp_start
    process_start modbus.py -m rtu_start
    process_start cron.py -m control
    process_start cron.py -m device
    process_start cron.py -m loop
    process_start cron.py -m queue
    process_start cron.py -m queuedrop
    process_start cron.py -m savepic
    process_start cron.py -m timesync
    process_start cron.py -m timing
    process_start cron.py -m mqtt_sub
    #process_start cron.py -m mqtt_pub
}

stop_iot()
{
	process_stop admin.py
    process_stop front.py
    process_stop modbus.py -m tcp_start
    process_stop modbus.py -m rtu_start
    process_stop cron.py -m control
    process_stop cron.py -m device
    process_stop cron.py -m loop
    process_stop cron.py -m queue
    process_stop cron.py -m queuedrop
    process_stop cron.py -m savepic
    process_stop cron.py -m timesync
    process_stop cron.py -m timing
    process_stop cron.py -m mqtt_sub
}

monit_iot()
{
    process_monit admin.py
    process_monit front.py
    process_monit modbus.py -m tcp_start
    process_monit modbus.py -m rtu_start
    process_monit cron.py -m control
    process_monit cron.py -m device
    process_monit cron.py -m loop
    process_monit cron.py -m queue
    process_monit cron.py -m queuedrop
    process_monit cron.py -m savepic
    process_monit cron.py -m timesync
    process_monit cron.py -m timing
    process_monit cron.py -m mqtt_sub
}