FROM jess/chrome:latest
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root
RUN mkdir -p /data; chown chrome:chrome -R /data
USER chrome
VOLUME /data