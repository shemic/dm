FROM docker.dever.cc/dev/python/v3:latest

MAINTAINER Rabin "https://github.com/shemic"

RUN apk update && apk add --no-cache curl && \
	curl -O https://pypi.python.org/packages/b6/fc/34342ee8ea0c413679ddfb23d73a132fc7ecbf479383de9f0946344ec73c/numpy-1.13.3-cp27-cp27m-manylinux1_x86_64.whl#md5=64bc7dc4a503398e0b4cc48778136374 && \
	pip install numpy-1.13.3-cp27-cp27m-manylinux1_x86_64.whl