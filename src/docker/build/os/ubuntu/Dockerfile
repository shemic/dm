FROM daocloud.io/library/ubuntu

MAINTAINER Rabin "https://github.com/shemic"

RUN sed -i "s/http:\/\/archive.ubuntu.com/http:\/\/mirrors.163.com/g" /etc/apt/sources.list && apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get -y install bash git tar vim-nox net-tools wget --no-install-recommends && apt-get clean  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mv /bin/sh /bin/sh-old && ln -s /bin/bash /bin/sh

VOLUME ["/share"]

COPY entrypoint.sh /entrypoint.sh
COPY process.sh /entrypoint/process.sh

RUN chmod +x /entrypoint.sh
RUN chmod +x /entrypoint/process.sh

#ENTRYPOINT ["/entrypoint.sh"]