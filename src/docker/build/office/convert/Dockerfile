FROM docker.dever.cc/office/libreoffice:latest

MAINTAINER Rabin "https://github.com/shemic"

ENV DEMETER_HOME=/usr/local/convert
ENV DEMETER_CONF=env
ENV PATH=$PATH:$DEMETER_HOME

RUN apk add --no-cache --update git curl gcc g++ python-dev py-pip openssl-dev libffi-dev imagemagick imagemagick-dev && \
	pip install --upgrade pip && \
	pip install gevent==1.2 && \
	pip install redis && \
	pip install wand && \
	pip install -U git+http://git.dever.cc:3000/python/demeter.git && \
	git clone http://git.dever.cc:3000/python/convert.git $DEMETER_HOME && \
	curl -O https://fossies.org/linux/misc/poppler-data-0.4.9.tar.gz && \
	tar -zxvf poppler-data-0.4.9.tar.gz && \
	cd poppler-data-0.4.9 && \
	make install datadir=/usr/share && \
	#chmod -R +x $DEMETER_HOME/*.py && \
	apk del curl gcc g++ python-dev

EXPOSE 8087 8088

COPY convert.sh /entrypoint/convert.sh