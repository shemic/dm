FROM docker.dever.cc/os/alpine:latest

MAINTAINER Rabin "https://github.com/shemic"

RUN apk add --no-cache --update nginx mysql-client python py-virtualenv && \
	mkdir /run/nginx/ && \
	rm -rf /etc/nginx/conf.d/default.conf && \
	pip install virtualenv && \
	pip install flask && \
	git clone https://github.com/meolu/walle-web.git /walle-web && \
	cd /walle-web && \
	sh admin.sh init && \
	virtualenv --no-site-packages -p python venv && \
	sed -i "s/user:password@localhost:3306/root:123456@web-mysql:3306/g" /walle-web/walle/config/settings_prod.py && \
	mysql  -hweb-mysql -uroot -p123456 -e 'CREATE SCHEMA walle' && \
	sh admin.sh migration && \


#COPY walle.sh /entrypoint/walle.sh
#COPY walle.conf /etc/nginx/conf.d/walle.conf