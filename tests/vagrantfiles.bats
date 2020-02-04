#!/usr/bin/env bats


test_vagrant() {
    local dir="$1"
    [ -d "$BATS_TEST_DIRNAME/../vagrantfiles/$dir" ]
    cd "$BATS_TEST_DIRNAME/../vagrantfiles/$dir"

    tmp_dir="$TEST_TEMP_DIR"
    
    rsync -hrtp --exclude '.vagrant' * "$tmp_dir"
    cd "$tmp_dir"

    export VAGRANT_DETECTED_OS="$(uname)"
    vagrant destroy -f
    run vagrant up
    bash -c "vagrant halt | true"

    [[ $status -eq 0 ]]
}

@test "Test vagrant up alpine-docker" {
    test_vagrant "alpine-docker"
}

@test "Test vagrant up centos-docker" {
    test_vagrant "centos-docker"
}

@test "Test vagrant up ubuntu-docker" {
    test_vagrant "ubuntu-docker"
}

setup() {
  TEST_TEMP_DIR="$(mk_temp -d)"
}

teardown() {
  rm -rf "$TEST_TEMP_DIR"
}