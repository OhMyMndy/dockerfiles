ARG UBUNTU20_04
FROM ohmymndy/ubuntu-x11-hw:$UBUNTU20_04
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root

RUN mkdir -p /data && chown "$USER:$USER" /data


# Install Chrome
RUN install-package \
	curl \
	gnupg \
	libv4l-0 \
	&& install-deb-from-url https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb


USER $USER
VOLUME /data

USER root
CMD s6-setuidgid $USER google-chrome --user-data-dir=/data
