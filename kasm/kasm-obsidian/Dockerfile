ARG BASE_IMAGE="kasmweb/ubuntu-focal-desktop:develop"
FROM $BASE_IMAGE
USER root

RUN apt-get update \
    && apt-get install -y software-properties-common sudo

RUN curl -sL https://raw.githubusercontent.com/wimpysworld/deb-get/main/deb-get | sudo -E bash -s install deb-get
RUN deb-get install obsidian
RUN deb-get install insync
RUN deb-get install vivaldi-stable
RUN deb-get install signal-desktop

RUN chown kasm-user:kasm-user -R ~kasm-user
USER kasm-user