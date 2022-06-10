#!/usr/bin/env bash
set -ex

apt-get update
apt-get install -y software-properties-common sudo

curl -sL https://raw.githubusercontent.com/wimpysworld/deb-get/main/deb-get | sudo -E bash -s install deb-get
deb-get install obsidian

# Default settings and desktop icon
# cp /usr/share/applications/org.inkscape.Inkscape.desktop $HOME/Desktop/
# chmod +x $HOME/Desktop/org.inkscape.Inkscape.desktop