ARG UBUNTU19_10
FROM mandy91/ubuntu-x11-hw:$UBUNTU19_10
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

RUN install-package --no-install-recommends filezilla
	

CMD s6-setuidgid $USER filezilla