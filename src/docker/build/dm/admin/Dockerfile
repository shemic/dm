FROM docker.dever.cc/dev/python:latest

MAINTAINER Rabin "https://github.com/shemic"

ENV ADMIN_HOME=/usr/local/admin
ENV ADMIN_LIB=/usr/lib/python2.7/site-packages/demeter
ENV DEMETER_CONF=env
ENV PATH=$PATH:$ADMIN_HOME

RUN apk add --no-cache --update py-gevent git && \
	pip install -U git+http://git.dever.cc:3000/python/demeter.git && \
	git clone http://git.dever.cc:3000/demeter/admin.git $ADMIN_HOME && \
	chmod -R +x $ADMIN_HOME/*.py

EXPOSE 8011 8012

COPY admin.sh /entrypoint/admin.sh