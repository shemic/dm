FROM docker.dever.cc/java/base:latest

MAINTAINER Rabin "https://github.com/shemic"

ENV SBT_HOME=/usr/local/sbt \
	SBT_VERSION=0.13.15
ENV PATH=$PATH:$SBT_HOME/bin

COPY repositories /root/repositories

RUN curl -O -L https://github.com/sbt/sbt/releases/download/v${SBT_VERSION}/sbt-${SBT_VERSION}.tgz && \
	tar -zxvf sbt-${SBT_VERSION}.tgz && \
	rm sbt-${SBT_VERSION}.tgz && \
	mv sbt ${SBT_HOME}

VOLUME ["/usr/local/sbt/conf"]