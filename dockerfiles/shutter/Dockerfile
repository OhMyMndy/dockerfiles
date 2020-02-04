ARG UBUNTU19_10
FROM mandy91/ubuntu:$UBUNTU19_10
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root
RUN apt-get update \
  && apt-get install -y software-properties-common \
  && add-apt-repository ppa:linuxuprising/shutter \
  && apt-get update \
  && apt-get install shutter dbus-x11 gtk2-engines-pixbuf gnome-themes-standard -y --no-install-recommends \
  && rm -rf /tmp/*

USER "$USER"
RUN mkdir -p ~/.shutter

VOLUME [ "$HOME/.shutter" ]

USER root
CMD s6-setuidgid $USER shutter
