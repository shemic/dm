FROM docker.dever.cc/dev/python:latest

MAINTAINER Rabin "https://github.com/shemic"

# Add gecko driver
ENV GECKODRIVER_VERSION=0.15.0
ENV GECKODRIVER_FILE=v${GECKODRIVER_VERSION}/geckodriver-v${GECKODRIVER_VERSION}-linux64.tar.gz

RUN apk add --no-cache bash curl dbus firefox-esr fontconfig ttf-freefont xvfb && \
    pip install pyvirtualdisplay && \
    pip install selenium && \
    curl -s -o /tmp/geckodriver.tar.gz -L https://github.com/mozilla/geckodriver/releases/download/$GECKODRIVER_FILE && \
    rm -rf /usr/bin/geckodriver && \
    tar -C /usr/bin -zxf /tmp/geckodriver.tar.gz && \
    rm /tmp/geckodriver.tar.gz && \
    mv /usr/bin/geckodriver /usr/bin/geckodriver-$GECKODRIVER_VERSION && \
    chmod 755 /usr/bin/geckodriver-$GECKODRIVER_VERSION && \
    ln -fs /usr/bin/geckodriver-$GECKODRIVER_VERSION /usr/bin/geckodriver && \
    apk del curl