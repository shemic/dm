FROM docker.dever.cc/dev/python:latest

MAINTAINER Rabin "https://github.com/shemic"

ENV PGADMIN_HOME=/usr/local/hadoop 
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

RUN apk add --no-cache --update postgresql curl && \
	curl -O https://ftp.postgresql.org/pub/pgadmin/pgadmin4/v1.6/pip/pgadmin4-1.6-py2.py3-none-any.whl && \
	pip pgadmin4-1.6-py2.py3-none-any.whl && \


RUN mkdir /data

VOLUME ["/data"]

ENTRYPOINT ["sh"]