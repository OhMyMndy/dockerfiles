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


RUN usermod -aG audio,video,root,input,plugdev "$USER" \
  && mkdir -p "$HOME/.config/retroarch" \
  && chown -R "$USER":"$USER" "$HOME" 

RUN usermod -aG plugdev,input "$USER" 
RUN echo "$USER ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers.d/all
RUN passwd -d "$USER"
COPY ./entrypoint.sh /entrypoint


USER $USER

VOLUME $USER/.config/retroarch

ENTRYPOINT [ "/entrypoint" ]
CMD [ "retroarch" ]