FROM ghcr.io/linuxserver/code-server:version-v3.8.0


# Docker and Docker-in-Docker
RUN curl -SsL https://get.docker.com | bash -
RUN curl -SsL https://raw.githubusercontent.com/moby/moby/master/hack/dind > /bin/dind && chmod +x /bin/dind
RUN mkdir -p /etc/services.d/dind && printf '#!/usr/bin/execlineb -P\ndind dockerd\n' >> /etc/services.d/dind/run && chmod +x /etc/services.d/dind/run
