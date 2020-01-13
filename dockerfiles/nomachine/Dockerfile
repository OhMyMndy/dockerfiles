ARG UBUNTU19_10
FROM mandy91/ubuntu:$UBUNTU19_10
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root

RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive \
  apt-get install -y --no-install-recommends \
    fonts-noto \
    fonts-lato \
    xdg-utils \
    libpulse0 \
  && apt-get clean -y

RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive \
	curl -sSL "$(curl -sSL https://www.nomachine.com/download/download\&id\=6 2>/dev/null | grep -E -o "http.*download.*deb")" >> "/tmp/nomachine.deb" \
	&& dpkg -i "/tmp/nomachine.deb" \
  && rm /tmp/nomachine.deb
  

COPY root/ /

USER $USER
RUN mkdir "$HOME/.nx"
RUN mkdir "$HOME/NoMachine"
VOLUME $HOME/.nx
VOLUME $HOME/NoMachine

USER root

ENTRYPOINT "/init"  s6-setuidgid $USER /usr/NX/bin/nxplayer
