ARG BASE_IMAGE="kasmweb/core-ubuntu-noble:develop"
FROM $BASE_IMAGE
USER root

RUN apt-get update && \
    apt-get install -y software-properties-common sudo && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


RUN curl -sL https://raw.githubusercontent.com/wimpysworld/deb-get/main/deb-get | sudo -E bash -s install deb-get

RUN usermod -aG sudo kasm-user
RUN passwd -d kasm-user

RUN chown kasm-user:kasm-user -R ~kasm-user
USER kasm-user


ENV HOME=/home/kasm-user
ENV USER=kasm-user

RUN bash -c "shopt -s dotglob && cp -f /etc/skel/* ~/"
RUN cat /home/kasm-default-profile/.bashrc >> ~/.bash_rc && mkdir -p ~/Desktop
