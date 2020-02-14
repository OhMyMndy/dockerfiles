ARG UBUNTU19_10
FROM mandy91/ubuntu-x11:$UBUNTU19_10
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root

RUN curl -LsS -o /tmp/vscode.deb https://go.microsoft.com/fwlink/?LinkID=760868 \
	&& dpkg -i /tmp/vscode.deb \
	; apt-get update -y \
	&& DEBIAN_FRONTEND=noninteractive apt-get install -y -f --no-install-recommends \
	&& rm /tmp/vscode.deb \
	&& rm -rf /tmp/*

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
	gpg-agent \
	libx11-xcb1 \
	libxtst6 \
	libasound2 \
	&& rm -rf /tmp/*


USER $USER

RUN curl -LsS https://raw.githubusercontent.com/Mandy91/dotfiles/master/installers/apps/code.sh | bash -

RUN mv $HOME/.config/Code $HOME/.config/Code_original

USER root
COPY root/ /

CMD s6-setuidgid $USER /bin/bash -c "code && while pgrep code &>/dev/null; do sleep 10; done"