ARG IMAGE_TAG=x
ARG BASE_IMAGE="ohmymndy/kasm-ubuntu-base:${IMAGE_TAG}"
FROM $BASE_IMAGE

USER root
RUN deb-get install obsidian; apt-get update \
    && apt-get install -y -f -q \
    && deb-get install obsidian \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER kasm-user

RUN mkdir -p ~/.local/share/applications/ \
    && cp /usr/share/applications/obsidian.desktop ~/.local/share/applications/obsidian.desktop \
    && sed -iE 's#/obsidian #/obsidian --no-sandbox #g' ~/.local/share/applications/obsidian.desktop \
    && update-desktop-database ~/.local/share/applications/
