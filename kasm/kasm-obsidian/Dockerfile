ARG BASE_IMAGE="kasmweb/ubuntu-focal-desktop:develop"
FROM $BASE_IMAGE
USER root

RUN apt-get update \
    && apt-get install -y software-properties-common sudo

RUN curl -sL https://raw.githubusercontent.com/wimpysworld/deb-get/main/deb-get | sudo -E bash -s install deb-get
RUN deb-get install obsidian
RUN deb-get install insync
RUN deb-get install vivaldi-stable
RUN deb-get install signal-desktop

RUN usermod -aG sudo kasm-user
RUN passwd -d kasm-user

RUN chown kasm-user:kasm-user -R ~kasm-user
USER kasm-user

RUN mkdir -p ~/.local/share/applications/
RUN cp /usr/share/applications/obsidian.desktop ~/.local/share/applications/obsidian.desktop 
RUN sed -iE 's#/obsidian #/obsidian --no-sandbox #g' ~/.local/share/applications/obsidian.desktop

RUN cp /usr/share/applications/vivaldi-stable.desktop ~/.local/share/applications/vivaldi-stable.desktop 
RUN sed -iE 's#/vivaldi-stable #/vivaldi-stable --no-sandbox #g' ~/.local/share/applications/vivaldi-stable.desktop
RUN update-desktop-database ~/.local/share/applications/