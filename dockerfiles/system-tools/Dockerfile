ARG UBUNTU19_10
FROM mandy91/ubuntu:$UBUNTU19_10
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root
RUN install-package htop iotop glances nload nnn ack sed tree grep findutils curl wget rename

CMD s6-setuidgid $USER bash