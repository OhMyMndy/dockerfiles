
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
	docker-compose-wrapper build $(service)

push:
	docker-compose-wrapper push $(service)

xhost:
	xhost + local:docker


# Services
run: xhost
	docker-compose-wrapper run --rm $(dargs) $(service) $(args)

chrome: xhost
	docker-compose-wrapper run --rm $(dargs) chrome $(args)

firefox: xhost
	docker-compose-wrapper run --rm $(dargs) firefox $(args)

vlc: xhost
	docker-compose-wrapper run --rm $(dargs) vlc $(args)

vscode: xhost
	docker-compose-wrapper run --rm $(dargs) vscode $(args)
filezilla: xhost
	docker-compose-wrapper run --rm $(dargs) filezilla $(args)

dosbox: xhost
	docker-compose-wrapper run --rm $(dargs) dosbox $(args)

lutris: xhost
	docker-compose-wrapper run --rm $(dargs) lutris $(args)

retropie: xhost
	docker-compose-wrapper run --rm $(dargs) retropie $(args)


spacefm: xhost
	docker-compose-wrapper run --rm $(dargs) spacefm $(args)
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
