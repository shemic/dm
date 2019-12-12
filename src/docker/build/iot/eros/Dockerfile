FROM docker.dever.cc/dev/python/v3:latest

MAINTAINER Rabin "https://github.com/shemic"

ENV IOT_FARM=1
ENV IOT_NAME=eros
ENV IOT_HOME=/usr/local/$IOT_NAME
ENV DEMETER_CONF=env
ENV PATH=$PATH:$IOT_HOME

ENV NG_DOMAIN="ngrok.dever.cc"
ENV NG_NAME=ngrok
ENV NG_HOME=/usr/local/$NG_NAME
ENV PATH=$PATH:$NG_HOME/bin

RUN apk add --no-cache --update py-psycopg2 git gcc g++ go git make openssl && \
	pip3 install --upgrade pip && \
	pip3 install tornado && \
	pip3 install pytest-runner && \
	pip3 install paho-mqtt && \
	pip3 install modbus-tk && \
	pip3 install influxdb && \
	pip3 install short_url && \
	pip3 install oss2 && \
	#pip3 install qrcode && \
	pip3 install -U git+http://git.dever.cc:3000/python/demeter.git && \
	git clone http://git.dever.cc:3000/xinnongbaohe/$IOT_NAME.git $IOT_HOME && \
	rm -R $IOT_HOME/runtime/postgresql && \
	chmod -R +x $IOT_HOME/*.py && \
	git clone https://github.com/inconshreveable/ngrok.git --depth=1 $NG_HOME
	#apk del gcc g++ git make

COPY ngrokroot.crt /usr/local/ngrok/assets/client/tls/ngrokroot.crt

RUN cd $NG_HOME && \
	GOOS=linux GOARCH=amd64 make release-client

EXPOSE 8090 8091

COPY iot.sh /entrypoint/iot.sh