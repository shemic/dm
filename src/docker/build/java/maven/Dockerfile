FROM docker.dever.cc/java/base:latest

MAINTAINER Rabin "https://github.com/shemic"

ENV MAVEN_HOME=/usr/local/mvn \
	MAVEN_VERSION=3.5.2
ENV PATH=$PATH:$MAVEN_HOME/bin

RUN curl -O ${MIRRORS}apache/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz && \
	tar -zxvf apache-maven-$MAVEN_VERSION-bin.tar.gz && \
	rm apache-maven-$MAVEN_VERSION-bin.tar.gz && \
	mv apache-maven-$MAVEN_VERSION $MAVEN_HOME