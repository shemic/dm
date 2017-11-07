FROM docker.dever.cc/os/alpine/v3.4:latest

MAINTAINER Rabin "https://github.com/shemic"

USER root
RUN apk add --no-cache --update bash mysql mysql-client && \
	mkdir /run/mysqld && chmod 777 /run/mysqld && \
	rm -rf /var/lib/mysql && mkdir -p /var/lib/mysql && \
	chmod 664 /etc/mysql/my.cnf


RUN sed -Ei 's/^(bind-address|log|binlog)/#&/' /etc/mysql/my.cnf \
	#&& sed -Ei 's/^(#skip-networking)/skip-networking/' /etc/mysql/my.cnf \
	&& echo 'user=root' | awk '{ print } $1 == "[mysqld]" && c == 0 { c = 1; system("cat") }' /etc/mysql/my.cnf > /tmp/my.cnf \
	&& mv /tmp/my.cnf /etc/mysql/my.cnf \
	&& echo 'skip-host-cache' | awk '{ print } $1 == "[mysqld]" && c == 0 { c = 1; system("cat") }' /etc/mysql/my.cnf > /tmp/my.cnf \
	&& mv /tmp/my.cnf /etc/mysql/my.cnf \
	&& echo 'skip-name-resolve' | awk '{ print } $1 == "[mysqld]" && c == 0 { c = 1; system("cat") }' /etc/mysql/my.cnf > /tmp/my.cnf \
	&& mv /tmp/my.cnf /etc/mysql/my.cnf

VOLUME ["/var/lib/mysql", "/etc/mysql"]

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 3306
CMD ["mysqld"]