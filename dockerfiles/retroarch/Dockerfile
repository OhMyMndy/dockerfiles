ARG DOCKER_IMAGE_VERSION
FROM mandy91/ubuntu-gaming:$DOCKER_IMAGE_VERSION
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root

RUN apt-get update \
  && add-apt-repository ppa:libretro/stable \
  && DEBIAN_FRONTEND=noninteractive \
  apt-get install -y \
   'retroarch*' \
   'libretro*' \
  && apt-get clean -y


RUN usermod -aG audio,video,root,input "$USER" \
  && mkdir -p "$HOME/.config/retroarch" \
  && chown -R "$USER":"$USER" "$HOME" 

USER $USER

VOLUME $USER/.config/retroarch

ENTRYPOINT [ "retroarch" ]