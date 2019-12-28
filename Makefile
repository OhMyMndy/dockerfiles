
ifndef VERBOSE
.SILENT:
.IGNORE:
endif

include Makefile.local.mk

.PHONY: all
all:

.PHONY: clean
clean:

.PHONY: test
test:
	circleci build

build:
	docker-compose build $(service)

push:
	docker-compose push $(service)

xhost:
	xhost + local:docker


# Services
run: xhost
	docker-compose run --rm $(dargs) $(service) $(args)

chrome: xhost
	docker-compose run --rm $(dargs) chrome $(args)

firefox: xhost
	docker-compose run --rm $(dargs) firefox $(args)

vlc: xhost
	docker-compose run --rm $(dargs) vlc $(args)

dosbox: xhost
	docker-compose run --rm $(dargs) dosbox $(args)

lutris: xhost
	docker-compose run --rm $(dargs) lutris $(args)

retropie: xhost
	docker-compose run --rm $(dargs) retropie $(args)

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
