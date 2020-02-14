ARG UBUNTU19_10
FROM mandy91/ubuntu-x11:$UBUNTU19_10
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root

RUN install-package spacefm --no-install-recommends

CMD s6-setuidgid $USER spacefm
