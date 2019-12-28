#!/usr/bin/env bash

if [[ $INPUT_GROUP_ID != '' ]]; then
    group_name="$(getent group $INPUT_GROUP_ID  | awk -F: '{print $1}')"
    if [[ $group_name != 'input' ]]; then
        sudo groupmod --gid 992 $(getent group $INPUT_GROUP_ID  | awk -F: '{print $1}')
    fi
    sudo groupmod --gid "$INPUT_GROUP_ID"  input
fi
if [[ $PLUGDEV_GROUP_ID != '' ]]; then
    group_name="$(getent group $PLUGDEV_GROUP_ID  | awk -F: '{print $1}')"
    if [[ $group_name != 'plugdev' ]]; then
        sudo groupmod --gid 992 $(getent group $PLUGDEV_GROUP_ID  | awk -F: '{print $1}')
    fi
    sudo groupmod --gid "$PLUGDEV_GROUP_ID" plugdev
fi


mkdir -p "$HOME/.emulationstation/all"

source "$HOME/RetroPie-Setup/scriptmodules/inifuncs.sh"
source "$HOME/RetroPie-Setup/scriptmodules/helpers.sh"
source "$HOME/RetroPie-Setup/scriptmodules/emulators/retroarch.sh"

addUdevInputRules


configdir=/opt/retropie/configs
setAutoConf "es_swap_a_b" "1"

configdir=/opt/retropie/configs
iniConfig " = " '' "$configdir/psx/emulators.cfg"
iniSet "default" "lr-beetle-psx"

iniConfig " = " '' "$configdir/psx/retroarch.cfg"
iniSet "beetle_psx_dither_mode" "\"internal resolution\""
iniSet "beetle_psx_filter" "\"bilinear\""
iniSet "beetle_psx_internal_color_depth" "\"32bpp\""
iniSet "beetle_psx_internal_resolution" "\"4x\""
iniSet "beetle_psx_renderer" "\"opengl\""
iniSet "beetle_psx_scale_dither" "\"enabled\""




iniConfig " = " '' "$configdir/all/retroarch.cfg"
iniSet "menu_swap_ok_cancel_buttons" "\"true\""



# sudo "$HOME/RetroPie-Setup/retropie_packages.sh" retroarch configure

/opt/retropie/supplementary/emulationstation/scripts/inputconfiguration.sh

# input_remapping_directory = "/opt/retropie/configs/all/retroarch-joypads"   in "/opt/retropie/configs/all/retroarch.cfg" ?



ls -lash ~/.config/retroarch/autoconfig/
exec "$@"