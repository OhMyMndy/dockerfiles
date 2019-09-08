FROM ubuntu:18.04
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends vinagre \
  && apt-get clean -y \
  && apt-get autoclean -y \
  && apt-get autoremove -y \
  && rm -rf /tmp/*
  

RUN groupadd -r vinagre -g 1000 && useradd -u 1000 -r -m -g vinagre -G audio,video vinagre && chown -R vinagre:vinagre /home/vinagre

USER vinagre