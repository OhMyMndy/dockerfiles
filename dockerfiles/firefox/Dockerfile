FROM jess/firefox:latest
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

RUN groupadd -r firefox -g 1000 \
    && useradd -m -u 1000 -r -m -g firefox -G audio,video firefox \
    && mkdir -p /home/firefox/{Downloads,.mozilla,.ssh} \
    && chown -R firefox:firefox /home/firefox

USER firefox

VOLUME /home/firefox/.mozilla