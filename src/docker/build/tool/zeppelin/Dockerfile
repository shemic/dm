FROM docker.dever.cc/java/zeppelin:latest

MAINTAINER Rabin "https://github.com/shemic"

RUN apk update && apk add --no-cache python3-dev gcc g++ automake lapack lapack-dev gfortran freetype freetype-dev libstdc++ jpeg-dev && \
	# python learn
	pip3 install numpy && \
	pip3 install scipy && \
	pip3 install pandas && \
	pip3 install matplotlib && \
	pip3 install scikit-learn && \
	pip3 install seaborn && \
	pip3 install incremental && \
	pip3 install scrapy && \
	pip3 install gevent && \
	apk del openssl-dev && apk add postgresql-dev && pip3 install psycopg2 && \
	pip3 install pymysql && \
	pip3 install pyecharts && \
	apk del gcc g++ automake gfortran