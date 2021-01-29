ARG UBUNTU20_04
FROM ohmymndy/ubuntu-x11:$UBUNTU20_04
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root
RUN install-package curl
RUN add-apt-repository ppa:ondrej/php
RUN install-deb-from-url https://github.com/wkhtmltopdf/packaging/releases/download/0.12.1.4-2/wkhtmltox_0.12.1.4-2.bionic_amd64.deb
RUN install-package php7.4-cli composer php7.4-opcache php7.4-zip php7.4-curl php7.4-yaml php7.4-xml php7.4-mbstring php7.4-curl php7.4-zip php7.4-pdo-sqlite php7.4-intl php7.4-zmq

CMD s6-setuidgid $USER php