ARG UBUNTU20_04
FROM ohmymndy/ubuntu-x11:$UBUNTU20_04
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root

RUN install-package spacefm --no-install-recommends

CMD s6-setuidgid $USER spacefm
