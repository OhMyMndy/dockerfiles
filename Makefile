
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


DOCKER_COMPOSE_BIN = docker-compose-wrapper
# Services
DOCKER_RUN_CMD = $(DOCKER_COMPOSE_BIN) run --rm $(dargs) $(1) $(args)
DOCKER_EXEC_CMD = $(DOCKER_COMPOSE_BIN) exec $(dargs) $(1) $(args)
DOCKER_BUILD_CMD = $(DOCKER_COMPOSE_BIN) build $(1) $(args)

build:
	$(DOCKER_COMPOSE_BIN) build $(service)

push:
	$(DOCKER_COMPOSE_BIN) push $(service)

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
