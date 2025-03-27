ARG IMAGE=docker.io/opensuse/leap:15.6
FROM $IMAGE

RUN zypper install -y git awk sed less && zypper clean

RUN git clone https://github.com/89luca89/distrobox.git \
    && cd distrobox \
    && bash -c "source <(awk '/setup_zypper\(/, /^}/' distrobox-init \
      | sed -E 's/\[\s+/[[ /g; s/\s+\]/ ]] /g') && setup_zypper dnf" \
    && cd .. \
    && rm -rf distrobox
