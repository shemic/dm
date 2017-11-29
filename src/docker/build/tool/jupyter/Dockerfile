FROM docker.dever.cc/learning:latest

MAINTAINER Rabin "https://github.com/shemic"

RUN apk update && apk add --no-cache gcc g++ curl make libzmq python-dev python3 python3-dev libxml2 libxml2-dev libxslt-dev libffi-dev openssl openssl-dev && \
	curl -O http://www.dever.cc/file/zeromq/zeromq-4.2.1.tar.gz && \
	tar -zxvf zeromq-4.2.1.tar.gz && \
	cd zeromq-4.2.1 && \
	./configure --prefix=/usr/local/zeromq && \
	make && make install && \
	cd .. && \
	rm -rf zeromq* && \
	pip2 install pyzmq --install-option="--zmq=/usr/local/zeromq" && \
	pip3 install pyzmq --install-option="--zmq=/usr/local/zeromq" && \
	#pip2 install ipython && \
	pip2 install jupyter && \
	pip3 install jupyter && \
	pip3 install -U ipykernel && \
	python2 -m ipykernel install --user && \
	python3 -m ipykernel install --user && \
	pip2 uninstall -y jupyter && \

	pip3 install jupyterlab && \
	pip3 install jupyter_contrib_nbextensions && \
	pip3 install jupyter_nbextensions_configurator && \
	pip3 install jupyter_dashboards && \
	pip3 install rise && \
	jupyter contrib nbextension install --user && \
	jupyter nbextensions_configurator enable --user && \
	jupyter dashboards quick-setup --sys-prefix && \
	jupyter-nbextension install rise --py --sys-prefix && \
	jupyter-nbextension enable rise --py --sys-prefix && \

	pip3 install incremental && \
	pip3 install scrapy && \
	pip3 install gevent && \
	apk del openssl-dev && apk add postgresql-dev && pip3 install psycopg2 && \
	pip3 install pymysql && \
	pip3 install prettytable && \

	#apk add jpeg-dev && pip3 install pyecharts && \
	#c kernel
	#pip3 install jupyter-c-kernel && install_c_kernel && \

	apk del curl gcc g++ make

COPY jupyter.sh /entrypoint/jupyter.sh