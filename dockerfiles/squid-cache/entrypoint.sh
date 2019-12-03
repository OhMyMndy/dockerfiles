#!/usr/bin/env bash

mkdir -p /var/cache/squid/
chmod 777 /var/cache/squid
rm /var/run/squid.pid &>/dev/null

# Create swap dirs
squid -z

rm /var/run/squid.pid &>/dev/null
exec squid -NYCd 1