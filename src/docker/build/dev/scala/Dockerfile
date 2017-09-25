FROM docker.shemic.com/dev/java:latest

MAINTAINER Rabin "https://github.com/shemic"

ARG SCALA_VERSION
ARG SCALA_HOME

ENV SCALA_VERSION=${SCALA_VERSION:-2.12.2}
ENV SCALA_HOME=${SCALA_HOME:-/opt/scala}
ENV PATH=${PATH}:${JAVA_HOME}/bin:${JAVA_HOME}/sbin:${SCALA_HOME}/bin

RUN java -version 2>&1 | grep version | sed -e 's/^openjdk version /JAVA_VERSION=/' > $JAVA_HOME/release

RUN apk add --no-cache --update curl && \ 
    curl -O https://downloads.lightbend.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz && \
    tar -xf scala-$SCALA_VERSION.tgz && \
    rm scala-$SCALA_VERSION.tgz && \
    mv scala-$SCALA_VERSION $SCALA_HOME && \
    apk del curl

ENTRYPOINT ["sh"]