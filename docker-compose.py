#!/usr/bin/python3

import yaml
import os
import grp
import pwd
import pprint
import copy
from collections import Collection
from collections import defaultdict

import sys
from os.path import dirname

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from docker_compose_helper import create_service, render_service

pp = pprint.PrettyPrinter(indent=4)

uid = os.getuid()
gid = os.getgid()
docker_gid = grp.getgrnam('docker').gr_gid
home = os.path.expanduser("~")
user = pwd.getpwuid(os.getuid())[0]

docker_image_version = 0.1

global_volumes = {
  "/var/lib/lxcfs/proc/cpuinfo": "/proc/cpuinfo:rw",
  "/var/lib/lxcfs/proc/diskstats": "/proc/diskstats:rw",
  "/var/lib/lxcfs/proc/meminfo": "/proc/meminfo:rw", 
  "/var/lib/lxcfs/proc/stat": "/proc/stat:rw",
  "/var/lib/lxcfs/proc/swaps": "/proc/swaps:rw",
  "/var/lib/lxcfs/proc/uptime": "/proc/uptime:rw",
  "/etc/timezone": "/etc/timezone:ro",
  "/etc/localtime": "/etc/localtime:ro",
  # "./dockerfiles/ubuntu/root/etc/cron.d": "/etc/cron.d:ro",
  "/dev/shm": "/dev/shm",
  "/etc/machine-id": "/etc/machine-id:ro",
}

global_volumes = {k:v for k,v in global_volumes.items() if os.path.isfile(k) or os.path.isdir(k)}


x11_volumes = {
    "/tmp/.X11-unix": "/tmp/.X11-unix",
    f"/run/user/{uid}/pulse": "/run/user/1000/pulse",
    "./etc/pulse/pulse-client.conf": "/etc/pulse/client.conf:ro",
    f"{home}/.config/fontconfig": "/root/.config/fontconfig:ro",
    f"{home}/.config/fontconfig": f"{home}/.config/fontconfig:ro",
    f"{home}/.config/gtk-2.0": f"{home}/.config/gtk-2.0:ro",
    f"{home}/.config/gtk-3.0": f"{home}/.config/gtk-3.0:ro",
    f"{home}/.Xresources": f"{home}/.Xresources",
    "./etc/ssl/certificates": "/etc/ssl/certificates:ro",
    "/usr/share/fonts": "/usr/share/fonts:ro",
    "/usr/share/themes": "/usr/share/themes:ro",
    "/usr/share/icons": "/usr/share/icons:ro",
    "/usr/share/fontconfig": "/usr/share/fontconfig:ro",
    f"{home}/.local/share/fonts": f"{home}/.local/share/fonts:ro",
}
x11_volumes = {k:v for k,v in x11_volumes.items() if os.path.isfile(k) or os.path.isdir(k)}


x11_environment = {
  "DISPLAY": os.environ['DISPLAY']
}

default_build_args = {
   "DOCKER_IMAGE_VERSION": f"{docker_image_version}",
   "UBUNTU19_10": f"{docker_image_version}-19.10",
   "UBUNTU18_04": f"{docker_image_version}-18.04",
   "USER": f"{user}",
}

ubuntu1804 = create_service(
  image_name='ubuntu',
  version=f'{docker_image_version}-18.04',
  build_args={**default_build_args, **{"VERSION": "18.04"}},
  environment={**default_build_args, **{"VERSION": "18.04"}},
  volumes=global_volumes
)

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

bitwarden = create_service(
  image_name='bitwarden',
  version=f'{docker_image_version}',
  extends=ubuntu1804_x11_hw
)
bitwarden['network_mode'] = 'service:vpn'


vpn = create_service(
  image_name='vpn',
  version=f'{docker_image_version}',
  volumes={ "./etc/openvpn": "/etc/openvpn",
         "./storage/ssh": f"{home}/.ssh"},
  extends=ubuntu1910
)
vpn['privileged'] = True
vpn['command'] = 'sleep infinity'

alpine = create_service(
  image_name='alpine',
  version=f'{docker_image_version}',
  build_args={}
)

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
    "chrome": render_service(chrome),
    "bitwarden": render_service(bitwarden),
    "mkdocs": render_service(mkdocs)
  },
  "networks": {
    "default": {}
  }
}


print(yaml.dump(docker_compose))