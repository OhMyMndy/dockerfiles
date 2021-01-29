ARG UBUNTU20_04
FROM ohmymndy/ubuntu:$UBUNTU20_04
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root
RUN install-package squid

EXPOSE 3128/tcp
COPY squid-cache/squid.conf /etc/squid/squid.conf
COPY squid-cache/entrypoint.sh /entrypoint

CMD "/entrypoint"