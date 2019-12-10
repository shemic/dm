#!/usr/bin/env sh
set -e
process_status()
{
    pids=`ps aux|grep '$*'|grep -v entrypoint|grep -v grep|awk '{print $1}'`
    if [ "$pids" ]; then
        echo $pids
    else
        echo 1
    fi
}
process_start()
{
    status=`process_status $*`
    if [ "$status" == 1 ]; then
        echo "$* starting"
        $@ >/dev/null &
        echo "$* started"
    else
        echo "$* started"
    fi
}
process_stop()
{
    status=`process_status $*`
    if [ "$status" == 1 ]; then
        echo "$* stoped"
    else
        echo "stoping $*"
        for pid in $status
        do
            kill -TERM ${pid} >/dev/null 2>&1
        done
        echo "$* stoped"
    fi
}
process_restart()
{
    process_stop $*
    sleep 5
    p=`process_command`
    echo `$p`
}
process_monit()
{
    status=`process_status $*`
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