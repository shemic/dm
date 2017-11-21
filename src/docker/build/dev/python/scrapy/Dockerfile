FROM docker.dever.cc/dev/python/v3:latest

MAINTAINER Rabin "https://github.com/shemic"

RUN apk update && apk add --no-cache python3-dev gcc g++ automake libxml2 libxml2-dev libxslt-dev libffi-dev openssl openssl-dev && \
	pip3 install incremental && \
	pip3 install scrapy && \
	apk del gcc g++ automake python3-dev