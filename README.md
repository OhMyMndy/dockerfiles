# Dockerfiles

## Kasm

## Insync

```bash
mkdir -p ~/.config/Insync-headless ~/Insync-headless-storage
podman run --rm --name insync-backups -d -it \
  -v ~/.config/Insync-headless:/home/ubuntu/.config/Insync-headless:Z \
  -v ~/Insync-headless-storage:/home/ubuntu/backups:Z \
  --userns=keep-id:uid=1000 ohmymndy/insync:latest

# To run a SMB server with the correct permissions:
podman run -it --name insync-backups-smb \
  -d --rm -p 1445:445 \
  -e "USER=samba" -e "PASS=secret" \
  -v ~/Insync-headless-storage/:/storage:z \
  --uidmap=1000:0:1 --uidmap=0:1:1000 dockurr/samba
```

## Virter

```bash
docker run -d --name virter --rm -it --privileged --device /dev/kvm docker.io/ohmymndy/virter

docker exec -it -u virter virter bash
```

Then in the container:

```bash
virter image pull alma-9
virter vm run alma-9 --name alma-9 --id 3
# wait for the VM to boot
sleep 30
virter vm ssh alma-9
```
