#!/usr/bin/env bash

set -o errexit -o nounset -o pipefail -e

INPUT_GROUP_ID="$(cut -d: -f3 < <(getent group input))"
PLUGDEV_GROUP_ID="$(cut -d: -f3 < <(getent group plugdev))"

user=$(whoami)

environment="- PUID=$(id -u)
    - PGID=$(id -g)
    - INPUT_GROUP_ID=${INPUT_GROUP_ID}
    - PLUGDEV_GROUP_ID=${PLUGDEV_GROUP_ID}"

DOCKER_IMAGE_VERSION=0.1
	function total_memory_in_kb() {
		grep MemTotal /proc/meminfo | grep -Eo '[0-9]+' | tr -d '\n\r'
	}

	function total_memory_in_mb() {
		bc <<< "(($(total_memory_in_kb)) / 1024)"
	}

	function total_memory_in_gb() {
		bc <<< "(($(total_memory_in_mb)) / 1024)"
	}

	function percentage_of_memory_in_kb() {
		bc <<< "(($(total_memory_in_kb)) / 100) * $1" | awk '{printf "%d\n", $0}'
	}

	function percentage_of_memory_in_mb() {
		bc <<< "(($(total_memory_in_mb)) / 100) * $1" | awk '{printf "%d\n", $0}'
	}

	function percentage_of_memory_in_gb() {
		bc <<< "scale=1;(($(total_memory_in_gb)) / 100) * $1" | awk '{printf "%.1f\n", $0}'
	}


cat <<EOF
version: '2.3'

x-default: &default
  init: true
  environment:
    - DISPLAY
    - SSH_AUTH_SOCK
    $environment
  volumes:
    - /tmp/.X11-unix:/tmp/.X11-unix
    - /run/user/${UID:-1000}/pulse:/run/user/1000/pulse
    - ./etc/pulse/pulse-client.conf:/etc/pulse/client.conf:ro
    - $HOME/.config/fontconfig:/root/.config/fontconfig:ro
    - $HOME/.config/fontconfig:$HOME/.config/fontconfig:ro
    - $HOME/.config/gtk-2.0:$HOME/.config/gtk-2.0:ro
    - $HOME/.config/gtk-3.0:$HOME/.config/gtk-3.0:ro
    - /etc/timezone:/etc/timezone:ro
    - /etc/localtime:/etc/localtime:ro
    - ./dockerfiles/ubuntu/root/etc/cron.d:/etc/cron.d:ro
    - /dev/shm:/dev/shm
    - /etc/machine-id:/etc/machine-id:ro
    - ./etc/ssl/certificates:/etc/ssl/certificates:ro
    - /usr/share/fonts:/usr/share/fonts:ro
    - /usr/share/themes:/usr/share/themes:ro
    - /usr/share/icons:/usr/share/icons:ro
    #- /usr/share/fontconfig:/usr/share/fontconfig:ro
    - $HOME/.local/share/fonts:$HOME/.local/share/fonts:ro
  env_file: .env

