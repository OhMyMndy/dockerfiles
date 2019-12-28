ARG UBUNTU19_10
FROM mandy91/ubuntu:$UBUNTU19_10
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root


RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
	gpg-agent \
	python3-pip \
	python-pip \
	php-cli php-xml php-mbstring php-curl php-zip php-pdo-sqlite php-pdo-mysql php-intl php-zmq \
	# Gnu global and exuberant ctags
	global ctags \
	&& apt-get clean -y

RUN curl -sL https://deb.nodesource.com/setup_12.x | APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=DontWarn bash -
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs \
	&& apt-get clean -y

RUN curl -fLSs https://circle.ci/cli | bash

RUN scversion="stable" \
	&& curl -L "https://storage.googleapis.com/shellcheck/shellcheck-${scversion?}.linux.x86_64.tar.xz" | tar -xJv \
	&& cp "shellcheck-${scversion}/shellcheck" /usr/bin/ \
	&& rm -rf "shellcheck-${scversion}"


RUN curl -L "https://github.com/hadolint/hadolint/releases/download/v1.17.3/hadolint-Linux-x86_64" > /usr/bin/hadolint \
	&& chmod +x /usr/bin/hadolint

RUN	curl -sS https://getcomposer.org/installer | php \
	&& mv composer.phar /usr/local/bin/composer
RUN composer --version

RUN PATH=$PATH:$HOME/.composer/vendor/bin

USER $USER


RUN pip3 install mypy yamllint flake8 autopep8
# python3 version is not in pypi
RUN pip install crudini

RUN npm config set prefix "$HOME/.local"
RUN npm install -g vsce
RUN npm install -g markdownlint-cli
RUN npm install -g vsce
RUN npm install -g bash-language-server
RUN npm install -g intelephense
RUN npm install -g bats
RUN npm install -g json


# Add go dev things
USER root

RUN wget https://dl.google.com/go/go1.13.5.linux-amd64.tar.gz \
	&& tar -xvf go1.13.5.linux-amd64.tar.gz \
	&& mv go /usr/local

ENV GOPATH /go
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y pandoc \
	&& apt-get clean -y

RUN go get github.com/mrtazz/checkmake \
	&& cd $GOPATH/src/github.com/mrtazz/checkmake \
	&& make



ENTRYPOINT [ "/bin/bash", "-c", "code && while pgrep code &>/dev/null; do sleep 10; done" ]