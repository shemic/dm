FROM docker.dever.cc/os/alpine:latest

MAINTAINER Rabin "https://github.com/shemic"

COPY daemon.sh /entrypoint/daemon.sh
COPY daemon.py /usr/bin/daemon
RUN apk add --no-cache --update python git && chmod +x /usr/bin/daemon

CMD ["daemon"]