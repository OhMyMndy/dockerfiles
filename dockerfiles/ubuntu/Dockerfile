ARG UBUNTU_VERSION=non-existing
FROM ubuntu:$UBUNTU_VERSION as ubuntu
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

ARG UBUNTU_VERSION
ARG USER=user
ARG PUID=1000
ARG PGID=1000

ENV SHELL=/bin/bash
ENV USER=$USER
ENV UBUNTU_VERSION=$UBUNTU_VERSION
ENV HOME=/home/$USER
ENV PATH=$PATH:$HOME/.local/bin


ARG OVERLAY_VERSION="v1.22.1.0"
ARG OVERLAY_ARCH="amd64"

ADD https://github.com/just-containers/s6-overlay/releases/download/${OVERLAY_VERSION}/s6-overlay-${OVERLAY_ARCH}.tar.gz /tmp/

# hadolint ignore=SC2015
RUN [[ "$UBUNTU_VERSION" != '18.04' ]] && tar xzf /tmp/s6-overlay-${OVERLAY_ARCH}.tar.gz -C / --exclude="./bin" && \
    tar xzf /tmp/s6-overlay-${OVERLAY_ARCH}.tar.gz -C /usr ./bin || true

# hadolint ignore=SC2015
RUN [[ "$UBUNTU_VERSION" = '18.04' ]] && tar xzf /tmp/s6-overlay-${OVERLAY_ARCH}.tar.gz -C / || true

