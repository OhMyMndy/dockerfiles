ARG UBUNTU19_10
FROM mandy91/ubuntu:$UBUNTU19_10
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root
RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive \
  apt-get install -y --no-install-recommends \
    fonts-noto \
    fonts-lato \
    virt-manager \
    virt-viewer \
    openssh-client \
    ssh-askpass-gnome \
    libspice-client-gtk-3.0-5 \
    libspice-client-glib-2.0-8 \
    gir1.2-spiceclientgtk-3.0 \
  && apt-get clean -y
  

USER $USER


ENTRYPOINT [ "virt-manager" ]