FROM gitlab/gitlab-ce:latest
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

ARG USER=user
ARG PUID=1000
ARG PGID=1000

ENV SHELL=/bin/bash
ENV USER=$USER
ENV HOME=/home/$USER
ENV PATH=$PATH:$HOME/.local/bin

RUN groupadd -g 1000 "$USER" \
	&& useradd --create-home -u "$PUID" -g "$PGID" -s /bin/bash --home-dir "$HOME" "$USER" \
	&& mkdir -p "$HOME"/{.ssh,.config,.local/share} \
	&& chown -R "$USER":"$USER" "$HOME" \
	&& usermod -a -G audio,video,root,sudo "$USER"


ARG OVERLAY_VERSION="v1.22.1.0"
ARG OVERLAY_ARCH="amd64"

ADD https://github.com/just-containers/s6-overlay/releases/download/${OVERLAY_VERSION}/s6-overlay-${OVERLAY_ARCH}.tar.gz /tmp/

RUN tar xzf /tmp/s6-overlay-${OVERLAY_ARCH}.tar.gz -C / --exclude="./bin" && \
    tar xzf /tmp/s6-overlay-${OVERLAY_ARCH}.tar.gz -C /usr ./bin


COPY shared/root/ /

ENTRYPOINT [ "/init" ]
CMD s6-setuidgid $USER /assets/wrapper
