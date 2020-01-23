ARG UBUNTU19_10
FROM mandy91/ubuntu-gui:$UBUNTU19_10
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root

# Install Chrome
RUN apt-get update && apt-get install -y \
	spacefm \
	--no-install-recommends \
	&& rm -rf /var/lib/apt/lists/*

CMD s6-setuidgid $USER spacefm
