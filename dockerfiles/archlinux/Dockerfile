FROM archlinux
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

ARG USER=user

ENV SHELL=/bin/bash
ENV USER=$USER
ENV HOME=/home/$USER
ENV PATH=$PATH:$HOME/.local/bin

WORKDIR $HOME


RUN pacman-key --init && pacman-key --populate archlinux
RUN pacman -Syy --noconfirm --noprogressbar \
    && pacman -S --noconfirm --needed --noprogressbar git sudo binutils

# Add user, group sudo
RUN groupadd --system sudo && \
    sed -i -e "s/Defaults    requiretty.*/ #Defaults    requiretty/g" /etc/sudoers && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

RUN groupadd --gid 1000 "$USER" \
    && useradd --uid 1000 --gid 1000 --create-home --home-dir "$HOME" "$USER" \
	&& mkdir -p "$HOME"/{.ssh,.config,.local/share} \
	&& chown -R "$USER":"$USER" "$HOME" \
	&& usermod -a -G audio,video,root,sudo "$USER"


VOLUME $HOME/.ssh


# Install yay - https://github.com/Jguer/yay
ENV yay_version=9.4.2
ENV yay_folder=yay_${yay_version}_x86_64
RUN cd /tmp && \
    curl -LsS https://github.com/Jguer/yay/releases/download/v${yay_version}/${yay_folder}.tar.gz | tar zx && \
    install -Dm755 ${yay_folder}/yay /usr/bin/yay && \
    install -Dm644 ${yay_folder}/yay.8 /usr/share/man/man8/yay.8
