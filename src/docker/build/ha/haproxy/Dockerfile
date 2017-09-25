FROM docker.shemic.com/os/alpine/v3.4:latest

MAINTAINER Rabin "https://github.com/shemic"

RUN apk add --no-cache --update nginx

COPY nginx.sh /entrypoint/nginx.sh

VOLUME ["/www", "/etc/nginx", "/var/log/nginx"]

EXPOSE 80
EXPOSE 443

CMD ["nginx"]