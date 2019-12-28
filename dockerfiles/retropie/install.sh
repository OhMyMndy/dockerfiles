#!/usr/bin/env bash

set -e
for var in "$@"; do
    # shellcheck disable=2086
    "$HOME/RetroPie-Setup/retropie_packages.sh" $var || exit 255
done