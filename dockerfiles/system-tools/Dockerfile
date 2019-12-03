ARG UBUNTU19_10
FROM mandy91/ubuntu:$UBUNTU19_10
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y htop iotop glances nload nnn ack sed tree grep findutils curl wget rename \
  && apt-get clean -y
  

USER $USER