ARG UBUNTU19_10
FROM registry.mandy-home.duckdns.org/mandy91/ubuntu:$UBUNTU19_10
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root
RUN install-package --no-install-recommends vinagre

CMD s6-setuidgid $USER vinagre