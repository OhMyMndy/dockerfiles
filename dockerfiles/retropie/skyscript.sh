#!/bin/bash

trap "exit" INT

declare -a systems
systems=(psx psp ps2 n64 snes nes saturn sega32x segacd wii megadrive dreamcast gb gba gb gc)
systems=(psx)
if [[ $SKYSCRAPER_USERNAME != '' ]] && [[ $SKYSCRAPER_PASSWORD != '' ]]; then
    username="-u $SKYSCRAPER_USERNAME:$SKYSCRAPER_PASSWORD"
fi

for system in "${systems[@]}"; do
    set -x
    Skyscraper -p $system --unattend -s screenscraper $username
    Skyscraper -p $system --unattend -s thegamesdb $username
    Skyscraper -p $system --unattend --relative $username
done
