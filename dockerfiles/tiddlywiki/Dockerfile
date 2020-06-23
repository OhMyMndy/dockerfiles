
ARG DOCKER_IMAGE_VERSION
FROM ohmymndy/alpine:$DOCKER_IMAGE_VERSION
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/ash", "-o", "pipefail", "-c" ]

RUN apk add --no-cache nodejs npm
RUN npm install -g tiddlywiki

VOLUME /data
WORKDIR /data

COPY tiddlywiki/root/ /

EXPOSE 8080

CMD s6-setuidgid $USER tiddlywiki . --listen host=0.0.0.0 port=8080
