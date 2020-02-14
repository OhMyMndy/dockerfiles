# Vagrant files

## Execute command in all Docker VM's

```bash
find . -maxdepth 1 -type d -iname '*-docker' -print0 | xargs -0 -r -i bash -c "echo; cd {}; echo {}; vagrant ssh --command 'docker --version; docker run --rm alpine ash -c \"ulimit -c\"'"
```
