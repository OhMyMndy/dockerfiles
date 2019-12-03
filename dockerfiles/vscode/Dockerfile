ARG DOCKER_IMAGE_VERSION
FROM mandy91/dev:$DOCKER_IMAGE_VERSION
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root

RUN curl -L -o /tmp/vscode.deb https://go.microsoft.com/fwlink/?LinkID=760868 \
	&& dpkg -i /tmp/vscode.deb \
	; DEBIAN_FRONTEND=noninteractive apt-get install -y -f --no-install-recommends \
	&& rm /tmp/vscode.deb

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
	gpg-agent \
	libx11-xcb1 \
	libxtst6 \
	libasound2 \
	&& apt-get clean -y


USER $USER

ENTRYPOINT [ "/bin/bash", "-c", "code && while pgrep code &>/dev/null; do sleep 10; done" ]