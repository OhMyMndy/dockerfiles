#!/usr/bin/python3

import yaml
import os
import grp
import pwd
import pprint
import copy
from collections.abc import Collection
from collections import defaultdict

import sys
from os.path import dirname

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from docker_compose_helper import create_service, render_service, global_volumes, x11_volumes

pp = pprint.PrettyPrinter(indent=4)

uid = os.getuid()
gid = os.getgid()
docker_gid = grp.getgrnam('docker').gr_gid
home = os.path.expanduser("~")
user = pwd.getpwuid(os.getuid())[0]

docker_image_version = 0.1


x11_environment = {
  "DISPLAY": os.environ['DISPLAY']
}

default_build_args = {
   "DOCKER_IMAGE_VERSION": f"{docker_image_version}",
   "UBUNTU19_10": f"{docker_image_version}-19.10",
   "UBUNTU18_04": f"{docker_image_version}-18.04",
   "USER": f"{user}",
   "PUID": f"{uid}",
   "PGID": f"{gid}"
}

ubuntu1804 = create_service(
  image_name='ubuntu',
  version=f'{docker_image_version}-18.04',
  build_args={**default_build_args, **{"VERSION": "18.04"}},
  environment={**default_build_args, **{"VERSION": "18.04"}},
  volumes=global_volumes
)

gitlab = create_service(
  image_name='gitlab',
  version=f'{docker_image_version}',
  extends=ubuntu1804,
  volumes={
    "./storage/gitlab/config": "/etc/gitlab",
    "./storage/gitlab/logs": "/var/log/gitlab",
    "./storage/gitlab/data": "/var/opt/gitlab",
    }
)
gitlab['ports'] = [
  "8880:80",
  "2222:22"
]

ubuntu1804_x11 = create_service(
  image_name='ubuntu-x11',
  version=f'{docker_image_version}-18.04',
  environment=x11_environment,
  volumes=x11_volumes,
  extends=ubuntu1804
)
ubuntu1804_x11['devices'] = ['/dev/dri']

ubuntu1804_x11_hw = create_service(
  image_name='ubuntu-x11-hw',
  version=f'{docker_image_version}-18.04',
  extends=ubuntu1804_x11
)

ubuntu1910 = create_service(
  image_name='ubuntu',
  version=f'{docker_image_version}-19.10',
  build_args={"VERSION": "19.10"},
  environment={"VERSION": "19.10"},
  extends=ubuntu1804
)


ubuntu1910_x11 = create_service(
  image_name='ubuntu-x11',
  version=f'{docker_image_version}-19.10',
  environment=x11_environment,
  volumes=x11_volumes,
  extends=ubuntu1910
)
ubuntu1910_x11['devices'] = ['/dev/dri']
ubuntu1910_x11_hw = create_service(
  image_name='ubuntu-x11-hw',
  version=f'{docker_image_version}-19.10',
  extends=ubuntu1910_x11
)


wine = create_service(
  image_name='wine',
  version=f'{docker_image_version}',
  extends=ubuntu1910_x11
)

wine5 = create_service(
  image_name='wine5',
  version=f'{docker_image_version}',
  extends=ubuntu1910_x11,
  environment={
    "QT_X11_NO_MITSHM": 1
  }
)


mobaxterm = create_service(
  image_name='mobaxterm',
  version=f'{docker_image_version}',
  extends=ubuntu1910_x11_hw
)

firefox_volumes = {
      "./storage/firefox": f"{home}/.mozilla",
      f"{home}/Downloads": f"{home}/Downloads"
}
firefox = create_service(
  image_name='firefox',
  version=f'{docker_image_version}',
  volumes=firefox_volumes, 
  extends=ubuntu1910_x11_hw
)
firefox['network_mode'] = 'service:vpn'

filezilla = create_service(
  image_name='filezilla',
  version=f'{docker_image_version}',
  extends=ubuntu1910_x11_hw
)

dosbox_volumes = {
      "./storage/dosbox": f"{home}/.config/dosbox",
}
dosbox = create_service(
  image_name='dosbox',
  version=f'{docker_image_version}',
  extends=ubuntu1910_x11_hw,
  volumes=dosbox_volumes
)
chrome_volumes = {
      "./storage/chrome": f"/data",
      f"{home}/Downloads": f"{home}/Downloads"
}
chrome = create_service(
  image_name='chrome',
  version=f'{docker_image_version}',
  volumes=chrome_volumes, 
  extends=ubuntu1910_x11_hw
)
chrome['network_mode'] = 'service:vpn'
chrome['security_opt'] = [ "seccomp=./seccomp/chrome.json" ]

