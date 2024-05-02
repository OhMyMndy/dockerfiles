build:
    docker compose build

push:
    docker compose push

up:
    docker compose up -d

logs:
    docker compose logs -f --tail 100