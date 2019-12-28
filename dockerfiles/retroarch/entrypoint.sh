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



exec "$@"