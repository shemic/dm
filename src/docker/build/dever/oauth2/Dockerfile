FROM docker.dever.cc/os/alpine:latest

MAINTAINER Rabin "https://github.com/shemic"

RUN apk add --no-cache --update go g++ git && \
	git clone http://git.dever.cc:3000/dever/oauth2.git /root/oauth2 && \
	chmod +x /root/oauth2/core.go && \
	chmod +x /root/oauth2/start.sh && \
	cd /root/oauth2/ && \
	go get gopkg.in/mgo.v2 && \
	go get github.com/gin-contrib/sessions && \
	go get github.com/gin-gonic/gin && \
	go build core.go && \
	chmod +x /root/oauth2/core && \
	apk del go g++ && \
	rm -rf /root/go

COPY oauth2.sh /entrypoint/oauth2.sh