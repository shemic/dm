FROM docker.dever.cc/db/postgresql:latest

MAINTAINER Rabin "https://github.com/shemic"

RUN apk add --no-cache --update python py-pip python-dev pkgconf gcc gmp-dev postgresql-dev curl && \
	curl -O https://ftp.postgresql.org/pub/pgadmin/pgadmin4/v1.6/pip/pgadmin4-1.6-py2.py3-none-any.whl && \
	pip install pgadmin4-1.6-py2.py3-none-any.whl && \
	rm pgadmin4-1.6-py2.py3-none-any.whl