FROM docker.dever.cc/os/alpine:latest

MAINTAINER Rabin "https://github.com/shemic"

ENV NFS_DIR=/files
ENV NFS_DOMAIN=*
ENV NFS_OPTION=rw,fsid=0,sync,no_subtree_check,no_auth_nlm,insecure,no_root_squash,crossmnt,no_acl

RUN apk add --no-cache --update nfs-utils && \
    mkdir -p /var/lib/nfs/v4recovery

COPY nfs.sh /entrypoint/nfs.sh

EXPOSE 111/tcp 111/udp 2049/tcp 2049/udp

VOLUME /files
WORKDIR /files