ARG DOCKER_IMAGE_VERSION
FROM mandy91/wine:$DOCKER_IMAGE_VERSION
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

COPY mobaxterm/mobaxterm/* $HOME/mobaxterm/

ENV WINEPREFIX="$HOME/.wine64" 
ENV WINEARCH=win64 

ENTRYPOINT [ "wine64" ]

CMD [ "$HOME/mobaxterm/MobaXterm_Personal_12.2.exe" ]
