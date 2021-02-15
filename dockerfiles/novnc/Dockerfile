FROM ubuntu:20.04 as novnc

RUN rm -f /etc/apt/apt.conf.d/docker-clean
RUN --mount=type=cache,target=/var/cache/apt apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y -qq --no-install-recommends \
    bash \
    net-tools \
    novnc \
    supervisor \
    xterm \
    x11-utils \
    x11-xserver-utils \
    eterm \
    'tigervnc*' \
    fluxbox \
  && rm -rf /tmp/** rm -rf /var/lib/apt/lists/*



ARG OVERLAY_VERSION="v1.22.1.0"
ARG OVERLAY_ARCH="amd64"

ADD https://github.com/just-containers/s6-overlay/releases/download/${OVERLAY_VERSION}/s6-overlay-${OVERLAY_ARCH}.tar.gz /tmp/

# hadolint ignore=SC2015
RUN tar xzf /tmp/s6-overlay-${OVERLAY_ARCH}.tar.gz -C / --exclude="./bin" \
  && tar xzf /tmp/s6-overlay-${OVERLAY_ARCH}.tar.gz -C /usr ./bin || true

ENV HOME /home/novnc

ENV USER=novnc
ENV PUID=1000
ENV PGID=1000
RUN groupadd -g 1000 "$USER" \
	&& useradd --create-home -u "$PUID" -g "$PGID" -s /bin/bash --home-dir "$HOME" "$USER" \
	&& mkdir -p "$HOME"/{.ssh,.config,.local/share} \
	&& chown -R "$USER":"$USER" "$HOME" \
	&& usermod -a -G audio,video,root,sudo "$USER"



ENV LANG=en_US.UTF-8 \
  LANGUAGE=en_US.UTF-8 \
  LC_ALL=C.UTF-8 \
  DISPLAY=:0.0 \
  DISPLAY_WIDTH=1024 \
  DISPLAY_HEIGHT=768 \
  RUN_XTERM=yes \
  RUN_FLUXBOX=yes


ADD ./etc/novnc/supervisor /etc/supervisor
ADD ./etc/vncstartup.sh /vncstartup.sh
ADD ./etc/entrypoint.sh /entrypoint.sh

RUN chmod 777 -R /etc/supervisor
RUN touch /supervisord.log && chmod 777 /supervisord.log
RUN cp -f /usr/share/novnc/vnc.html /usr/share/novnc/index.html

CMD ["/entrypoint.sh"]
EXPOSE 8080



FROM novnc as phpstorm

RUN --mount=type=cache,target=/var/cache/apt apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y -qq --no-install-recommends curl \
  && rm -rf /tmp/** /var/lib/apt/lists/*

RUN --mount=type=cache,target=/tmp curl -SsL https://download-cf.jetbrains.com/webide/PhpStorm-2020.3.2.tar.gz -o /tmp/phpstorm.tgz \
  && mkdir -p /opt/phpstorm && tar -xzf /tmp/phpstorm.tgz -C /opt/phpstorm --strip-components=1 && rm -rf /tmp/** \
  && test -f /opt/phpstorm/bin/phpstorm.sh \
  && test -x /opt/phpstorm/bin/phpstorm.sh

ADD ./etc/phpstorm/supervisor /etc/supervisor
RUN chmod 777 -R /etc/supervisor