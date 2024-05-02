ARG BASE_IMAGE="kasmweb/core-ubuntu-jammy:develop"
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