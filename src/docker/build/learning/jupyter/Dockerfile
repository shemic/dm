FROM docker.dever.cc/learning:latest

MAINTAINER Rabin "https://github.com/shemic"

RUN apk update && apk add --no-cache gcc g++ curl make libzmq python-dev python3 python3-dev && \
	curl -O http://www.dever.cc/file/zeromq/zeromq-4.2.1.tar.gz && \
	tar -zxvf zeromq-4.2.1.tar.gz && \
	cd zeromq-4.2.1 && \
	./configure --prefix=/usr/local/zeromq && \
	make && make install && \
	cd .. && \
	rm -rf zeromq* && \
	pip2 install pyzmq --install-option="--zmq=/usr/local/zeromq" && \
	#pip2 install ipython && \
	pip2 install jupyter && \
	pip3 install pyzmq --install-option="--zmq=/usr/local/zeromq" && \
	pip3 install -U ipykernel && \
	python3 -m ipykernel install --user && \
	mkdir /usr/local/jupyter && \
	apk del curl gcc g++ make python-dev python3-dev

COPY jupyter.sh /entrypoint/jupyter.sh