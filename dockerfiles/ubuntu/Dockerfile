ARG VERSION=non-existing
FROM ubuntu:$VERSION
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

ARG USER=user

ENV SHELL=/bin/bash
ENV USER=$USER
ENV HOME=/home/$USER
ENV PATH=$PATH:$HOME/.local/bin

WORKDIR $HOME

RUN useradd --create-home --home-dir $HOME "$USER" \
	&& mkdir -p "$HOME"/{.ssh,.config,.local/share} \
	&& chown -R "$USER":"$USER" "$HOME" \
	&& usermod -a -G audio,video,root,sudo "$USER"


VOLUME $HOME/.ssh

RUN apt-get update \
	&& DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y iproute2 wget curl less file software-properties-common vim git readline-common sudo openssh-client ssh-askpass \
	&& apt-get clean -y


USER $USER