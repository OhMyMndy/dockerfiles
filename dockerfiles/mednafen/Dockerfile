ARG UBUNTU19_10
FROM mandy91/ubuntu:$UBUNTU19_10
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root
RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y mednafen \
  && apt-get clean -y


RUN mkdir -p "$HOME"/{.ssh,.config,.mednafen} \
  && chown -R "$USER":"$USER" "$HOME"
  

USER mednafen
VOLUME /home/mednafen/.mednafen

ENTRYPOINT [ "/usr/games/mednafen" ]