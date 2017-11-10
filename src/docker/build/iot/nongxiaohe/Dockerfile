FROM docker.dever.cc/dev/python:latest

MAINTAINER Rabin "https://github.com/shemic"

ENV DEMETER_HOME=/usr/local/demeter
ENV DEMETER_LIB=/usr/lib/python2.7/site-packages/demeter
ENV DEMETER_CONF=env
ENV PATH=$PATH:$DEMETER_HOME

RUN apk add --no-cache --update py-gevent py-psycopg2 git && \
	apk add --no-cache jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl gcc g++ python-dev && \
	pip install pillow && \
	pip install tornado && \
	pip install pytest-runner && \
	pip install paho-mqtt && \
	pip install influxdb && \
	pip install short_url && \
	pip install oss2 --upgrade && \
	#pip install qrcode && \
	git clone http://git.dever.cc:3000/python/demeter.git $DEMETER_LIB && \
	git clone http://git.dever.cc:3000/python/nongxiaohe.git $DEMETER_HOME && \
	#mkdir -p /etc/supervisor/conf.d/ && \
	chmod -R +x $DEMETER_HOME/*.py && \
	apk del curl gcc g++ python-dev

EXPOSE 8087 8088

COPY demeter.sh /entrypoint/demeter.sh
#COPY supervisor/ /etc/supervisor/