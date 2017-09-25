#!/bin/bash
set -e

dever_python()
{
	e=${1}" "${2}"/main.py"
	eval $e
	echo $e
	echo 'Python web init process complete; ready for start up.'
}

dever_start()
{
	if [ -n "$PYTHON_PATH" ] ; then
		dever_python $1 $PYTHON_PATH
	else
		dever_python $1 $2
	fi
}

if [ "$1" = 'python-web' ]; then
	p="/src"
	m="python"
	dever_start $m $p
fi

exec $0