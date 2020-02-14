#!/usr/bin/env bats
# @see https://gist.github.com/tkuchiki/041a401041530c05f73a
trap 'exit' INT EXIT

test_dockerfile() {
    local dir="$1"
    [ -d "$BATS_TEST_DIRNAME/../dockerfiles/$dir" ]
    cd "$BATS_TEST_DIRNAME/../dockerfiles/$dir"

    if [[ $docker = '' ]]; then
        docker run --privileged --rm \
            -v "${PWD}":/source \
            docker:dind bash -c "cd /source; docker build ."
    else
        run $docker build .
    fi

    

    [ $status -eq 0 ]
}

@test "Test vagrant up" {
    cd "$BATS_TEST_DIRNAME/../dockerfiles"
    find . -name 'Dockerfile' -print0 | 
        while IFS= read -r -d '' file; do
            dir="$(dirname "$file")"
            BATS_TEST_NAME="Test vagrant up $dir"
            test_dockerfile "$dir"
        done
}
