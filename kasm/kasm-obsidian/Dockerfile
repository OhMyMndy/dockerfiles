ARG IMAGE_TAG
ARG BASE_IMAGE="ohmymndy/kasm-ubuntu-base:${IMAGE_TAG}"
FROM $BASE_IMAGE


RUN deb-get install obsidian; sudo apt-get update && sudo apt-get install -y -f -q && deb-get install obsidian


RUN mkdir -p ~/.local/share/applications/
RUN cp /usr/share/applications/obsidian.desktop ~/.local/share/applications/obsidian.desktop 
RUN sed -iE 's#/obsidian #/obsidian --no-sandbox #g' ~/.local/share/applications/obsidian.desktop

RUN update-desktop-database ~/.local/share/applications/