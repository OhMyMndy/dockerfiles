ARG UBUNTU19_10
FROM mandy91/ubuntu:$UBUNTU19_10
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

ENV VLC_PLUGIN_PATH=/usr/lib/x86_64-linux-gnu/vlc/plugins/

USER root
RUN apt-get update \
	&& DEBIAN_FRONTEND=noninteractive apt-get install -y vlc 'vlc-plugins*' --no-install-recommends \
	&& apt-get clean -y


USER $USER

ENTRYPOINT [ "vlc" ]