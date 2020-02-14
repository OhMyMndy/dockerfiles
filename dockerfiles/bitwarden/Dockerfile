ARG UBUNTU18_04
FROM mandy91/ubuntu-x11-hw:$UBUNTU18_04
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

RUN install-package curl
RUN install-deb-from-url "https://vault.bitwarden.com/download/?app=desktop&platform=linux&variant=deb"

RUN chmod 4755 /opt/Bitwarden/chrome-sandbox && chown root /opt/Bitwarden/chrome-sandbox


CMD s6-setuidgid $USER bitwarden --no-sandbox