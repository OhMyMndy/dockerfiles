ARG TAG=41
FROM quay.io/fedora/fedora:${TAG}

RUN dnf install -y git

RUN git clone https://github.com/89luca89/distrobox.git \
    && cd distrobox \
    && bash -c "source <(awk '/setup_dnf\(/, /^}/' distrobox-init \
      | sed -E 's/\[\s+/[[ /g; s/\s+\]/ ]] /g') && setup_dnf dnf" \
    && cd .. \
    && rm -rf distrobox