ARG UBUNTU20_04
FROM ohmymndy/ubuntu-x11-hw:$UBUNTU20_04
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root
RUN install-package dosbox

USER $USER
RUN mkdir -p "$HOME/.config/dosbox"
VOLUME $HOME/.config/dosbox

USER root

CMD s6-setuidgid $USER dosbox