FROM docker.dever.cc/office/libreoffice:latest

MAINTAINER Rabin "https://github.com/shemic"

ENV DEMETER_HOME=/usr/local/convert
ENV DEMETER_CONF=env
ENV PATH=$PATH:$DEMETER_HOME


RUN echo -e '@community http://mirrors.ustc.edu.cn/alpine/edge/community' >> /etc/apk/repositories

#rm -rf $DEMETER_HOME/runtime/mysql/* && \
# apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev && pip install pillow && pip install pdf2image

#git clone https://github.com/dawbarton/pdf2svg && cd pdf2svg && cp README.md README && ./configure && make && make install

RUN apk add --no-cache --update git curl nginx gcc g++ python-dev py-pip make cmake m4 openssl-dev libffi-dev imagemagick6@community imagemagick6-dev@community && \
	pip install --upgrade pip && \
	pip install gevent==1.2 && \
	pip install redis && \
	pip install wand && \
	pip install pdf2jpg && \
	pip install -U git+http://git.dever.cc:3000/python/demeter.git && \
	git clone http://git.dever.cc:3000/python/convert.git $DEMETER_HOME && \
	curl -O https://fossies.org/linux/misc/poppler-data-0.4.9.tar.gz && \
	tar -zxvf poppler-data-0.4.9.tar.gz && \
	cd poppler-data-0.4.9 && \
	make install datadir=/usr/share && \
	mkdir /run/nginx/ && \
	rm -rf /etc/nginx/conf.d/default.conf && \
	apk del curl m4 make cmake gcc g++ python-dev

EXPOSE 8087 8088 80 443

COPY convert.sh /entrypoint/convert.sh
COPY convert.conf /etc/nginx/conf.d/convert.conf