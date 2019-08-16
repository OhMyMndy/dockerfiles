FROM ubuntu:18.04
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends nmap nload curl dnsutils traceroute iputils-ping \
  && apt-get clean -y \
  && apt-get autoclean -y \
  && apt-get autoremove -y \
  && rm -rf /tmp/*
  