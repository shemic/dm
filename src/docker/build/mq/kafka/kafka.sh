#!/bin/bash
set -e

start_kafka()
{
	kafka-server-start.sh
}

stop_kafka()
{
	kafka-server-end.sh
}