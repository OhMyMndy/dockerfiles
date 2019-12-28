#!/usr/bin/env bash

set -e
for var in "$@"; do
    "$HOME/RetroPie-Setup/retropie_packages.sh" $var || exit 255
done