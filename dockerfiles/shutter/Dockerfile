ARG UBUNTU19_10
FROM registry.mandy-home.duckdns.org/mandy91/ubuntu-x11:$UBUNTU19_10
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root
RUN add-apt-repository ppa:linuxuprising/shutter \
  && package-install shutter --no-install-recommends

USER "$USER"
RUN mkdir -p ~/{.shutter,Pictures}

VOLUME [ "$HOME/.shutter" ]

USER root
CMD s6-setuidgid $USER shutter
