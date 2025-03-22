FROM ubuntu:24.04

RUN apt-get update && apt-get install git curl wget tar yq jq -y && apt-get clean

ARG ASDF_VERSION=0.16.6
RUN curl -SsL "https://github.com/asdf-vm/asdf/releases/download/v${ASDF_VERSION}/asdf-v${ASDF_VERSION}-linux-amd64.tar.gz" \
    | tar -C /usr/local/bin/ -xzf - &&  command -v asdf


# Python build dependencies
RUN apt-get update && apt-get install -y build-essential libssl-dev zlib1g-dev \
    	libbz2-dev libreadline-dev libsqlite3-dev curl git \
    	libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev -y && apt-get clean

# Nodejs build dependencies
RUN apt-get update && apt-get install -y python3 g++-12 gcc-12 make python3-pip -y && apt-get clean

# Ruby build dependencies
RUN apt-get update && apt-get install autoconf patch build-essential rustc libssl-dev libyaml-dev \
    libreadline6-dev zlib1g-dev libgmp-dev libncurses5-dev libffi-dev libgdbm6 \
    libgdbm-dev libdb-dev uuid-dev -y && apt-get clean

# Terraform build dependencies
RUN apt-get update && apt-get install unzip -y && apt-get clean

RUN mkdir -p /opt/asdf && chmod 777 -R /opt/asdf

ENV ASDF_DATA_DIR=/opt/asdf
ENV PATH="${ASDF_DATA_DIR}/shims:$PATH"

USER ubuntu

