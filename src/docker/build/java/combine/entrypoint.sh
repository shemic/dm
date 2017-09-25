#!/bin/sh
set -e

init()
{
    /usr/sbin/sshd
}

loadStart()
{
    dir=/entrypoint/
    loop=$(ls -l $dir |awk '{print $9}')
    for i in $loop
    do
        source $dir$i
    done
}

start()
{
	loadStart
    if [[ $1 =~ "-" ]]; then
        OLD_IFS="$IFS"
        IFS="-"
        arr=($1)
        IFS="$OLD_IFS"
        start="start_${arr[0]}"
        echo $start
        eval $start ${arr[1]}
    else
        start="start_$1"
        echo $start
        eval $start
    fi
}

init

if [ "$1" != "sh" ]; then
    for args in $@
    do
        start $args
        echo -e "\n"
    done
fi
jps
netstat -apn

exec sh