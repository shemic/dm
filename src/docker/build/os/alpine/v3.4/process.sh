#!/usr/bin/env sh
set -e
process_status()
{
    pids=`ps aux|grep $1|grep -v entrypoint|grep -v grep|awk '{print $1}'`
    if [ "$pids" ]; then
        echo $pids
    else
        echo 1
    fi
}
process_start()
{
    status=`process_status $1`
    if [ "$status" == 1 ]; then
        echo "$1 starting"
        $@ >/dev/null &
        echo "$1 started"
    else
        echo "$1 started"
    fi
}
process_stop()
{
    status=`process_status $1`
    if [ "$status" == 1 ]; then
        echo "$1 stoped"
    else
        echo "stoping $1"
        for pid in $status
        do
            kill -TERM ${pid} >/dev/null 2>&1
        done
        echo "$1 stoped"
    fi
}
process_restart()
{
    process_stop $1
    sleep 5
    p=`process_command`
    echo `$p`
}
process_monit()
{
    status=`process_status $1`
    if [ "$status" == 1 ]; then
        p=`process_command`
        echo `$p`
    fi
}
process_command()
{
    p=$(cat /process)
    echo $p
}