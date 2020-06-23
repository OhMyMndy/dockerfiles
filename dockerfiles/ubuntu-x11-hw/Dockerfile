ARG VERSION
ARG DOCKER_IMAGE_VERSION
FROM ohmymndy/ubuntu-x11:${DOCKER_IMAGE_VERSION}-$VERSION
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root

RUN install-package \
   xinput \
   usbutils \
   libxcb-xinput0 \
   xserver-xorg-video-intel \
   i965-va-driver \
	xserver-xorg-video-ati \
   libgl1-mesa-dri \
	libgl1-mesa-glx \
   xterm \
   --no-install-recommends
  

RUN usermod -aG audio,video,root,input "$USER"
