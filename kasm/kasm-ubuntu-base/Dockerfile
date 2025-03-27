ARG BASE_IMAGE="kasmweb/core-ubuntu-noble:1.16.1-rolling-daily"
FROM $BASE_IMAGE

USER root

RUN apt-get update && apt-get install -y software-properties-common sudo \
    && curl -sL https://raw.githubusercontent.com/wimpysworld/deb-get/main/deb-get | bash -s install deb-get \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN usermod -aG sudo kasm-user \
    && passwd -d kasm-user \
    && chown kasm-user:kasm-user -R ~kasm-user

USER kasm-user

ENV HOME=/home/kasm-user
ENV USER=kasm-user

RUN bash -c "shopt -s dotglob && cp -f /etc/skel/* ~/" \
    && cat /home/kasm-default-profile/.bashrc >> ~/.bash_rc && mkdir -p ~/Desktop