services:
  ubuntu19.10:
    <<: *default
    build:
      context: ./dockerfiles/ubuntu
      args:
        - DOCKER_IMAGE_VERSION=${DOCKER_IMAGE_VERSION}
        - UBUNTU19_10=0.1-19.10
        - UBUNTU18_04=0.1-18.04
        - VERSION=19.10
        - USER=${user}
    image: mandy91/ubuntu:${DOCKER_IMAGE_VERSION}-19.10

  ubuntu18.04:
    extends: ubuntu19.10
    build:
      context: ./dockerfiles/ubuntu
      args:
        - VERSION=18.04
    image: mandy91/ubuntu:${DOCKER_IMAGE_VERSION}-18.04

  ubuntu19.10-gui:
    extends: ubuntu19.10
    build:
      context: ./dockerfiles/ubuntu-gui
    image: mandy91/ubuntu-gui:${DOCKER_IMAGE_VERSION}-19.10


  alpine:
    extends: ubuntu19.10
    build:
      context: ./dockerfiles/alpine
    image: mandy91/alpine:${DOCKER_IMAGE_VERSION}-19.10

   

  archlinux:
    <<: *default
    build:
      context: ./dockerfiles/archlinux
      args:
        - DOCKER_IMAGE_VERSION=${DOCKER_IMAGE_VERSION}
        - USER=${user}
    environment:
      - DISPLAY=unix$DISPLAY
    image: mandy91/archlinux:${DOCKER_IMAGE_VERSION}


  ubuntu-x11-hw:
    extends: ubuntu19.10
    build:
      context: ./dockerfiles/ubuntu-x11-hw
    image: mandy91/ubuntu-x11-hw:${DOCKER_IMAGE_VERSION}

  vpn:
    extends: ubuntu19.10
    build:
      context: ./dockerfiles/vpn
    image: mandy91/vpn:${DOCKER_IMAGE_VERSION}
    privileged: true
    volumes:
      - ./etc/openvpn:/etc/openvpn
      - ssh_config:$HOME/.ssh
    entrypoint: sleep infinity

  firefox:
    extends: ubuntu19.10
    build:
      context: ./dockerfiles/firefox
    image: mandy91/firefox:${DOCKER_IMAGE_VERSION}
    volumes:
      - ./storage/firefox:$HOME/.mozilla
      - $HOME/Downloads:$HOME/Downloads
    network_mode: service:vpn


  chrome:
    extends: ubuntu19.10
    build: ./dockerfiles/chrome
    image: mandy91/chrome:${DOCKER_IMAGE_VERSION}
    volumes:
      - ./storage/chrome:/data
      - $HOME/Downloads:$HOME/Downloads
    security_opt:
      - seccomp="./seccomp/chrome.json"
    devices:
      - /dev/dri
    network_mode: service:vpn

  # Make sure to generate a SSH key first and ssh-copy-id to the server you want to connect to
  # Run: docker-compose run --rm virt-manager virt-viewer -c qemu+ssh://<user>@<ip>/system <vm_name>
  virt-manager:
    extends: ubuntu19.10
    image: mandy91/virt-manager:${DOCKER_IMAGE_VERSION}
    build:
      context: ./dockerfiles/virt-manager
    volumes:
      - ssh_config:$HOME/.ssh
      - $HOME/Downloads:$HOME/Downloads
      - ./storage/virt-manager:$HOME/.config/dconf
    devices:
      - /dev/dri
    network_mode: service:vpn

  nomachine:
    extends: ubuntu19.10
    image: mandy91/nomachine:${DOCKER_IMAGE_VERSION}
    build:
      context: ./dockerfiles/nomachine
    volumes:
      - ssh_config:$HOME/.ssh
      - $HOME/Downloads:$HOME/Downloads
      - ./storage/nomachine-configs:$HOME/.nx
      - ./storage/nomachine:$HOME/NoMachine
    devices:
      - /dev/dri
    network_mode: service:vpn

  vim:
    extends: ubuntu19.10
    volumes:
      - $HOME/.vimrc:$HOME/.vimrc:ro
      - $HOME/.vim:$HOME/.vim:ro
      - /:/host
    entrypoint: ["vim"]
    network_mode: service:vpn

  filezilla:
    extends: ubuntu19.10
    build:
      context: ./dockerfiles/filezilla
    image: mandy91/filezilla:${DOCKER_IMAGE_VERSION}
    volumes:
      - ./storage/filezilla:$HOME/.config/filezilla
      - ssh_config:$HOME/.ssh
      - $HOME/Downloads:$HOME/Downloads
    network_mode: service:vpn

  # Run: docker-compose run --rm vinagre --vnc-scale <ip> &> /tmp/vinagre.log &
  vinagre:
    extends: ubuntu19.10
    build:
      context: ./dockerfiles/vinagre
    image: mandy91/vinagre:${DOCKER_IMAGE_VERSION}
    volumes:
      - ssh_config:$HOME/.ssh
      - /dev/shm:/dev/shm
    network_mode: service:vpn

  wine:
    extends: ubuntu19.10
    build:
      context: ./dockerfiles/wine
    image: mandy91/wine:${DOCKER_IMAGE_VERSION}
    devices:
      - /dev/dri

  lutris:
    extends: wine
    build:
      context: ./dockerfiles/lutris
    image: mandy91/lutris:${DOCKER_IMAGE_VERSION}
    volumes:
      - /tank:/tank:ro
      - $HOME/network_media:$HOME/network_media
      - lutris:$HOME/.local/share/lutris


  mednafen:
    extends: ubuntu19.10
    build:
      context: ./dockerfiles/mednafen
    image: mandy91/mednafen:${DOCKER_IMAGE_VERSION}
    volumes:
      - mednafen:$HOME/.mednafen
      - $HOME/Nextcloud/Retro/:/roms:ro
      - $HOME/Downloads/:$HOME/Downloads
    devices:
      - /dev/dri

  retroarch:
    extends: ubuntu19.10
    build:
      context: ./dockerfiles/retroarch
    image: mandy91/retroarch:${DOCKER_IMAGE_VERSION}
    volumes:
      - retroarch:$HOME/.config/retroarch
      - $HOME/Nextcloud/Retro/:/roms:ro
      - $HOME/Downloads/:$HOME/Downloads
      - /dev:/dev
    devices:
      - /dev/dri


  dosbox:
    extends: ubuntu19.10
    build:
      context: ./dockerfiles/dosbox
    image: mandy91/dosbox:${DOCKER_IMAGE_VERSION}
    volumes:
      - $HOME/Nextcloud/Retro/:/roms:ro
      - $HOME/Downloads/:$HOME/Downloads
    devices:
      - /dev/dri


  jupyter:
    extends: ubuntu19.10
    image: mandy91/jupyter:${DOCKER_IMAGE_VERSION}
    build:
      context: ./dockerfiles/jupyter
    ports:
      - 8888:8888
    volumes:
      - jupyter:$HOME/.jupyter
      - /tank/media/docs:$HOME/Docs
      - ./etc/jupyter/.bash_aliases:$HOME/.bash_aliases
      - $HOME/Downloads/:$HOME/Downloads
      - /tank:$HOME/tank:ro

  mobaxterm:
    extends: wine
    build:
      context: ./dockerfiles/mobaxterm
    image: mandy91/mobaxterm:${DOCKER_IMAGE_VERSION}
    volumes:
      - mobaxterm_wine:$HOME/.wine

  ssh:
    extends: ubuntu19.10
    build:
      context: ./dockerfiles/ssh
    image: mandy91/ssh:${DOCKER_IMAGE_VERSION}
    volumes:
      - ssh_config:/home/ssh/.ssh
      - $HOME/Downloads:$HOME/Downloads
    network_mode: service:vpn

  network-tools:
    extends: ubuntu19.10
    build:
      context: ./dockerfiles/network-tools
    image: mandy91/network-tools:${DOCKER_IMAGE_VERSION}
    init: true
    environment:
      - DISPLAY
    volumes:
      - /etc/timezone:/etc/timezone:ro
      - /etc/localtime:/etc/localtime:ro
      - ssh_config:$HOME/.ssh
      - $HOME/Downloads:$HOME/Downloads:ro
    network_mode: service:vpn

  system-tools:
    extends: ubuntu19.10
    build:
      context: ./dockerfiles/system-tools
    image: mandy91/system-tools:${DOCKER_IMAGE_VERSION}
    network_mode: service:vpn

  vlc:
    extends: ubuntu19.10
    build:
      context: ./dockerfiles/vlc
    image: mandy91/vlc:${DOCKER_IMAGE_VERSION}
    volumes:
      - vlc:/home/vlc/.config/vlc
    devices:
      - /dev/dri
    network_mode: service:vpn

  squid-cache:
    extends: ubuntu19.10
    build:
      context: ./dockerfiles/squid-cache
    image: mandy91/squid-cache:${DOCKER_IMAGE_VERSION}
    ports:
      - 3128:3128
    volumes:
      - ./dockerfiles/squid-cache/squid.conf:/etc/squid/squid.conf:ro
      - ./dockerfiles/squid-cache/entrypoint.sh:/entrypoint
      - $HOME/.squid-cache:/var/cache/squid/

  dev:
    extends: ubuntu19.10
    build:
      context: ./dockerfiles/dev
    image: mandy91/dev:${DOCKER_IMAGE_VERSION}
    volumes:
      - $PWD:$PWD

  vscode:
    extends: ubuntu19.10-gui
    build:
      context: ./dockerfiles/vscode
    image: mandy91/vscode:${DOCKER_IMAGE_VERSION}
    volumes:
      # - $PWD:$PWD
      - ./storage/vscode:$HOME/.config/Code

  spacefm:
    extends: ubuntu19.10-gui
    build:
      context: ./dockerfiles/spacefm
    image: mandy91/spacefm:${DOCKER_IMAGE_VERSION}
    #volumes:
      #- $HOME/.config:$HOME/.config:ro
      #- /usr/share/themes/:/usr/share/themes/:ro

  quicktile:
    extends: ubuntu18.04
    build:
      context: ./dockerfiles/quicktile
    image: mandy91/quicktile:${DOCKER_IMAGE_VERSION}
    #volumes:
      #- $HOME/.config:$HOME/.config:ro
      #- /usr/share/themes/:/usr/share/themes/:ro

  shutter:
    extends: ubuntu19.10-gui
    build:
      context: ./dockerfiles/shutter
    image: mandy91/shutter:${DOCKER_IMAGE_VERSION}
    volumes:
      - ./storage/shutter:$HOME/.shutter
      - $HOME/Pictures:$HOME/Pictures
      #- /usr/share/themes/:/usr/share/themes/:ro


  retropie:
    extends: ubuntu19.10
    build:
      context: ./dockerfiles/retropie
    image: mandy91/retropie:${DOCKER_IMAGE_VERSION}
    network_mode: host
    privileged: true
    volumes:
      - /dev:/dev
      - $HOME/Games/roms:$HOME/RetroPie/roms
      - $HOME/Games/bios_emulationstation:$HOME/RetroPie/BIOS
      - retropie-emulationstation:$HOME/.emulationstation
      - ./dockerfiles/retropie/skyscript.sh:$HOME/.skyscript.sh
      - ./dockerfiles/retropie/entrypoint.sh:/entrypoint
      - retropie-skyscraper:$HOME/.skyscraper/
      - /etc/udev/rules.d/:/etc/udev/rules.d/
    devices:
      - /dev/dri
      - /dev/shm


  polybar:
    extends: archlinux
    build:
      context: ./dockerfiles/polybar
    image: mandy91/polybar:${DOCKER_IMAGE_VERSION}
    volumes:
      - $HOME:$HOME:ro
      - /run/user/1000:/run/user/1000
    entrypoint: polybar

volumes:
  vlc:
  ssh_config:
  mobaxterm_wine:
  jupyter:
  lutris:
  mednafen:
  retroarch:
  retropie-skyscraper:
  retropie-emulationstation:
EOF