ARG UBUNTU19_10
FROM ohmymndy/ubuntu:$UBUNTU19_10
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root
RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends nload dnsutils traceroute iputils-ping mtr \
  && apt-get clean -y


USER $USER
