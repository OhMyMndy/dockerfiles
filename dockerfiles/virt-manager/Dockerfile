FROM ubuntu:18.04
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends virt-manager virt-viewer openssh-client ssh-askpass ssh-askpass-gnome readline-common \
  && apt-get clean -y \
  && apt-get autoclean -y \
  && apt-get autoremove -y \
  && rm -rf /tmp/*
  


RUN groupadd -r virt-manager -g 1000 && useradd -u 1000 -r -m -g virt-manager -G audio,video virt-manager && chown -R virt-manager:virt-manager /home/virt-manager

USER virt-manager
WORKDIR /home/virt-manager
VOLUME /home/virt-manager

ENTRYPOINT virt-manager