#!/bin/bash

trap "exit" INT

declare -a systems
systems=(psx psp ps2 n64 snes nes saturn sega32x segacd wii megadrive dreamcast gb gba gb gc)
systems=(psx)

for system in "${systems[@]}"; do
    set -x
    Skyscraper -p "$system" --unattend --relative -s screenscraper
    # Skyscraper -p "$system" --unattend --relative -s thegamesdb
    Skyscraper -p "$system" --unattend --relative
done
