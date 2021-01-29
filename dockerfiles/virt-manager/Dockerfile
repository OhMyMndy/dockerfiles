ARG UBUNTU20_04
FROM ohmymndy/ubuntu:$UBUNTU20_04
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root
RUN install-package \
    fonts-noto \
    fonts-lato \
    virt-manager \
    virt-viewer \
    openssh-client \
    ssh-askpass-gnome \
    libspice-client-gtk-3.0-5 \
    libspice-client-glib-2.0-8 \
    gir1.2-spiceclientgtk-3.0
  
USER $USER

RUN mkdir -p "$HOME/.config/dconf"
VOLUME $HOME/.config/dconf

USER root

CMD s6-setuidgid $USER virt-manager