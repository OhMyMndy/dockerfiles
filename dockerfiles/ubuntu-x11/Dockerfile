ARG VERSION
ARG DOCKER_IMAGE_VERSION
FROM mandy91/ubuntu-x11:${DOCKER_IMAGE_VERSION}-$VERSION
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

RUN install-package \
	hicolor-icon-theme \
	adwaita-qt \
	adwaita-icon-theme \
	gnome-themes-standard \
	libcanberra-gtk* \
	libgl1-mesa-dri \
	libgl1-mesa-glx \
	libpango1.0-0 \
	libv4l-0 \
	libpulse0 \
	libasound2 \
	apulse \
	fonts-noto-color-emoji \
	fonts-noto \
	fonts-lato \
	dbus-x11 \
	dbus \
	dconf \
	gtk2-engines-pixbuf \
	--no-install-recommends
	
COPY ubuntu-x11/root/ /