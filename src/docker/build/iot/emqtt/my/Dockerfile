FROM docker.dever.cc/os/alpine:latest

MAINTAINER Rabin "https://github.com/shemic"

RUN mkdir /src
VOLUME ["/src"]
WORKDIR /src

RUN apk add --no-cache --update erlang git make perl && \
	git clone https://github.com/emqtt/emq-relx.git && \
	cd emq-relx && \
	make && \

EXPOSE 1883 8083 8883 8084 18083

COPY emqtt.sh /entrypoint/emqtt.sh