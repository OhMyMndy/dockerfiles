ARG BASE_IMAGE="kasmweb/core-rockylinux-9:develop"
FROM $BASE_IMAGE
USER root

RUN dnf install -y sudo podman podman-docker && \
    dnf clean all && \
    rm -rf /var/cache/dnf
RUN chmod ug+s /usr/bin/new{gid,uid}map


RUN usermod -aG wheel kasm-user
RUN passwd -d kasm-user

RUN chown kasm-user:kasm-user -R ~kasm-user
USER kasm-user


ENV HOME=/home/kasm-user
ENV USER=kasm-user

RUN bash -c "shopt -s dotglob && cp -f /etc/skel/* ~/"
RUN cat /home/kasm-default-profile/.bashrc >> ~/.bash_rc && mkdir -p ~/Desktop
