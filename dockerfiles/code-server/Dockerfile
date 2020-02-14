FROM theiaide/theia-full:next
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]


USER root


ARG OVERLAY_VERSION="v1.22.1.0"
ARG OVERLAY_ARCH="amd64"


ADD https://github.com/just-containers/s6-overlay/releases/download/${OVERLAY_VERSION}/s6-overlay-${OVERLAY_ARCH}.tar.gz /tmp/

RUN tar xzf /tmp/s6-overlay-${OVERLAY_ARCH}.tar.gz -C / --exclude="./bin" && \
    tar xzf /tmp/s6-overlay-${OVERLAY_ARCH}.tar.gz -C /usr ./bin


RUN apt-get update && apt-get install -y \
	curl \
	readline-common \
	--no-install-recommends \
	&& rm -rf /var/lib/apt/lists/*


RUN docker_url=https://download.docker.com/linux/static/stable/x86_64; \
    docker_version="19.03.5"; \
    curl -fsSL $docker_url/docker-$docker_version.tgz | \
    tar zxvf - --strip 1 -C /usr/bin docker/docker


ENV SHELL=bash