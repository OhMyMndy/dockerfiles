ARG UBUNTU20_04
FROM ohmymndy/ubuntu-x11-hw:$UBUNTU20_04
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

ENV VLC_PLUGIN_PATH=/usr/lib/x86_64-linux-gnu/vlc/plugins/

USER root
RUN install-package vlc 'vlc-plugins*' --no-install-recommends

CMD s6-setuidgid $USER vlc
