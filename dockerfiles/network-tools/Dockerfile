FROM ubuntu:18.04
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends nmap nload curl dnsutils traceroute iputils-ping mtr \
  && apt-get clean -y \
  && apt-get autoclean -y \
  && apt-get autoremove -y \
  && rm -rf /tmp/*
  

RUN groupadd -r network-tools -g 1000 && useradd -u 1000 -r -m -g network-tools network-tools && chown -R network-tools:network-tools /home/network-tools

USER network-tools
WORKDIR /home/network-tools
VOLUME /home/network-tools
