FROM docker.dever.cc/dev/python/v3:latest

MAINTAINER Rabin "https://github.com/shemic"

RUN apk update && apk add --no-cache python3-dev gcc g++ automake freetype freetype-dev && \
	pip3 install matplotlib && \
	apk del gcc g++ automake