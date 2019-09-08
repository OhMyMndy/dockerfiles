FROM ubuntu:18.04
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends rsync openssh-client ssh-askpass \
  && apt-get clean -y \
  && apt-get autoclean -y \
  && apt-get autoremove -y \
  && rm -rf /tmp/*


RUN useradd -u 1000 -r -m -g ssh ssh && chown -R ssh:ssh /home/ssh

USER ssh
WORKDIR /home/ssh
VOLUME /home/ssh