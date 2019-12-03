# Dockerfiles

## Setting the project up

```bash
mkdir -p ~/.teamocil
ln -s ~/src/dockerfiles/.teamocil.yml ~/.teamocil/dockerfiles.yml

teamocil dockerfiles
```

## Building

Dependent images first
`docker-compose build ubuntu19.10 ubuntu18.04 ubuntu-gaming wine`
All images
`docker-compose build`

## Checking files

```bash
git ls-files -z | grep -EZz '*Dockerfile$' 2>/dev/null | xargs -0 -r -i bash -c "[[ -f \"{}\" ]] && hadolint \"{}\""
git ls-files -z | grep -EZz '*.md*$' 2>/dev/null | xargs -0 -r -i bash -c "[[ -f \"{}\" ]] && markdownlint \"{}\""
git ls-files -z | grep -EZz '*.ya?ml*$' 2>/dev/null | xargs -0 -r -i bash -c "[[ -f \"{}\" ]] && yamllint \"{}\""
```

## Fix permissions

```bash
find . -type d -print0 | xargs -0 -r -i chmod 770 "{}"
find . -type f -print0 | xargs -0 -r -i chmod 660 "{}"
find ./dockerfiles/vpn/scripts/ -type f -print0 | xargs -0 -r -i chmod 770 "{}"
```
