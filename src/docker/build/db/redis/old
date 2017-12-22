FROM docker.dever.cc/dev/python:latest

MAINTAINER Rabin "https://github.com/shemic"

RUN apk add --update redis git && \
	echo 'vm.overcommit_memory = 1' >> /etc/sysctl.conf && \
	echo "echo never > /sys/kernel/mm/transparent_hugepage/enabled" >> /etc/rc.local && \
	pip install tornado && \
	pip install redis && \
	pip install python-dateutil && \
	cd /usr/local && \
	git clone https://github.com/kumarnitin/RedisLive.git redislive && \
	apk del git

COPY redis-live.conf /usr/local/redislive/src/redis-live.conf
COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

CMD ["redis"]