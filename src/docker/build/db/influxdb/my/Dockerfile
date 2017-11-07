FROM docker.dever.cc/os/alpine:latest

MAINTAINER Rabin "https://github.com/shemic"

ENV $GOPATH=/usr/local/go
RUN apk add --no-cache --update git go openssl-dev && \
	go get github.com/influxdata/influxdb && \
	cd $GOPATH/src/github.com/influxdata/ && \
	go get ./... && \
	go install ./... && \
	apk del curl go

COPY influxdb.sh /entrypoint/influxdb.sh

CMD ["influxdb"]