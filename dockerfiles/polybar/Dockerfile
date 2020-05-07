ARG DOCKER_IMAGE_VERSION
FROM registry.mandy-home.duckdns.org/mandy91/archlinux:$DOCKER_IMAGE_VERSION
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

RUN pacman -S  --noconfirm base-devel \
    && yay -S --noconfirm --needed polybar \
    && pacman -R  --noconfirm base-devel



USER $USER