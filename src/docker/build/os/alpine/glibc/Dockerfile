FROM docker.dever.cc/os/alpine:latest

MAINTAINER Rabin "https://github.com/shemic"

#curl -Ls

ENV GLIB_VERSION 2.28-r0
RUN apk --no-cache add ca-certificates wget && \
	wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub && \
	wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIB_VERSION}/glibc-${GLIB_VERSION}.apk && \
	wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIB_VERSION}/glibc-i18n-${GLIB_VERSION}.apk && \
	apk add glibc-${GLIB_VERSION}.apk glibc-i18n-${GLIB_VERSION}.apk && \
	apk del wget ca-certificates && \
    rm -rf /tmp/* /var/cache/apk/*