vlc = create_service(
  image_name='vlc',
  version=f'{docker_image_version}',
  environment=x11_environment,
  volumes=x11_volumes,
  extends=ubuntu1910_x11_hw
)


quicktile = create_service(
  image_name='quicktile',
  version=f'{docker_image_version}',
  volumes={
    f"{home}/.config/quiocktile.cfg": f"{home}/.config/quiocktile.cfg"
  },
  extends=ubuntu1910_x11)

bitwarden = create_service(
  image_name='bitwarden',
  version=f'{docker_image_version}',
  extends=ubuntu1804_x11_hw,
  volumes={
    "./storage/bitwarden": f"{home}/.config/Bitwarden"
  }
)
bitwarden['network_mode'] = 'service:vpn'



nomachine = create_service(
  image_name='nomachine',
  version=f'{docker_image_version}',
  extends=ubuntu1910_x11_hw,
  volumes={
    "./storage/ssh": f"{home}/.ssh",
    f"{home}/Downloads": f"{home}/Downloads",
    "./storage/nomachine-configs": f"{home}/.nx",
    "./storage/nomachine": f"{home}/NoMachine"
  }
)
nomachine['network_mode'] = 'service:vpn'


vpn = create_service(
  image_name='vpn',
  version=f'{docker_image_version}',
  volumes={ "./etc/openvpn": "/etc/openvpn",
         "./storage/ssh": f"{home}/.ssh"},
  extends=ubuntu1910
)
vpn['privileged'] = True
vpn['command'] = 'sleep infinity'

crafty = create_service(
  image_name='crafty',
  version=f'{docker_image_version}',
    volumes={
    "./storage/crafty/db": f"/crafty_db",
    "./storage/crafty/certs": f"{home}/crafty/crafty-web/app/web/certs"
  },
  extends=ubuntu1910
)
crafty['ports'] = [
  "8000:8000",
  "25565:25565"
]
crafty["deploy"] = {
  "resources": {
    "limits": {
      "memory": "2400m",
      "cpus": "1.4"
    }
  }
}

alpine = create_service(
  image_name='alpine',
  version=f'{docker_image_version}',
  build_args=default_build_args
)

tmux = create_service(
  image_name='tmux',
  version=f'{docker_image_version}',
  extends=alpine
)

code_server = create_service(
  image_name='code-server',
  version=f'{docker_image_version}',
  extends=ubuntu1804,
  volumes={
    "./storage/code-server": "/home/coder/.local/share/code-server-host",
    f"{home}/src" : "/home/coder/src",
    f"{home}/.ssh" : "/home/coder/.ssh",
    f"{home}/dotfiles" : "/home/coder/dotfiles"
  }
)
code_server['ports'] = ['8880:8080']


mkdocs = create_service(
  image_name='mkdocs',
  version=f'{docker_image_version}',
  extends=ubuntu1910,
  volumes={"./storage/mkdocs": f"{home}/mkdocs"}
)
mkdocs['ports'] = ['8080:8000']

docker_compose = {
  "version": "3.7",
  "services": {
    "ubuntu18.04": render_service(ubuntu1804),
    "ubuntu18.04-x11": render_service(ubuntu1804_x11),
    "ubuntu18.04-x11-hw": render_service(ubuntu1804_x11_hw),
    "ubuntu19.10": render_service(ubuntu1910),
    "ubuntu19.10-x11": render_service(ubuntu1910_x11),
    "ubuntu19.10-x11-hw": render_service(ubuntu1910_x11_hw),
    "alpine": render_service(alpine),
    "vlc": render_service(vlc),
    "vpn": render_service(vpn),
    "firefox": render_service(firefox),
    "filezilla": render_service(filezilla),
    "chrome": render_service(chrome),
    "bitwarden": render_service(bitwarden),
    "mkdocs": render_service(mkdocs),
    "tmux": render_service(tmux),
    "nomachine": render_service(nomachine),
    "code-server": render_service(code_server),
    "gitlab": render_service(gitlab),
    "wine": render_service(wine),
    "wine5": render_service(wine5),
    "mobaxterm": render_service(mobaxterm),
    "dosbox": render_service(dosbox),
    "quicktile": render_service(quicktile),
    "crafty": render_service(crafty),
  },
  "networks": {
    "default": {}
  }
}


print(yaml.dump(docker_compose))