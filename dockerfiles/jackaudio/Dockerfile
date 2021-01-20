ARG UBUNTU20_04
FROM ohmymndy/ubuntu-x11-hw:$UBUNTU20_04
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

RUN install-package curl
RUN install-deb-from-url https://launchpad.net/\~kxstudio-debian/+archive/kxstudio/+files/kxstudio-repos_10.0.3_all.deb

	#sudo -E dpkg --purge kxstudio-repos-gcc5
RUN install-package python-gconf python-pip supervisor jackd2 carla-git cadence jack-mixer pulseaudio-module-jack mididings lsp-plugins liblash-compat-1debian0 jack-mixer
RUN pip install gconf

COPY jackaudio/root/ /

WORKDIR /audio
CMD s6-setuidgid $USER supervisord