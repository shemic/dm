FROM docker.dever.cc/os/alpine:latest

MAINTAINER Rabin "https://github.com/shemic"

RUN apk --no-cache add rsync lua lua-dev git gcc g++ libgc++ make cmake && \
	git clone https://github.com/axkibe/lsyncd.git && \
	cd lsyncd && \
	cmake . && \
	make && make install && \
	apk del git gcc g++ libgc++ make cmake && \
    rm -rf /tmp/* /var/cache/apk/*