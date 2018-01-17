FROM docker.dever.cc/learning/opencv:latest

MAINTAINER Rabin "https://github.com/shemic"

RUN apk update && apk add --no-cache cmake build-base boost-dev && \
	pip3 install dlib && \
	apk del cmake build-base