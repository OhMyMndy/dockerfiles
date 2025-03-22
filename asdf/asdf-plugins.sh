#!/usr/bin/env bash

set -eu

plugins=("age" "act" "python" "flutter" "golang" "nodejs" "ruby" "rust" "terraform" "direnv")


for plugin in "${plugins[@]}"; do
  echo "Testing installation for plugin $plugin"
  asdf plugin add "$plugin"
  asdf install "$plugin" latest
  asdf set -u "$plugin" latest
  rm -rf /opt/asdf/*
done