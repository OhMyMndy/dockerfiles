ARG UBUNTU19_10
FROM mandy91/ubuntu:$UBUNTU19_10
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root

RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive \
  apt-get install -y \
   xinput \
   usbutils \
   libxcb-xinput0 \
   xserver-xorg-video-intel \
	 xserver-xorg-video-ati \
   libgl1-mesa-dri \
	 libgl1-mesa-glx \
  && apt-get clean -y
  

RUN usermod -aG audio,video,root,input "$USER"

USER $USER