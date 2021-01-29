ARG UBUNTU20_04
FROM ohmymndy/ubuntu:$UBUNTU20_04
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root

RUN install-package openjdk-8-jdk openjdk-8-jre unzip libgdiplus curl rsync git python3.7 python3.7-dev python3-pip software-properties-common


USER $USER
RUN mkdir -p "$HOME/Minecraft" \
  && curl -sSL https://s3.amazonaws.com/Minecraft.Download/versions/1.11.2/minecraft_server.1.11.2.jar -o "$HOME/Minecraft/minecraft_server.jar" \
  && chmod +x "$HOME/Minecraft/minecraft_server.jar" \
  && mkdir -p touch "$HOME/Minecraft/logs" \
  && touch "$HOME/Minecraft/logs/latest.log"

# hadolint ignore=DL3003
RUN mkdir -p "$HOME/crafty" \
  && cd "$HOME/crafty" \
  && git clone https://gitlab.com/Ptarrant1/crafty-web.git

# hadolint ignore=DL3003
RUN cd "$HOME/crafty/crafty-web" \
  && pip3 install -r requirements.txt

COPY crafty/config.yml "$HOME/crafty/config.yml"
RUN echo 'eula=true' > "$HOME/Minecraft/eula.txt"

EXPOSE 8000
EXPOSE 25565

# hadolint ignore=DL3000
WORKDIR "$HOME/crafty/crafty-web"
USER root
RUN mkdir -p /crafty_db && chown "$USER:$USER" -R /crafty_db
CMD s6-setuidgid $USER python3 "$HOME/crafty/crafty-web/crafty.py" -c "$HOME/crafty/config.yml"