COPY shared/root/ /
COPY ubuntu/root/ /
COPY ubuntu/bin/* /bin/

# Test if s6 is working as expected
RUN test -f /init
RUN test -f /bin/execlineb

RUN groupadd -g 1000 "$USER" \
	&& useradd --create-home -u "$PUID" -g "$PGID" -s /bin/bash --home-dir "$HOME" "$USER" \
	&& mkdir -p "$HOME"/{.ssh,.config,.local/share} \
	&& chown -R "$USER":"$USER" "$HOME" \
	&& usermod -a -G sudo "$USER"

RUN mv "$HOME" "${HOME}_original"
RUN ln -sf "${HOME}_original" "$HOME"
RUN touch "$HOME/.initialized"

VOLUME $HOME/.ssh
WORKDIR $HOME


RUN --mount=type=cache,target=/var/cache/apt install-package --no-install-recommends readline-common sudo less file cron vim-tiny iputils-ping

# RUN apt-get update \
# 	&& add-apt-repository ppa:git-core/ppa \
# 	&& apt-get update \
# 	&& DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends git -y \
# 	&& apt-get clean -y \
# 	&& rm -rf /tmp/*


ENTRYPOINT ["/init"]


FROM ubuntu as ubuntu



FROM ubuntu as ubuntu-x11

RUN --mount=type=cache,target=/var/cache/apt install-package \
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
	gtk2-engines-pixbuf \
	yaru-theme-gtk \
	yaru-theme-icon \
	zsh fzf htop tmux \
	--no-install-recommends
	
RUN usermod -aG audio,video "$USER"

COPY ubuntu-x11/root/ /



FROM ubuntu-x11 as ubuntu-x11-hw

USER root

RUN --mount=type=cache,target=/var/cache/apt install-package \
	xinput \
	usbutils \
	libxcb-xinput0 \
	xserver-xorg-video-intel \
	i965-va-driver \
	xserver-xorg-video-ati \
	libgl1-mesa-dri \
	libgl1-mesa-glx \
	xterm \
	xorg \
	compton \
   --no-install-recommends
  
RUN usermod -aG audio,video,render,input "$USER"

FROM ubuntu-x11-hw as wine5

USER root
RUN mkdir -p "$HOME"/{.wine,.wine64} \
	&& chown -R "$USER":"$USER" "$HOME"

RUN --mount=type=cache,target=/var/cache/apt install-package curl gnupg


RUN dpkg --add-architecture i386 \
	&& curl -LsS https://dl.winehq.org/wine-builds/winehq.key -o /tmp/winehq.key \
	&& apt-key add /tmp/winehq.key \
	&& rm /tmp/winehq.key

RUN add-apt-repository -y 'deb https://dl.winehq.org/wine-builds/ubuntu/ focal main'


RUN --mount=type=cache,target=/var/cache/apt install-package --install-recommends winehq-stable -o APT::Immediate-Configure=false

RUN --mount=type=cache,target=/var/cache/apt install-package winetricks winbind
RUN --mount=type=cache,target=/var/cache/apt install-package --no-install-recommends zenity 

RUN mkdir -p "/run/user/1000/$USER" \
	&& chown "$USER":"$USER" -R "/run/user/1000/$USER" \
	&& chmod 700 -R "/run/user/1000/$USER"


USER $USER

VOLUME $HOME/.wine64
VOLUME $HOME/.wine

USER root
CMD s6-setuidgid $USER wine



FROM ubuntu-x11-hw as firefox



RUN mkdir -p $HOME/{Downloads,.mozilla,.ssh} \
    && chown -R $USER:$USER $HOME

RUN --mount=type=cache,target=/var/cache/apt install-package --no-install-recommends ffmpeg firefox

RUN echo 'pref("browser.tabs.remote.autostart", false);' >> /etc/firefox/syspref.js
RUN echo 'pref("security.enterprise_roots.enabled", true);' >> /etc/firefox/syspref.js


USER $USER

VOLUME $USER/.mozilla

USER root

CMD s6-setuidgid $USER firefox


FROM ubuntu-x11-hw as nomachine


RUN --mount=type=cache,target=/var/cache/apt install-package \
    xdg-utils \
    curl \
  && apt-get clean -y

# hadolint ignore=SC1001
RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive \
	curl -sSL "$(curl -sSL https://www.nomachine.com/download/download\&id=4 2>/dev/null | grep -E -o "http.*download.*deb")" > "/tmp/nomachine.deb" \
	&& dpkg -i "/tmp/nomachine.deb" \
  && rm /tmp/nomachine.deb
  

COPY nomachine/root/ /

USER $USER
RUN mkdir -p "$HOME/.nx"
RUN mkdir -p "$HOME/NoMachine"
VOLUME $HOME/.nx
VOLUME $HOME/NoMachine

USER root

CMD s6-setuidgid $USER /usr/NX/bin/nxplayer

FROM ubuntu-x11-hw as dosbox
USER root
RUN --mount=type=cache,target=/var/cache/apt install-package dosbox

USER $USER
RUN mkdir -p "$HOME/.config/dosbox"
VOLUME $HOME/.config/dosbox

USER root

CMD s6-setuidgid $USER dosbox



FROM ubuntu-x11-hw as novnc

RUN rm -f /etc/apt/apt.conf.d/docker-clean
RUN --mount=type=cache,target=/var/cache/apt install-package --no-install-recommends \
    net-tools \
    novnc \
    supervisor \
    xterm \
    x11-utils \
    x11-xserver-utils \
    eterm \
    'tigervnc*' \
    # fluxbox \
	xfwm4 xfce4-panel xfdesktop4 xfce4-terminal xfce4-settings \
	curl

ENV DISPLAY=:0.0
ENV DISPLAY_WIDTH=1024
ENV DISPLAY_HEIGHT=768


ADD ./novnc/etc/novnc/supervisor /etc/supervisor
ADD ./novnc/etc/vncstartup.sh /vncstartup.sh
ADD ./novnc/root/ /

RUN cp -f /usr/share/novnc/vnc.html /usr/share/novnc/index.html

EXPOSE 8080


FROM novnc as novnc-docker


RUN --mount=type=cache,target=/var/cache/apt install-package btrfs-progs e2fsprogs iptables openssl xfsprogs xz-utils pigz
RUN curl -SsL https://get.docker.com | bash -
RUN curl -SsL https://raw.githubusercontent.com/moby/moby/master/hack/dind > /bin/dind && chmod +x /bin/dind
RUN curl -L "https://github.com/docker/compose/releases/download/1.28.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose


RUN usermod -aG docker $USER
ADD ./novnc-docker/root/ /

FROM novnc-docker as pycharm

RUN --mount=type=cache,target=/var/cache/apt install-package --no-install-recommends git tig vim

RUN curl -SsL https://download.jetbrains.com/python/pycharm-community-2020.3.3.tar.gz -o /tmp/pycharm.tgz \
  && mkdir -p /opt/pycharm && tar -xzf /tmp/pycharm.tgz -C /opt/pycharm --strip-components=1 && rm -rf /tmp/** \
  && test -f /opt/pycharm/bin/pycharm.sh \
  && test -x /opt/pycharm/bin/pycharm.sh

ADD ./pycharm/root/ /


FROM novnc-docker as code

RUN --mount=type=cache,target=/var/cache/apt install-package --no-install-recommends git tig


RUN curl -LsS -o /tmp/vscode.deb https://go.microsoft.com/fwlink/?LinkID=760868 \
	&& dpkg -i /tmp/vscode.deb \
	; apt-get update -y \
	&& DEBIAN_FRONTEND=noninteractive apt-get install -y -f --no-install-recommends \
	&& rm /tmp/vscode.deb \
	&& rm -rf /tmp/*

RUN --mount=type=cache,target=/var/cache/apt install-package gpg-agent \
	libx11-xcb1 \
	libxtst6 \
	libasound2

RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && usermod -aG sudo $USER && passwd -d $USER

ADD ./code/root/ /



FROM ubuntu as audiotools

RUN --mount=type=cache,target=/var/cache/apt install-package audiotools # ffmpeg

# ENTRYPOINT [ "" ]




FROM novnc as vivaldi-novnc



RUN mkdir -p $HOME/.cache/vivaldi \
	&& mkdir -p $HOME/.config/vivaldi \
    && chown -R $USER:$USER $HOME

RUN --mount=type=cache,target=/var/cache/apt install-deb-from-url https://downloads.vivaldi.com/stable/vivaldi-stable_3.6.2165.40-1_amd64.deb
USER $USER

VOLUME $USER/.cache/vivaldi
VOLUME $USER/.config/vivaldi


USER root

ADD ./vivaldi-novnc/root/ /




FROM novnc-docker as phpstorm

RUN --mount=type=cache,target=/var/cache/apt install-package --no-install-recommends git tig vim

RUN --mount=type=cache,target=/tmp curl -SsL https://download-cf.jetbrains.com/webide/PhpStorm-2020.3.2.tar.gz -o /tmp/phpstorm.tgz \
  && mkdir -p /opt/phpstorm && tar -xzf /tmp/phpstorm.tgz -C /opt/phpstorm --strip-components=1 && rm -rf /tmp/** \
  && test -f /opt/phpstorm/bin/phpstorm.sh \
  && test -x /opt/phpstorm/bin/phpstorm.sh

ADD ./phpstorm/root/ /

RUN mkdir -p $HOME/.cache/vivaldi \
	&& mkdir -p $HOME/.config/vivaldi \
    && chown -R $USER:$USER $HOME

RUN --mount=type=cache,target=/var/cache/apt install-deb-from-url https://downloads.vivaldi.com/stable/vivaldi-stable_3.6.2165.40-1_amd64.deb
USER $USER

VOLUME $USER/.cache/vivaldi
VOLUME $USER/.config/vivaldi

USER root