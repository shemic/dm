
FROM docker.dever.cc/os/ubuntu:latest
SHELL ["/bin/bash", "-c"]
ENV NVM_DIR=/usr/local/nvm
ENV PATH=$NVM_DIR/versions/node/current/bin:$PATH

RUN apt-get update && apt-get install -y \
    curl \
    bash \
    gosu \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p $NVM_DIR \
    && curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash \
    && source $NVM_DIR/nvm.sh \
    && nvm install --lts \
    && nvm alias default lts/* \
    && nvm use default \
    && NODE_PATH=$(nvm which current | xargs dirname | xargs dirname) \
    && ln -sfn $NODE_PATH $NVM_DIR/versions/node/current \
    && node -v \
    && npm -v
RUN npm config set registry https://registry.npmmirror.com
RUN npm install -g @qingchencloud/openclaw-zh@latest --registry=https://registry.npmmirror.com
#RUN openclaw config set auth.openai.baseURL http://ai-am:8045/v1
#RUN openclaw config set auth.openai.apiKey shemic
#RUN openclaw config set agents.defaults.model openai/gemini-2.5-flash
WORKDIR /root

EXPOSE 18789