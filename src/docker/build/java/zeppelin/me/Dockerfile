FROM docker.shemic.com/dev/java:latest

MAINTAINER Rabin "https://github.com/shemic"

# set environment variable
ENV ZEPPELIN_HOME=/usr/local/zeppelin \
	ZEPPELIN_VERSION=0.7.2 \
	ZEPPELIN_TYPE=dever \
	PATH=$PATH:$ZEPPELIN_HOME/bin

COPY zeppelin-$ZEPPELIN_VERSION-bin-$ZEPPELIN_TYPE $ZEPPELIN_HOME
COPY entrypoint.sh /entrypoint.sh

RUN apk update && apk add --no-cache bash

VOLUME ["/usr/local/zeppelin/conf"]

ENTRYPOINT ["/entrypoint.sh"]

CMD ["sh"]
