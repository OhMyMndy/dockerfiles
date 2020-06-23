FROM linuxserver/code-server
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]


USER root


ARG OVERLAY_VERSION="v1.22.1.0"
ARG OVERLAY_ARCH="amd64"

ENV SHELL=bash
ENV HOME=/config
ENV USER=abc

RUN curl -sSL https://deb.nodesource.com/setup_12.x | sudo -E bash - >/dev/null
RUN apt-get update -qq && apt-get install -y -qq \
	curl \
	readline-common \
    nodejs \
    rsync \
    python3-pip \
    git \
    openssh-client \
	&& rm -rf /var/lib/apt/lists/*
RUN npm install -g --silent json >/dev/null


RUN curl -LO https://github.com/BurntSushi/ripgrep/releases/download/11.0.2/ripgrep_11.0.2_amd64.deb && dpkg -i ripgrep_11.0.2_amd64.deb && rm ripgrep_11.0.2_amd64.deb


RUN docker_url=https://download.docker.com/linux/static/stable/x86_64; \
    docker_version="19.03.8"; \
    curl -fsSL $docker_url/docker-$docker_version.tgz | \
    tar zxvf - --strip 1 -C /usr/bin docker/docker


RUN apt-get update -qq && apt-get install -y -qq \
	curl \
	readline-common \
    nodejs \
    rsync \
    python3-pip \
    git \
    openssh-client \
	&& rm -rf /var/lib/apt/lists/*

RUN chown $USER:$USER -R $HOME

USER $USER

RUN curl -LsS https://raw.githubusercontent.com/Mandy91/dotfiles/master/installers/apps/code.sh | bash -

RUN cd /tmp && git clone https://github.com/Mandy91/dotfiles.git && cd dotfiles && /tmp/dotfiles/installers/ubuntu.sh --dev --php && rm -rf /tmp/dotfiles

USER root
