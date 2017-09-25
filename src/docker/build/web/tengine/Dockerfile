FROM centos:latest
MAINTAINER MAINTAINER The Condenast Web Server <liang.cheng@condenast.com.cn>

# install main packages:
RUN yum -y install wget openssl-devel gcc gcc-c++ make pcre-devel pcre; yum clean all
RUN cd /root \
&& wget http://tengine.taobao.org/download/tengine-2.1.2.tar.gz \
&& tar xzf tengine-2.1.2.tar.gz \
&& cd /root/tengine-2.1.2 \
&& ./configure --prefix=/etc/nginx/ --sbin-path=/usr/sbin/nginx --conf-path=/etc/nginx/nginx.conf --pid-path=/tmp/nginx.pid --lock-path=/tmp/nginx.lock --user=nginx --group=nginx --with-poll_module --with-http_realip_module --with-http_sub_module --with-http_ssl_module --with-http_flv_module --with-http_mp4_module --with-http_stub_status_module --with-http_gzip_static_module --with-http_concat_module \
&& make \
&& make install \
&& rm -rf /root/tengine*

# copy cfg files:
ADD ./conf/nginx/nginx.conf /etc/nginx/nginx.conf

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai  /etc/localtime \
&& chmod +x /etc/rc.d/rc.local

EXPOSE 80
CMD ["/usr/sbin/nginx","-c","/etc/nginx/nginx.conf"]