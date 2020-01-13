ARG VERSION=non-existing
FROM ubuntu:$VERSION
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

ARG USER=user

ENV SHELL=/bin/bash
ENV USER=$USER
ENV HOME=/home/$USER
ENV PATH=$PATH:$HOME/.local/bin


ARG OVERLAY_VERSION="v1.22.1.0"
ARG OVERLAY_ARCH="amd64"

WORKDIR $HOME

ADD https://github.com/just-containers/s6-overlay/releases/download/${OVERLAY_VERSION}/s6-overlay-${OVERLAY_ARCH}.tar.gz /tmp/

RUN tar xzf /tmp/s6-overlay-${OVERLAY_ARCH}.tar.gz -C / --exclude="./bin" && \
    tar xzf /tmp/s6-overlay-${OVERLAY_ARCH}.tar.gz -C /usr ./bin


RUN useradd --create-home --home-dir "$HOME" "$USER" \
	&& mkdir -p "$HOME"/{.ssh,.config,.local/share} \
	&& chown -R "$USER":"$USER" "$HOME" \
	&& usermod -a -G audio,video,root,sudo "$USER"


VOLUME $HOME/.ssh

RUN apt-get update \
	&& DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y curl ca-certificates readline-common sudo \
	&& DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y iproute2 wget less file software-properties-common vim git openssh-client ssh-askpass htop cron cronic \
	&& apt-get clean -y \
	&& rm -rf /tmp/*


COPY root/ /
ENTRYPOINT ["/init"]
