FROM docker.dever.cc/office/pdf2htmlex:latest

MAINTAINER Rabin "https://github.com/shemic"

RUN apk update && apk add --no-cache libreoffice font-adobe-100dpi git && \
	cd /usr/share/fonts && \
	git clone http://git.dever.cc:3000/rabin/fonts.git win && \
	cd win && \
	chmod -Rf 755 * && \
	mkfontscale && mkfontdir && fc-cache –fv