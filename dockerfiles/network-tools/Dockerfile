ARG UBUNTU20_04
FROM ohmymndy/ubuntu:$UBUNTU20_04
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root
RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends nload dnsutils traceroute iputils-ping mtr \
  && apt-get clean -y


USER $USER
