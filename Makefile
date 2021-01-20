
ifndef VERBOSE
.SILENT:
.IGNORE:
endif

-include Makefile.local.mk

.PHONY: all
all:

.PHONY: clean
clean:

.PHONY: test
test:
	circleci build


DOCKER_COMPOSE_BIN = /home/mandy/bin/docker-compose-wrapper
# Services
DOCKER_RUN_CMD = $(DOCKER_COMPOSE_BIN) run --rm $(dargs) $(1) $(args)
DOCKER_EXEC_CMD = $(DOCKER_COMPOSE_BIN) exec $(dargs) $(1) $(args)
DOCKER_BUILD_CMD = $(DOCKER_COMPOSE_BIN) build $(1) $(args)
DOCKER_PUSH_CMD = $(DOCKER_COMPOSE_BIN) push $(1) $(args)



build-deps:
	$(call DOCKER_BUILD_CMD, "ubuntu20.04")
	$(call DOCKER_BUILD_CMD, "ubuntu20.04-x11")
	$(call DOCKER_BUILD_CMD, "ubuntu20.04-x11-hw")
	$(call DOCKER_BUILD_CMD, "alpine")
	$(call DOCKER_BUILD_CMD, "wine")
	$(call DOCKER_BUILD_CMD, "wine5")
	
push-deps:
	$(call DOCKER_PUSH_CMD, "ubuntu20.04")
	$(call DOCKER_PUSH_CMD, "ubuntu20.04-x11")
	$(call DOCKER_PUSH_CMD, "ubuntu20.04-x11-hw")
	$(call DOCKER_PUSH_CMD, "alpine")
	$(call DOCKER_PUSH_CMD, "wine")
	$(call DOCKER_PUSH_CMD, "wine5")


push:
	$(DOCKER_COMPOSE_BIN) push $(service)

pull:
	$(DOCKER_COMPOSE_BIN) pull $(service)

xhost:
	xhost + local:docker


build: xhost
	$(call DOCKER_BUILD_CMD, $(service))


run: xhost build
	$(call DOCKER_RUN_CMD, $(service))

exec: xhost
	$(call DOCKER_EXEC_CMD, $(service))

vlc: xhost
	$(call DOCKER_RUN_CMD, vlc)

# Dev

dev-checkmake:
	$(MAKE) -C dockerfiles/dev


chromium-code-server:
	chromium-browser --app=http://localhost:8880

# Retropie

retropie-scrape:
	$(MAKE) -C dockerfiles/retropie retropie-scrape
retropie-build:
	$(MAKE) -C dockerfiles/retropie retropie-build
retropie-bash:
	$(MAKE) -C dockerfiles/retropie retropie-bash
retropie-run:
	$(MAKE) -C dockerfiles/retropie retropie-run
retropie-list-packages:
	$(MAKE) -C dockerfiles/retropie retropie-list-packages
