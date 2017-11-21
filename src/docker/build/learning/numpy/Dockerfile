FROM docker.dever.cc/dev/python/v3:latest

MAINTAINER Rabin "https://github.com/shemic"

RUN apk update && apk add --no-cache python3-dev gcc g++ automake && \
	pip3 install numpy && \
	apk del gcc g++ automake