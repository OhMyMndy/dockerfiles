ARG DOCKER_IMAGE_VERSION
FROM ohmymndy/nomachine:$DOCKER_IMAGE_VERSION
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

# WIP!

USER root

RUN install-package i3 libperl5.28 vim

EXPOSE 4000

RUN /usr/NX/scripts/setup/nxserver --install debian
RUN /usr/NX/scripts/setup/nxnode --install debian
CMD s6-setuidgid $USER /usr/NX/bin/nxserver.bin