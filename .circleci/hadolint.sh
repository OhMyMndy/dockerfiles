#!/usr/bin/env bash

set +e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR/../" || exit 1

failed=0
for file in $(git ls-files -- '*/Dockerfile')
do
  if ! hadolint  "$file"; then
    failed=1
  fi
done
exit $failed