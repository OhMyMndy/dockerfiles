ARG UBUNTU19_10
FROM mandy91/ubuntu:$UBUNTU19_10
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root
RUN install-package squid

EXPOSE 3128/tcp
COPY squid.conf /etc/squid/squid.conf
COPY entrypoint.sh /entrypoint

CMD "/entrypoint"