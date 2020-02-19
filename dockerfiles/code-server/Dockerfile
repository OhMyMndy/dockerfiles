FROM codercom/code-server:latest
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]


USER root


ARG OVERLAY_VERSION="v1.22.1.0"
ARG OVERLAY_ARCH="amd64"

ENV SHELL=bash
ENV HOME=/home/coder
ENV USER=coder

ADD https://github.com/just-containers/s6-overlay/releases/download/${OVERLAY_VERSION}/s6-overlay-${OVERLAY_ARCH}.tar.gz /tmp/

RUN tar xzf /tmp/s6-overlay-${OVERLAY_ARCH}.tar.gz -C /


RUN apt-get update && apt-get install -y \
	curl \
	readline-common \
    npm \
    rsync \
    python3-pip \
    git \
    openssh-client \
	&& rm -rf /var/lib/apt/lists/*
RUN npm install -g --silent json >/dev/null


RUN curl -LO https://github.com/BurntSushi/ripgrep/releases/download/11.0.2/ripgrep_11.0.2_amd64.deb && dpkg -i ripgrep_11.0.2_amd64.deb && rm ripgrep_11.0.2_amd64.deb


RUN docker_url=https://download.docker.com/linux/static/stable/x86_64; \
    docker_version="19.03.5"; \
    curl -fsSL $docker_url/docker-$docker_version.tgz | \
    tar zxvf - --strip 1 -C /usr/bin docker/docker

USER coder

RUN curl -LsS https://raw.githubusercontent.com/Mandy91/dotfiles/master/installers/apps/code.sh | bash -


USER root

ADD root/ /

ENTRYPOINT [ "/init" ]
CMD s6-setuidgid $USER code-server --host 0.0.0.0