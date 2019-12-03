ARG UBUNTU19_10
FROM mandy91/ubuntu:$UBUNTU19_10
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root
RUN apt-get update \
	&& DEBIAN_FRONTEND=noninteractive apt-get install -y squid \
	&& apt-get clean -y

EXPOSE 3128/tcp
COPY squid.conf /etc/squid/squid.conf
COPY entrypoint.sh /entrypoint

ENTRYPOINT [ "/entrypoint" ]