FROM debian

MAINTAINER Rabin "https://github.com/shemic"

#COPY sources.list /etc/apt/sources.list

RUN apt-get update && apt-get install -y locales && \
   localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8 && \
   apt-get clean && \
   rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV LANG en_US.utf8