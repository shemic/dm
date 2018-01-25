#!/bin/bash
set -e

start_jupyter()
{
	jupyter notebook --allow-root --no-browser --notebook-dir=/src --port=8888 --ip=0.0.0.0 --debug &
	if [ "$1" == "lab" ]; then
        start_jupyterlab
    fi
}

start_jupyterlab()
{
	jupyter lab --allow-root --no-browser --notebook-dir=/src --port=8889 --ip=0.0.0.0 &
}

stop_jupyter()
{
	true
}

monit_jupyter()
{
	process_monit jupyter
}