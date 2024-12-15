#!/usr/bin/env bash

insync-headless config allow_analytics 0

insync-headless start --no-daemon

# For logging in, go to: https://connect.insynchq.com/auth
# then execute: insync-headless account add --cloud gd --path ~/backups/ --auth-code <the-auth-code>
#
# Select folders to sync: insync-headless selective-sync
