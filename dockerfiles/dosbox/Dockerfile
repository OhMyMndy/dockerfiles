ARG UBUNTU19_10
FROM mandy91/ubuntu-gaming:$UBUNTU19_10
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root
RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive \
  apt-get install -y \
   dosbox \
	&& apt-get clean -y


USER $USER
RUN mkdir -p "$HOME/.config/dosbox"
VOLUME $HOME/.config/dosbox

ENTRYPOINT [ "dosbox" ]