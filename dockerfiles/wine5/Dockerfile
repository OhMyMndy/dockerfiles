ARG UBUNTU19_10
FROM mandy91/ubuntu-x11-hw:$UBUNTU19_10
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root
RUN mkdir -p "$HOME"/{.wine,.wine64} \
	&& chown -R "$USER":"$USER" "$HOME"

RUN install-package curl gnupg


RUN dpkg --add-architecture i386 \
	&& curl -LsS https://dl.winehq.org/wine-builds/winehq.key -o /tmp/winehq.key \
	&& apt-key add /tmp/winehq.key \
	&& rm /tmp/winehq.key

RUN add-apt-repository -y 'deb https://dl.winehq.org/wine-builds/ubuntu/ eoan main'


RUN install-package --install-recommends winehq-stable

RUN install-package winetricks winbind
RUN install-package --no-install-recommends zenity 

RUN mkdir -p "/run/user/1000/$USER" \
	&& chown "$USER":"$USER" -R "/run/user/1000/$USER" \
	&& chmod 700 -R "/run/user/1000/$USER"


USER $USER

VOLUME $HOME/.wine64
VOLUME $HOME/.wine

USER root
CMD s6-setuidgid $USER wine
