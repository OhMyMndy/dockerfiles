
ARG DOCKER_IMAGE_VERSION
FROM ohmymndy/alpine:${DOCKER_IMAGE_VERSION}
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/ash", "-o", "pipefail", "-c" ]


#  ca-certificates libnss3-tools
RUN apk add --no-cache  tmux


ENTRYPOINT [ "/init" ]
CMD s6-setuidgid $USER tmux