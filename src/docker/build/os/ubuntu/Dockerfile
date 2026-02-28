FROM ubuntu:resolute-20260108

RUN sed -i 's@http://archive.ubuntu.com/ubuntu/@http://mirrors.tuna.tsinghua.edu.cn/ubuntu/@g' /etc/apt/sources.list.d/ubuntu.sources \
 && sed -i 's@http://security.ubuntu.com/ubuntu/@http://mirrors.tuna.tsinghua.edu.cn/ubuntu/@g' /etc/apt/sources.list.d/ubuntu.sources \
 && apt-get update -y \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    bash git tar vim-nox net-tools wget \
    --no-install-recommends \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mv /bin/sh /bin/sh-old && ln -s /bin/bash /bin/sh

VOLUME ["/share"]

COPY entrypoint.sh /entrypoint.sh
COPY process.sh /entrypoint/process.sh

RUN chmod +x /entrypoint.sh
RUN chmod +x /entrypoint/process.sh

#ENTRYPOINT ["/entrypoint.sh"]