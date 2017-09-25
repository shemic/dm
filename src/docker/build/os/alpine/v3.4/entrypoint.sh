#!/usr/bin/env sh
set -e
hosts()
{
    if [ `id -u` -eq 0 ];then
        host="/etc/hosts.main"
        yes="/etc/hosts.yes"
        if [ ! -s "$yes" ]; then
            if [ -s "$host" ]; then
                while read line
                do
                echo $line >> /etc/hosts
                done < $host
                echo "yes" > $yes
            fi
        fi
    fi
}
process()
{
    echo "$1 Startup Completed" > /share/process/$1
}
check()
{
    path="process"
    if [ -n "$2" ];then
        path="$2"
    fi
    process="/share/$path/$1"
    while [ ! -s "$process" ]; do
        true
    done
}
share()
{
    path=/share/lib/$2
    if [ ! -d "$path" ]; then  
        mkdir -p "$path"
    fi
    cp -R $1/* $path
}
hadoop_mkdir()
{
    dir=$(hadoop fs -ls / | grep $1 | wc -l)
    if [ $dir -eq 0 ] ;then
        for i in $@
        do
            hadoop fs -mkdir -p /$i
        done
    fi
}
load()
{
    dir=/entrypoint/
    loop=$(ls -l $dir |awk '{print $9}')
    for i in $loop
    do
        source $dir$i
    done
}
define()
{
    state=1
    type $1 >/dev/null ||
    {
        state=2
    }
    echo $state
}
start()
{
    if [ -n "$1" ];then
        start="start_$@"
        state=`define $start`
        if [ $state = 1 ];then
            echo $start
            status=`$start`
            echo $status
            netstat -apn
            process $1
        fi
    fi
}
stop()
{
    if [ -n "$1" ];then
        stop="stop_$@"
        state=`define $stop`
        if [ $state = 1 ];then
            echo $stop
            status=`$stop`
            echo $status
            rm -rf /share/process/$1
        fi
    fi
}
monit()
{
    if [ -n "$1" ];then
        monit="monit_$@"
        state=`define $monit`
        if [ $state = 1 ];then
            status=`$monit`
        fi
    fi
}
load
hosts
start $@
if [ "$2" == "exit" ]; then
    exit 0
fi
trap "stop $1" HUP INT QUIT ABRT KILL ALRM TERM EXIT

while true
do
    monit $@
    sleep 10
done
#exec sh
exit 0