FROM docker.dever.cc/dev/python/v3:latest

MAINTAINER Rabin "https://github.com/shemic"

RUN apk update && apk add --no-cache freetype lapack gfortran libstdc++
RUN apk add --no-cache --virtual=.build-deps python3-dev gcc g++ automake lapack-dev freetype-dev && \
	pip3 install --no-binary=:all: numpy && \
	pip3 install scipy && \
	pip3 install pandas && \
	pip3 install matplotlib && \
	pip3 install scikit-learn && \
	pip3 install seaborn && \
	apk del .build-deps