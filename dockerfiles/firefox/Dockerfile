FROM jess/firefox
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"

RUN groupadd -r firefox -g 1000 && useradd -u 1000 -r -m -g firefox -G audio,video firefox \
    && mkdir -p /home/firefox/Downloads && mkdir -p /home/firefox/.mozilla && chown -R firefox:firefox /home/firefox

USER firefox

VOLUME /home/firefox/.mozilla