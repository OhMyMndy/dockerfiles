FROM ubuntu:19.10
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y vim git \
  && apt-get clean -y \
  && apt-get autoclean -y \
  && apt-get autoremove -y \
  && rm -rf /tmp/*
  

RUN groupadd -r vim -g 1000 && useradd -u 1000 -r -m -g vim vim && chown -R vim:vim /home/vim

USER vim
WORKDIR /home/vim
VOLUME /home/vim
ENTRYPOINT [ "vim" ]