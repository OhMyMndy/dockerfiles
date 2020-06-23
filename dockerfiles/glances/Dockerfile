
ARG DOCKER_IMAGE_VERSION
FROM ohmymndy/alpine:$DOCKER_IMAGE_VERSION
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/ash", "-o", "pipefail", "-c" ]

RUN apk add --no-cache glances

ENTRYPOINT s6-setuidgid $USER glances
