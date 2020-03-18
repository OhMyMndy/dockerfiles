ARG DOCKER_IMAGE_VERSION
FROM registry.mandy-home.duckdns.org/mandy91/wine:$DOCKER_IMAGE_VERSION
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root
RUN apt-get update \
  && apt-get install -y software-properties-common \
  && add-apt-repository ppa:lutris-team/lutris \
  && apt-get update \
  && apt-get install lutris libwxbase3.0-0v5 -y \
  && apt-get clean -y \
  && apt-get autoclean -y \
  && apt-get autoremove -y \
  && rm -rf /tmp/*

RUN apt-get update \
  && apt-get install -y software-properties-common \
  && add-apt-repository ppa:lutris-team/lutris \
  && apt-get update \
  # Dependencies for PCSX2
  && apt-get install libgtk2.0-0:i386 libwxbase3.0-0v5 libwxbase3.0-0v5:i386 libwxgtk3.0-0v5 libwxgtk3.0-0v5:i386 libaio1 libaio1:i386 -y \
  && apt-get clean -y \
  && apt-get autoclean -y \
  && apt-get autoremove -y \
  && rm -rf /tmp/*

RUN mkdir -p "$HOME/.local/share/lutris" \
  && chown "$USER":"$USER" -R "$HOME"
VOLUME $USER/.local/share/lutris

USER $USER

ENTRYPOINT [ "lutris" ]