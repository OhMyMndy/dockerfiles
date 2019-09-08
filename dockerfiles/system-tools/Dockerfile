FROM ubuntu:18.04
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y htop iotop glances nload git vim nnn ack sed tree grep findutils curl wget less rename \
  && apt-get clean -y \
  && apt-get autoclean -y \
  && apt-get autoremove -y \
  && rm -rf /tmp/*
  

RUN groupadd -r system-tools -g 1000 && useradd -u 1000 -r -m -g system-tools system-tools && chown -R system-tools:system-tools /home/system-tools

USER system-tools
WORKDIR /home/system-tools
VOLUME /home/system-tools