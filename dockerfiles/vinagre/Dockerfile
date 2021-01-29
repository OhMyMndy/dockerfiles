ARG UBUNTU20_04
FROM registry.mandy-home.duckdns.org/mandy91/ubuntu:$UBUNTU20_04
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root
RUN install-package --no-install-recommends vinagre

CMD s6-setuidgid $USER vinagre