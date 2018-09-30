FROM docker.dever.cc/os/alpine:latest

MAINTAINER Rabin "https://github.com/shemic"

RUN apk update && apk add --no-cache rsync

COPY rsync.sh /entrypoint/rsync.sh

CMD ["rsync"]