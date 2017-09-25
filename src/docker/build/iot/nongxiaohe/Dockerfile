FROM docker.shemic.com/dev/python:latest

MAINTAINER Rabin "https://github.com/shemic"

ENV DEMETER_HOME=/usr/local/demeter
ENV DEMETER_CONF=env
ENV PATH=$PATH:$DEMETER_HOME

RUN apk add --no-cache --update py-gevent py-psycopg2 git && \
	pip install tornado && \
	pip install pytest-runner && \
	pip install paho-mqtt && \
	pip install influxdb && \
	pip install short_url && \
	#pip install hashlib && \
	git clone http://git.shemic.com:3000/atom/nongxiaohe.git $DEMETER_HOME && \
	chmod -R 777 $DEMETER_HOME/* && \
	rm -rf $DEMETER_HOME/runtime/postgresql/*

EXPOSE 8087 8088

COPY demeter.sh /entrypoint/demeter.sh