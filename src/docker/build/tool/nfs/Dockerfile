FROM docker.dever.cc/os/alpine:latest

MAINTAINER Rabin "https://github.com/shemic"

RUN apk update && apk add --no-cache nfs-utils
ADD entrypoint.sh /entrypoint.sh
ADD exports /etc/exports

ENTRYPOINT ["/entrypoint.sh"]

CMD ["sh"]