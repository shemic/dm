FROM docker.dever.cc/dev/python/v3:latest

MAINTAINER Rabin "https://github.com/shemic"

RUN apk update && apk add --no-cache python3-dev gcc g++ automake lapack lapack-dev gfortran && \
	pip3 install scipy && \
	apk del gcc g++ automake gfortran