ARG BASE_IMAGE="kasmweb/core-rockylinux-9:1.16.1-rolling-daily"
FROM $BASE_IMAGE
USER root

RUN dnf install -y sudo podman podman-docker \
    && dnf clean all \
    && rm -rf /var/cache/dnf \
    && chmod ug+s /usr/bin/newgidmap /usr/bin/newuidmap \
    && usermod -aG wheel kasm-user \
    && passwd -d kasm-user \
    && chown kasm-user:kasm-user -R ~kasm-user
USER kasm-user

ENV HOME=/home/kasm-user
ENV USER=kasm-user

RUN bash -c "shopt -s dotglob && cp -f /etc/skel/* ~/" \
    && cat /home/kasm-default-profile/.bashrc >> ~/.bash_rc && mkdir -p ~/Desktop
