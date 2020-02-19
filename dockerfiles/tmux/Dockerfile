
FROM alpine:3
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/ash", "-o", "pipefail", "-c" ]

ARG USER=user

ENV SHELL=/bin/bash
ENV USER=$USER
ENV HOME=/home/$USER
ENV PATH=$PATH:$HOME/.local/bin


ARG OVERLAY_ARCH="amd64"

ENV S6_OVERLAY_RELEASE v1.22.1.0
ENV TMP_BUILD_DIR /tmp/build

ENV S6_OVERLAY_RELEASE v1.22.1.0
ENV TMP_BUILD_DIR /tmp/build

# Pull in the overlay binaries
ADD https://github.com/just-containers/s6-overlay/releases/download/${S6_OVERLAY_RELEASE}/s6-overlay-nobin.tar.gz ${TMP_BUILD_DIR}/
ADD https://github.com/just-containers/s6-overlay/releases/download/${S6_OVERLAY_RELEASE}/s6-overlay-nobin.tar.gz.sig ${TMP_BUILD_DIR}/


# Patch in source for testing sources...
# Update, install necessary packages, fixup permissions, delete junk
RUN apk add --update s6 s6-portable-utils s6 s6-linux-utils && \
    apk add --virtual verify gnupg && \
    chmod 700 ${TMP_BUILD_DIR} && \
    cd ${TMP_BUILD_DIR} && \
    apk del verify && \
    tar -C / -xzf s6-overlay-nobin.tar.gz && \
    cd / && \
    rm -rf /var/cache/apk/* && \
    rm -rf ${TMP_BUILD_DIR}


# hadolint ignore=SC2169
RUN adduser -S -s "$(command -v ash)" -h "$HOME" "$USER" \
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
RUN apk add --no-cache sudo less file vim iputils tmux

COPY root/ /


ENTRYPOINT [ "/init" ]
