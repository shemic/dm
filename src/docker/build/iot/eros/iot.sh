#!/usr/bin/env sh
set -e
start_iot()
{
    cd $IOT_HOME
    git reset --hard FETCH_HEAD
    git pull
    install.py
    process_start {$IOT_HOME}/admin.py
    process_start {$IOT_HOME}/front.py
    process_start {$IOT_HOME}/modbus.py -m tcp_start
    process_start {$IOT_HOME}/modbus.py -m rtu_start
    process_start {$IOT_HOME}/cron.py -m control
    process_start {$IOT_HOME}/cron.py -m device
    process_start {$IOT_HOME}/cron.py -m loop
    process_start {$IOT_HOME}/cron.py -m queue
    process_start {$IOT_HOME}/cron.py -m queuedrop
    process_start {$IOT_HOME}/cron.py -m savepic
    process_start {$IOT_HOME}/cron.py -m timesync
    process_start {$IOT_HOME}/cron.py -m timing
    process_start {$IOT_HOME}/cron.py -m mqtt_sub
    #process_start cron.py -m mqtt_pub
    process_start ngrok -subdomain="f{$IOT_FARM}" -config="{$IOT_HOME}/ngrok.cfg" 8091
}

stop_iot()
{
	process_stop {$IOT_HOME}/admin.py
    process_stop {$IOT_HOME}/front.py
    process_stop {$IOT_HOME}/modbus.py -m tcp_start
    process_stop {$IOT_HOME}/modbus.py -m rtu_start
    process_stop {$IOT_HOME}/cron.py -m control
    process_stop {$IOT_HOME}/cron.py -m device
    process_stop {$IOT_HOME}/cron.py -m loop
    process_stop {$IOT_HOME}/cron.py -m queue
    process_stop {$IOT_HOME}/cron.py -m queuedrop
    process_stop {$IOT_HOME}/cron.py -m savepic
    process_stop {$IOT_HOME}/cron.py -m timesync
    process_stop {$IOT_HOME}/cron.py -m timing
    process_stop {$IOT_HOME}/cron.py -m mqtt_sub
}

monit_iot()
{
    process_monit {$IOT_HOME}/admin.py
    process_monit {$IOT_HOME}/front.py
    process_monit {$IOT_HOME}/modbus.py -m tcp_start
    process_monit {$IOT_HOME}/modbus.py -m rtu_start
    process_monit {$IOT_HOME}/cron.py -m control
    process_monit {$IOT_HOME}/cron.py -m device
    process_monit {$IOT_HOME}/cron.py -m loop
    process_monit {$IOT_HOME}/cron.py -m queue
    process_monit {$IOT_HOME}/cron.py -m queuedrop
    process_monit {$IOT_HOME}/cron.py -m savepic
    process_monit {$IOT_HOME}/cron.py -m timesync
    process_monit {$IOT_HOME}/cron.py -m timing
    process_monit {$IOT_HOME}/cron.py -m mqtt_sub
    process_monit ngrok -subdomain="f{$IOT_FARM}" -config="{$IOT_HOME}/ngrok.cfg" 8091
}