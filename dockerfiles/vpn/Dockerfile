FROM ubuntu:18.04
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends vpnc openvpn readline-common openssh-client ssh-askpass ufw curl \
  && apt-get clean -y \
  && apt-get autoclean -y \
  && apt-get autoremove -y \
  && rm -rf /tmp/*
  
COPY ./scripts/* /usr/local/bin/

VOLUME /etc/openvpn