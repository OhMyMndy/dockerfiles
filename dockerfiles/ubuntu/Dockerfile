ARG VERSION=non-existing
FROM ubuntu:$VERSION
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

ARG USER=user
ARG PUID=1000
ARG PGID=1000

ENV SHELL=/bin/bash
ENV USER=$USER
ENV HOME=/home/$USER
ENV PATH=$PATH:$HOME/.local/bin


ARG OVERLAY_VERSION="v1.22.1.0"
ARG OVERLAY_ARCH="amd64"

ADD https://github.com/just-containers/s6-overlay/releases/download/${OVERLAY_VERSION}/s6-overlay-${OVERLAY_ARCH}.tar.gz /tmp/

RUN tar xzf /tmp/s6-overlay-${OVERLAY_ARCH}.tar.gz -C / --exclude="./bin" && \
    tar xzf /tmp/s6-overlay-${OVERLAY_ARCH}.tar.gz -C /usr ./bin

COPY shared/root/ /
COPY ubuntu/root/ /
COPY ubuntu/bin/* /bin/

RUN groupadd -g 1000 "$USER" \
	&& useradd --create-home -u "$PUID" -g "$PGID" -s /bin/bash --home-dir "$HOME" "$USER" \
	&& mkdir -p "$HOME"/{.ssh,.config,.local/share} \
	&& chown -R "$USER":"$USER" "$HOME" \
	&& usermod -a -G audio,video,root,sudo "$USER"


VOLUME $HOME/.ssh
WORKDIR $HOME


RUN install-package --no-install-recommends readline-common sudo less file cron vim-tiny iputils-ping

# RUN apt-get update \
# 	&& add-apt-repository ppa:git-core/ppa \
# 	&& apt-get update \
# 	&& DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends git -y \
# 	&& apt-get clean -y \
# 	&& rm -rf /tmp/*


ENTRYPOINT ["/init"]
