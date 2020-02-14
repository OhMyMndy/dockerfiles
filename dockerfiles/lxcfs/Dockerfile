FROM alpine
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/ash", "-o", "pipefail", "-c" ]

RUN apk add --no-cache lxcfs 

RUN mkdir -p /lxcfs/lxcfs
VOLUME /lxcfs

ENTRYPOINT [ "/usr/bin/lxcfs", "/lxcfs/lxcfs" ]