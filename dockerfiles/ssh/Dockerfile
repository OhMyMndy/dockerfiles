ARG UBUNTU19_10
FROM ohmymndy/ubuntu:$UBUNTU19_10
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root
RUN install-package readline-common rsync openssh-client ssh-askpass

