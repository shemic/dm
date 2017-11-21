FROM docker.dever.cc/dev/python/v3:latest

MAINTAINER Rabin "https://github.com/shemic"

RUN apk update && apk add --no-cache python3-dev gcc g++ automake lapack lapack-dev gfortran freetype freetype-dev && \
	pip3 install numpy && \
	pip3 install scipy && \
	pip3 install pandas && \
	pip3 install matplotlib && \
	pip3 install scikit-learn && \
	apk del gcc g++ automake gfortran