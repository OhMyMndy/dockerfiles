ARG IMAGE_TAG=x
ARG BASE_IMAGE="ohmymndy/kasm-ubuntu-base:${IMAGE_TAG}"
FROM $BASE_IMAGE


USER kasm-user
ENV NIX_VERSION=2.22.0
ENV LD_LIBRARY_PATH=
# RUN curl -SsL https://releases.nixos.org/nix/nix-$NIX_VERSION/install | sh -x -s -- --no-daemon
RUN curl -SsL https://nixos.org/nix/install | sh -x -s -- --no-daemon

RUN mkdir -p ~/.config/nix \
    && echo "experimental-features = nix-command flakes" >> ~/.config/nix/nix.conf


RUN mkdir -p ~/.config/nixpkgs \
    && echo "{ allowUnfree = true; }" >  ~/.config/nixpkgs/config.nix

RUN echo "source ~/.nix-profile/etc/profile.d/nix.sh" >> ~/.bashrc 
