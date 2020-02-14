ARG DOCKER_IMAGE_VERSION
FROM mandy91/ubuntu-x11-hw:$DOCKER_IMAGE_VERSION
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root
RUN install-package git dialog unzip xmlstarlet


USER $USER

WORKDIR $HOME
RUN git clone --depth=1 https://github.com/RetroPie/RetroPie-Setup.git

USER root
ENV DEBIAN_FRONTEND=noninteractive

COPY ./install.sh /usr/local/bin/install.sh
RUN chmod +x /usr/local/bin/install.sh

RUN usermod -aG plugdev,input "$USER" 
RUN echo "$USER ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers.d/all
RUN passwd -d "$USER"

USER $USER

RUN sudo -E install.sh "setup basic_install"

RUN sudo -E install.sh autostart configedit
RUN sudo -E install.sh esthemes golang launchingimages
RUN sudo -E install.sh ps3controller retropie-manager retropiemenu runcommand samba scraper
RUN sudo -E install.sh sixaxis skyscraper xboxdrv image
RUN sudo -E install.sh lr-dolphin dolphin
RUN sudo -E install.sh lr-dosbox dosbox-sdl2
RUN sudo -E install.sh lr-bsnes lr-snes9x
RUN sudo -E install.sh lr-quicknes lr-nestopia
RUN sudo -E install.sh fs-uae lr-puae
RUN sudo -E install.sh lr-mupen64plus lr-mupen64plus-next mupen64plus lr-parallel-n64
RUN sudo -E install.sh reicast lr-redream lr-flycast

RUN sed -E -i 's#if dialog.*#if true; then#' "$HOME/RetroPie-Setup/scriptmodules/emulators/pcsx2.sh"
RUN sudo -E install.sh pcsx2
RUN sudo -E install.sh lr-pcsx-rearmed lr-beetle-psx
RUN sudo -E install.sh ppsspp lr-ppsspp
RUN sudo -E install.sh lr-gambatte lr-vba-next lr-tgbdual
RUN sudo -E install.sh lr-yabause lr-beetle-saturn

# Nintendo DS
RUN sudo -E install.sh lr-desmume

USER root
RUN ln -s /opt/retropie/supplementary/skyscraper/Skyscraper /usr/local/bin/Skyscraper
# COPY ./es_systems.cfg /opt/retropie/configs/all/emulationstation/es_systems.cfg

USER $USER
RUN mkdir -p "$HOME"/{.emulationstation,.skyscraper}
RUN sudo chown "$USER":"$USER" -R /opt/retropie/configs

VOLUME $HOME/.emulationstation
VOLUME $HOME/.skyscraper

COPY skyscript.sh $HOME/.skyscript.sh

RUN sudo chown "$USER":"$USER" -R "$HOME"

COPY ./entrypoint.sh /entrypoint

ENTRYPOINT [ "/entrypoint" ]
CMD [ "emulationstation" ]



# @todo why is the native retroarch also not working with the ps4 controller...