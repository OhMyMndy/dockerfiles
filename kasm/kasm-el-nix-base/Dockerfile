ARG IMAGE_TAG=x
ARG BASE_IMAGE="ohmymndy/kasm-el-base:${IMAGE_TAG}"
FROM $BASE_IMAGE

USER root
RUN dnf install -y xz \
    && dnf clean all \
    && rm -rf /var/cache/dnf

USER kasm-user
ENV NIX_VERSION=2.27.0

ENV LD_LIBRARY_PATH=''
# RUN curl -SsL https://releases.nixos.org/nix/nix-$NIX_VERSION/install | sh -x -s -- --no-daemon
RUN curl -SsL https://nixos.org/nix/install | sh -x -s -- --no-daemon \
    && mkdir -p ~/.config/nix \
    && echo "experimental-features = nix-command flakes" >> ~/.config/nix/nix.conf \
    && mkdir -p ~/.config/nixpkgs \
    && echo "{ allowUnfree = true; }" >  ~/.config/nixpkgs/config.nix \
    && echo "source ~/.nix-profile/etc/profile.d/nix.sh" >> ~/.bashrc
