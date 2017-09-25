FROM docker.shemic.com/os/alpine:latest

MAINTAINER Rabin "https://github.com/shemic"

ENV GLIB_VERSION 2.25-r0
RUN apk add --no-cache --update curl ca-certificates && \
	curl -Ls https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIB_VERSION}/glibc-${GLIB_VERSION}.apk > /tmp/glibc-${GLIB_VERSION}.apk && \
    apk add --allow-untrusted /tmp/glibc-${GLIB_VERSION}.apk && \
    apk del curl ca-certificates && \
    rm -rf /tmp/* /var/cache/apk/*