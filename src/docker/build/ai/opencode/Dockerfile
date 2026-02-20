
FROM docker.dever.cc/os/ubuntu:latest

RUN apt-get update && apt-get install -y \
    npm \
    curl \
    bash \
    gosu \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN npm i -g opencode-ai

WORKDIR /app

COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

EXPOSE 4096

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

CMD ["serve"]