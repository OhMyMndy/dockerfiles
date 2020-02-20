ARG UBUNTU19_10
FROM mandy91/ubuntu:$UBUNTU19_10
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root
RUN install-package --no-install-recommends vpnc openvpn ufw

COPY /vpn/scripts/* /usr/local/bin/
RUN echo "$USER ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers.d/all
RUN passwd -d "$USER"

VOLUME /etc/openvpn

ENTRYPOINT [ "/init" ]
