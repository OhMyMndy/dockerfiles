ARG UBUNTU18_04
FROM ohmymndy/ubuntu-x11:$UBUNTU18_04
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

RUN install-package python-pip

RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive \
	curl -sSL http://ftp.nl.debian.org/debian/pool/main/g/gnome-python-desktop/python-wnck_2.32.0+dfsg-3_amd64.deb >> "/tmp/python-wnck.deb" \
	&& dpkg -i "/tmp/python-wnck.deb" \
  ; install-package -f \
  && rm /tmp/*
  
RUN pip install -q https://github.com/ssokolow/quicktile/archive/master.zip

CMD s6-setuidgid $USER quicktile --daemonize
