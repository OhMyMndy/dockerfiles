ARG UBUNTU20_04
FROM ohmymndy/ubuntu-x11-hw:$UBUNTU20_04
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]


RUN mkdir -p $HOME/{Downloads,.mozilla,.ssh} \
    && chown -R $USER:$USER $HOME

RUN install-package --no-install-recommends ffmpeg firefox

RUN echo 'pref("browser.tabs.remote.autostart", false);' >> /etc/firefox/syspref.js
RUN echo 'pref("security.enterprise_roots.enabled", true);' >> /etc/firefox/syspref.js


USER $USER

VOLUME $USER/.mozilla

USER root

CMD s6-setuidgid $USER firefox