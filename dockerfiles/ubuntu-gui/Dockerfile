ARG UBUNTU19_10
FROM mandy91/ubuntu:$UBUNTU19_10
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root

# Install Chrome
RUN apt-get update && apt-get install -y \
	hicolor-icon-theme \
	adwaita-qt \
	adwaita-icon-theme \
	gnome-themes-standard \
	libcanberra-gtk* \
	libgl1-mesa-dri \
	libgl1-mesa-glx \
	libpango1.0-0 \
	libv4l-0 \
	fonts-symbola \
	--no-install-recommends \
	&& rm -rf /var/lib/apt/lists/*


COPY root/ /