ARG UBUNTU20_04
FROM ohmymndy/ubuntu:$UBUNTU20_04
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root
RUN install-package readline-common rsync openssh-client ssh-askpass

