
FROM alpine
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/ash", "-o", "pipefail", "-c" ]

ARG USER=user

ENV SHELL=/bin/bash
ENV USER=$USER
ENV HOME=/home/$USER
ENV PATH=$PATH:$HOME/.local/bin


ARG OVERLAY_VERSION="v1.22.1.0"
ARG OVERLAY_ARCH="amd64"


ADD https://github.com/just-containers/s6-overlay/releases/download/${OVERLAY_VERSION}/s6-overlay-${OVERLAY_ARCH}.tar.gz /tmp/

RUN apk add --no-cache tar
RUN tar xzf /tmp/s6-overlay-${OVERLAY_ARCH}.tar.gz -C / --exclude="./bin" && \
    tar xzf /tmp/s6-overlay-${OVERLAY_ARCH}.tar.gz -C /usr ./bin

# COPY root/ /
# COPY bin/* /bin

RUN adduser -S -h "$HOME" "$USER" \
	&& addgroup -S sudo \
	&& addgroup -S "$USER" \
	&& mkdir -p "$HOME"/{.ssh,.config,.local/share} \
	&& chown -R "$USER":"$USER" "$HOME" \
	&& adduser "$USER" audio \
	&& adduser "$USER" video \
	&& adduser "$USER" root \
	&& adduser "$USER" sudo \
	&& adduser "$USER" "$USER"


# VOLUME $HOME/.ssh
WORKDIR $HOME


#  ca-certificates libnss3-tools
RUN apk add --no-cache sudo less file vim iputils git



ENTRYPOINT [ "/init" ]
