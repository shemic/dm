#!/usr/bin/env sh
set -e

start_nfs()
{
	echo "$NFS_DIR $NFS_DOMAIN($NFS_OPTION)" > /etc/exports
    process_start /usr/sbin/exportfs -r
    process_start /sbin/rpcbind -s
    process_start /usr/sbin/rpc.nfsd --no-nfs-version 2 --no-nfs-version 3 8 |:
    process_start /usr/sbin/rpc.mountd -F
}

stop_nfs()
{
    process_stop rpcbind
}

monit_nfs()
{
	process_monit rpcbind
}