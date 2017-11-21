#!/bin/bash
set -e

start_jupyter()
{
	jupyter notebook --allow-root --no-browser --notebook-dir=/usr/local/jupyter --port=8888 --ip=*
}

stop_jupyter()
{
	true
}

monit_jupyter()
{
	process_monit jupyter
}