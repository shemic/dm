FROM docker.dever.cc/os/alpine:latest

MAINTAINER Rabin "https://github.com/shemic"
ENV NGINX_VERSION=1.13.2

RUN apk add --no-cache --update git curl pcre-dev openssl-dev gcc g++ make && \
	curl -O http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz && \
	tar -zxvf nginx-${NGINX_VERSION}.tar.gz && \
	rm -rf nginx-${NGINX_VERSION}.tar.gz && \
	git clone https://github.com/alibaba/nginx-http-concat && \
	cd nginx-${NGINX_VERSION} && \
	./configure --add-module=/nginx-http-concat --prefix=/var/lib/nginx --sbin-path=/usr/sbin/nginx --conf-path=/etc/nginx/nginx.conf --pid-path=/run/nginx/nginx.pid --lock-path=/run/nginx/nginx.lock --http-client-body-temp-path=/var/lib/nginx/tmp/client_body --http-proxy-temp-path=/var/lib/nginx/tmp/proxy --http-fastcgi-temp-path=/var/lib/nginx/tmp/fastcgi --http-uwsgi-temp-path=/var/lib/nginx/tmp/uwsgi --http-scgi-temp-path=/var/lib/nginx/tmp/scgi --user=nginx --group=nginx --with-http_dav_module --with-http_ssl_module --with-http_stub_status_module --with-http_gzip_static_module --with-http_v2_module --with-http_auth_request_module --with-mail --with-mail_ssl_module && \
	make && make install && \

	apk del git curl gcc g++ make