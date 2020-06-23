ARG DOCKER_IMAGE_VERSION
FROM ohmymndy/wine5:$DOCKER_IMAGE_VERSION
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER $USER
COPY mobaxterm/mobaxterm/* $HOME/mobaxterm/

ENV WINEPREFIX="$HOME/.wine64" 
ENV WINEARCH=win64 


USER root

RUN chown -R "$USER":"$USER" "$HOME"
CMD s6-setuidgid $USER wine64 "$HOME/mobaxterm/MobaXterm_Personal_12.2.exe"
