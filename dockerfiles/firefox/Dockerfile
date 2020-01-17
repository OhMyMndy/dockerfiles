ARG UBUNTU19_10
FROM mandy91/ubuntu:$UBUNTU19_10
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]


RUN mkdir -p $HOME/{Downloads,.mozilla,.ssh} \
    && chown -R $USER:$USER $HOME

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
	apulse \
	ffmpeg \
	firefox \
	hicolor-icon-theme \
	libasound2 \
	libgl1-mesa-dri \
	libgl1-mesa-glx \
	libpulse0 \
    firefox \
    fonts-noto-color-emoji fonts-noto fonts-roboto \
	&& apt-get clean -y

RUN echo 'pref("browser.tabs.remote.autostart", false);' >> /etc/firefox/syspref.js
RUN echo 'pref("security.enterprise_roots.enabled", true);' >> /etc/firefox/syspref.js


USER $USER

VOLUME $USER/.mozilla

USER root

COPY root/ /
CMD s6-setuidgid $USER firefox