#!/usr/bin/env sh
set -e
start_sshd()
{
	/usr/sbin/sshd
}
check jdk lib
hosts
start_sshd