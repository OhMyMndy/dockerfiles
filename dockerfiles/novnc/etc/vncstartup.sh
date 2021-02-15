#!/usr/bin/env bash

SHELL=/bin/bash
test x"$1"     = x"" && set -- default

"$SHELL" -l <<EOF
exec /etc/X11/Xsession "$@"
EOF
vncserver -kill $DISPLAY