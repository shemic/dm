FROM docker.shemic.com/os/alpine/glibc:latest

MAINTAINER Rabin "https://github.com/shemic"

WORKDIR /root

# set environment variable
ENV JAVA_HOME=/share/lib/jdk
ENV PATH=${PATH}:${JAVA_HOME}/bin:${JAVA_HOME}/sbin

COPY ssh_config /root/.ssh/config

# intall ssh... [del bash-completion]
RUN apk add --no-cache --update openssh rsync procps bash ncurses curl && \
	ssh-keygen -t rsa -f /root/.ssh/id_rsa -P '' && \
    cat /root/.ssh/id_rsa.pub >> /root/.ssh/authorized_keys && \
	ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -P '' && \
	ssh-keygen -t rsa -f /etc/ssh/ssh_host_dsa_key -P '' && \
	ssh-keygen -t rsa -f /etc/ssh/ssh_host_ecdsa_key -P '' && \
	ssh-keygen -t rsa -f /etc/ssh/ssh_host_ed25519_key -P '' && \
	chmod -R 600 /root/.ssh/*

COPY init.sh /entrypoint/init.sh