#!/bin/bash
set -e

if [ "${1:0:1}" = '-' ]; then
	set -- memcached "$@"
fi

dever_memcache()
{
	e=${1}" -u root -d -p "${2}" "${3}
	eval $e
	echo $e
	echo 'Memcached init process complete; ready for start up.'
}

dever_start()
{
	if [ -n "$MEMCACHED_PORT" ] ; then
		ifs="-"
		if [[ $MEMCACHED_PORT =~ $ifs ]] ; then
			port=(${MEMCACHED_PORT//-/ })
			for i in ${port[@]} ;
			do
				dever_memcache $1 $i $3
			done
		else
			dever_memcache $1 $MEMCACHED_PORT $3

		fi
	else
		dever_memcache $1 $2 $3
	fi
}

if [ "$1" = 'memcached' ]; then
	d=11211
	c=$MEMCACHED_COMMAND
	m="memcached"
	dever_start $m $d $c
fi

exec $0