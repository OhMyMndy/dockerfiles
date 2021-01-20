ARG UBUNTU20_04
FROM ohmymndy/ubuntu-x11:$UBUNTU20_04
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root

RUN install-package \
    xdg-utils \
    curl \
  && apt-get clean -y

# hadolint ignore=SC1001
RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive \
	curl -sSL "$(curl -sSL https://www.nomachine.com/download/download\&id\=2 2>/dev/null | grep -E -o "http.*download.*deb")" >> "/tmp/nomachine.deb" \
	&& dpkg -i "/tmp/nomachine.deb" \
  && rm /tmp/nomachine.deb
  

COPY nomachine/root/ /

USER $USER
RUN mkdir -p "$HOME/.nx"
RUN mkdir -p "$HOME/NoMachine"
VOLUME $HOME/.nx
VOLUME $HOME/NoMachine

USER root

CMD s6-setuidgid $USER /usr/NX/bin/nxplayer
