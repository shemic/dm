FROM anapsix/alpine-java
RUN apk add --update &&  apk add git && \
    git clone https://github.com/KOHGYLW/kiftd.git /kiftd && mkdir /data && \
    echo "cd /kiftd && java -jar kiftd-1.0.6-RELEASE.jar -start" > /start.sh && \
    chmod +x /start.sh
    
EXPOSE 9000
VOLUME ["/kiftd/conf","/data"]
CMD ["/start.sh"]