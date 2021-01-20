ARG UBUNTU20_04
FROM ohmymndy/ubuntu:$UBUNTU20_04
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root
RUN install-package --no-install-recommends vpnc openvpn ufw openssh-client

COPY /vpn/scripts/* /usr/local/bin/
RUN echo "$USER ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers.d/all
RUN passwd -d "$USER"

VOLUME /etc/openvpn

ENTRYPOINT [ "/init" ]
