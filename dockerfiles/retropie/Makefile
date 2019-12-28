
ifndef VERBOSE
.SILENT:
.IGNORE:
endif

retropie-init:
	cd ../.. #&& mkdir -p storage/retropie/{emulationstation,skyscraper}

retropie-build: retropie-init
	cd ../.. && docker-compose build retropie
retropie-scrape: retropie-init
	cd ../.. && docker-compose run --rm retropie $$HOME/.skyscript.sh
retropie-bash: retropie-init
	cd ../.. && docker-compose run --rm retropie bash
retropie-run: retropie-init
	cd ../.. && docker-compose run --rm retropie
retropie-list-packages: retropie-init
	cd ../.. && docker-compose run --rm retropie $$HOME/RetroPie-Setup/retropie_packages.sh


retropie-remove-volumes:
	docker volume ls | grep dockerfiles_retropie | awk '{print $$2}' | xargs -r -i docker volume rm -f {}