FROM docker.dever.cc/spider/xvfb:latest

MAINTAINER Rabin "https://github.com/shemic"

ENV DEMETER_HOME=/usr/local/buy
ENV PATH=$PATH:$DEMETER_HOME
ENV DEMETER_CONF=env

RUN apk add --no-cache --update gcc g++ make python-dev py-psycopg2 git && \
	pip install -U git+http://git.dever.cc:3000/python/demeter.git && \
	git clone http://git.dever.cc:3000/python/buy.git $DEMETER_HOME && \
	chmod -R +x $DEMETER_HOME/*.py && \
	apk del gcc g++ make python-dev

EXPOSE 8087 8088

COPY buy.sh /entrypoint/buy.sh