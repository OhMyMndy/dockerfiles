FROM codercom/code-server:latest
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]


USER root


ARG OVERLAY_VERSION="v1.22.1.0"
ARG OVERLAY_ARCH="amd64"

ENV SHELL=bash
ENV HOME=/home/coder
ENV USER=coder

ADD https://github.com/just-containers/s6-overlay/releases/download/${OVERLAY_VERSION}/s6-overlay-${OVERLAY_ARCH}.tar.gz /tmp/

RUN tar xzf /tmp/s6-overlay-${OVERLAY_ARCH}.tar.gz -C /

RUN curl -sSL https://deb.nodesource.com/setup_12.x | sudo -E bash - >/dev/null
RUN apt-get update -qq && apt-get install -y -qq \
	curl \
	readline-common \
    nodejs \
    rsync \
    python3-pip \
    git \
    openssh-client \
	&& rm -rf /var/lib/apt/lists/*
RUN npm install -g --silent json >/dev/null


RUN curl -LO https://github.com/BurntSushi/ripgrep/releases/download/11.0.2/ripgrep_11.0.2_amd64.deb && dpkg -i ripgrep_11.0.2_amd64.deb && rm ripgrep_11.0.2_amd64.deb


RUN docker_url=https://download.docker.com/linux/static/stable/x86_64; \
    docker_version="19.03.8"; \
    curl -fsSL $docker_url/docker-$docker_version.tgz | \
    tar zxvf - --strip 1 -C /usr/bin docker/docker


RUN apt-get update -qq && apt-get install -y -qq \
	curl \
	readline-common \
    nodejs \
    rsync \
    python3-pip \
    git \
    openssh-client \
	&& rm -rf /var/lib/apt/lists/*

RUN chown $USER:$USER -R $HOME

USER coder

RUN curl -LsS https://raw.githubusercontent.com/Mandy91/dotfiles/master/installers/apps/code.sh | bash -

RUN cd /tmp && git clone https://github.com/Mandy91/dotfiles.git && cd dotfiles && sudo /tmp/dotfiles/installers/ubuntu.sh --dev --php && rm -rf /tmp/dotfiles


USER root


COPY code-server/root/ /


ENTRYPOINT [ "/init" ]
CMD s6-setuidgid $USER code-server --host 0.0.0.0



#    1  code-server --install-extension byi8220.indented-block-highlighting
#     2  code-server --install-extension naumovs.color-highlight
#     3  curl
#     4  curl -SsL https://raw.githubusercontent.com/Mandy91/dotfiles/master/installers/apps/code.sh | bash -
#     5  curl -SsL https://raw.githubusercontent.com/Mandy91/dotfiles/master/.base-script.sh > ~/.base-script.sh
#     6  curl -SsL https://raw.githubusercontent.com/Mandy91/dotfiles/master/installers/apps/code.sh | bash -
#     7  mkdir -p ~/dotfiles/installers/apps
#     8  curl -SsL https://raw.githubusercontent.com/Mandy91/dotfiles/master/.base-script.sh > ~/dotfiles/.base-script.sh
#     9  curl -SsL https://raw.githubusercontent.com/Mandy91/dotfiles/master/installers/apps/code.sh | bash -
#    10  cd ~/dotfiles/installers/apps; curl -SsL https://raw.githubusercontent.com/Mandy91/dotfiles/master/installers/apps/code.sh | bash -
#    11  git
#    12  git clone https://github.com/Mandy91/dotfiles.git
#    13  rm -rf dotfiles
#    14  git clone https://github.com/Mandy91/dotfiles.git
#    15  ~/dotfiles/installers/apps/code.sh
#    16  code-server --install-extension fallenwood.viml
#    17  node
#    18  npm
#    19  nodejs
#    20  code-server --install-extension pkief.material-icon-theme
#    21  code-server --install-extension xyz.local-history
#    22  code-server --install-extension mrmlnc.vscode-duplicate
#    23  code-server --install-extension mads-hartmann.bash-ide-vscode
#    24  code-server --install-extension exiasr.hadolint
#    25  code-server --install-extension ms-azuretools.vscode-docker
#    26  code-server --install-extension ms-vscode.vscode-typescript-tslint-plugin
#    27  code-server --install-extension eamodio.gitlens
#    28  code-server --install-extension donjayamanne.githistory
#    29  code-server --install-extension jomeinaster.bracket-peek
#    30  code-server --install-extension formulahendry.code-runner
#    31  code-server --install-extension buenon.scratchpads
#    32  json
#    33  sudo ls
#    34  curl -sSL https://deb.nodesource.com/setup_12.x | sudo -E bash - >/dev/null
#    35  sudo apt update; sudo apt install nodejs -y -qq
#    36  npm install -g --silent --force json
#    37  json
#    38  sudo npm install -g --silent --force json
#    39  json
#    40  ~/dotfiles/installers/apps/code.sh --settings
#    41  code-server ~/dotfiles/installers/apps/code.sh
#    42  ~/dotfiles/installers/apps/code.sh
#    43  ls -lash ~
#    44  ls -lash ~/.config/
#    45  ls -lash ~/.local/share/code-server/
#    46  ls -lash ~/.config/configstore/update-notifier-npm.json 
#    47  ls -lash ~/.local/share/code-server/
#    48  ls -lash ~/.local/share/code-server/User/
#    49  ~/dotfiles/installers/apps/code.sh
#    50  code-server --help
#    51  history