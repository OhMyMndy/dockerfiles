FROM ubuntu:noble

ARG DEBIAN_FRONTEND=noninteractive
ARG INSYNC_VERSION=3.2.7.10758
ENV INSYNC_VERSION=${INSYNC_VERSION}


RUN apt-get update && apt-get install -y --no-install-recommends \
  curl \
  apt-transport-https \
  ca-certificates \
  gnupg \
  cron \
  software-properties-common \
  && rm -rf /var/lib/apt/lists/*
RUN curl -L -o insync-headless.deb https://cdn.insynchq.com/builds/linux/${INSYNC_VERSION}/insync-headless_${INSYNC_VERSION}-buster_amd64.deb \
  && apt-get install ./insync-headless.deb -y

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]

USER ubuntu
