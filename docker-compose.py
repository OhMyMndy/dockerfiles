#!/usr/bin/python3

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

from docker_compose_helper import x11_environment, default_build_args, create_service, render_service, global_volumes, x11_volumes, render_config
from docker_compose_helper import uid, gid, docker_gid, input_gid, plugdev_gid, home, user

#pp = pprint.PrettyPrinter(indent=4)


docker_image_version = 0.1

default_build_args.update({
   "DOCKER_IMAGE_VERSION": f"{docker_image_version}",
   "UBUNTU19_10": f"{docker_image_version}-19.10",
   "UBUNTU18_04": f"{docker_image_version}-18.04",
   "UBUNTU20_04": f"{docker_image_version}-20.04",
})


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
  extends=ubuntu1804,
  devices= ['/dev/dri'],
)

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
  extends=ubuntu1910,
  devices= ['/dev/dri']
)

ubuntu1910_x11_hw = create_service(
  image_name='ubuntu-x11-hw',
  version=f'{docker_image_version}-19.10',
  extends=ubuntu1910_x11
)



ubuntu2004 = create_service(
  image_name='ubuntu',
  version=f'{docker_image_version}-20.04',
  build_args={"VERSION": "20.04"},
  environment={"VERSION": "20.04"},
  extends=ubuntu1804
)


ubuntu2004_x11 = create_service(
  image_name='ubuntu-x11',
  version=f'{docker_image_version}-20.04',
  environment=x11_environment,
  volumes=x11_volumes,
  extends=ubuntu2004,
  devices= ['/dev/dri']
)

ubuntu2004_x11_hw = create_service(
  image_name='ubuntu-x11-hw',
  version=f'{docker_image_version}-20.04',
  extends=ubuntu2004_x11

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

filezilla_volumes = {
      "./storage/filezilla": f"{home}/.config/filezilla",
      "./storage/ssh": f"{home}/.ssh",
      f"{home}/Downloads": f"{home}/Downloads"
}
filezilla = create_service(
  image_name='filezilla',
  version=f'{docker_image_version}',
  volumes=filezilla_volumes, 
  extends=ubuntu1910_x11_hw
)
filezilla['network_mode'] = 'service:vpn'

system_tools_volumes = {
  "./storage/ssh": f"{home}/.ssh",
  f"{home}/Downloads": f"{home}/Downloads"
}
system_tools = create_service(
  image_name='system-tools',
  version=f'{docker_image_version}',
  volumes=system_tools_volumes,
  extends=ubuntu1910_x11_hw
)
system_tools['network_mode'] = 'service:vpn'


dosbox_volumes = {
      "./storage/dosbox": f"{home}/.config/dosbox",
}
dosbox = create_service(
  image_name='dosbox',
  version=f'{docker_image_version}',
  extends=ubuntu1910_x11_hw,
  volumes=dosbox_volumes
)


retropie_volumes = {
      "/run/udev/control": "/run/udev/control",
      "/dev/bus/usb": "/dev/bus/usb",
      # "/dev/serial": "/dev/serial",
      "/dev/input": "/dev/input",
      "./storage/retropie/emulationstation": f"{home}/.emulationstation",
      "./storage/retropie/skyscraper": f"{home}/.skyscraper",
      "./dockerfiles/retropie/entrypoint.sh": "/entrypoint",
      "./dockerfiles/retropie/skyscript.sh": f"{home}/.skyscript.sh",
      "/tank/media/games/retropie/roms": f"{home}/RetroPie/roms",
      "/tank/media/games/retropie/bios": f"{home}/RetroPie/BIOS"
}

retropie = create_service(
  image_name='retropie',
  version=f'{docker_image_version}',
  extends=ubuntu1910_x11_hw,
  volumes=retropie_volumes,
  devices=[
    "/dev/dri",
    "/dev/shm"
  ]
)
retropie['network_mode'] = 'host'
retropie['privileged'] = True




retroarch_volumes = {
      "/run/udev/control": "/run/udev/control",
      "/dev/bus/usb": "/dev/bus/usb",
      "/dev/input": "/dev/input",
      "/tank/media/games/retropie/roms": f"{home}/roms",
      "/tank/media/games/retropie/bios": f"{home}/BIOS",
      "./storage/retroarch": f"{home}/.config/retroarch",

}

retroarch = create_service(
  image_name='retroarch',
  version=f'{docker_image_version}',
  extends=ubuntu1910_x11_hw,
  volumes=retroarch_volumes,
  devices=[
    "/dev/dri",
    "/dev/shm"
  ]
)
retroarch['network_mode'] = 'host'
retroarch['privileged'] = True


php_volumes = {
}
php = create_service(
  image_name='php',
  version=f'{docker_image_version}',
  extends=ubuntu1910_x11,
  volumes=php_volumes
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


upsource = create_service(
  image_name='jetbrains/upsource:2019.1.1644',
  version=f'{docker_image_version}',
  volumes={
    f"{home}/.upsource/data": "/opt/upsource/data",
    f"{home}/.upsource/conf": "/opt/upsource/conf",
    f"{home}/.upsource/logs": "/opt/upsource/logs",
    f"{home}/.upsource/backups": "/opt/upsource/backups",
  },
  extends=ubuntu2004
)
upsource['image'] = 'jetbrains/upsource:2019.1.1644'
upsource['ports'] = ["8089:8080"]
upsource["deploy"] = {
  "resources": {
    "limits": {
      "memory": "8100m",
      "cpus": "1.4"
    }
  }
}


bitwarden = create_service(
  image_name='bitwarden',
  version=f'{docker_image_version}',
  extends=ubuntu1804_x11_hw,
  volumes={
    "./storage/bitwarden": f"{home}/.config/Bitwarden"
  }
)
bitwarden['network_mode'] = 'service:vpn'


jackaudio = create_service(
  image_name='jackaudio',
  version=f'{docker_image_version}',
  extends=ubuntu1804_x11_hw,
)



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


quod_libet = create_service(
  image_name='quod-libet',
  version=f'{docker_image_version}',
  extends=ubuntu1910,
  volumes={
    # "./storage/ssh": f"{home}/.ssh",
    # f"{home}/Downloads": f"{home}/Downloads",
    # "./storage/nomachine-configs": f"{home}/.nx",
    # "./storage/nomachine": f"{home}/NoMachine"
  }
)
quod_libet['ports'] = [
  "4444:4000"
]



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
    "./storage/crafty/certs": f"{home}/crafty/crafty-web/app/web/certs",
    "./storage/crafty/minecraft": f"{home}/Minecraft"
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
  extends=ubuntu2004,
  volumes={
    "./storage/code-server": "/home/coder/.local/share/code-server-host",
    f"{home}/src" : "/home/coder/src",
    f"{home}/.ssh" : "/home/coder/.ssh",
    f"{home}/dotfiles" : "/home/coder/dotfiles"
  },
  environment= {
    "USER": 'coder',
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

# docker run -it --privileged --network host -v  /var/run/docker.sock:/var/run/docker.sock:ro --pid host --rm vimagick/glances

glances = create_service(
  image_name='glances',
  version=f'{docker_image_version}',
  extends=alpine,
  volumes={
    "/var/run/docker.sock": f"/var/run/docker.sock:ro"
  }
)
glances['pid'] = 'host'
glances['network_mode'] = 'host'
glances['privileged'] = True


tiddlywiki = create_service(
  image_name='tiddlywiki',
  version=f'{docker_image_version}',
  extends=alpine,
  volumes={
    "./storage/tiddlywiki": f"/data"
  }
)
tiddlywiki['ports'] = ["8090:8080"]

jupyter = create_service(
  image_name='jupyter',
  version=f'{docker_image_version}',
  extends=ubuntu2004,
  volumes={
    "./storage/jupyter": f"{home}/.jupyter",
    f"{home}/Downloads": f"{home}/Downloads",
    f"{home}/Documents/Docs": f"{home}/docs"
  }
)
jupyter['ports'] = ['8888:8888']
jupyter['networks'] = ['default', 'webdev']


jupyter_dind = create_service(
  image_name='jupyter-dind',
  version=f'{docker_image_version}',
  extends=ubuntu2004,
  # volumes={
  #   "./storage/jupyter": f"{home}/.jupyter",
  #   f"{home}/Downloads": f"{home}/Downloads",
  #   f"{home}/Documents/Docs": f"{home}/docs"
  # }
)
jupyter['ports'] = ['8888:8888']
jupyter['networks'] = ['default', 'webdev']


rclone_browser_volumes = {
      f"{home}/.config/rclone": f"{home}/.config/rclone",
      # f"{home}/.config/rclone-browser": f"{home}/.config/rclone-browser",
      "./storage/rclone-browser": f"{home}/.config/rclone-browser",
}
rclone_browser = create_service(
  image_name='rclone-browser',
  version=f'{docker_image_version}',
  extends=ubuntu1910_x11,
  volumes=rclone_browser_volumes
)


docker_compose = {
  "version": "3.7",
  "services": {
    "ubuntu18.04": render_service(ubuntu1804),
    "ubuntu18.04-x11": render_service(ubuntu1804_x11),
    "ubuntu18.04-x11-hw": render_service(ubuntu1804_x11_hw),
    "ubuntu19.10": render_service(ubuntu1910),
    "ubuntu19.10-x11": render_service(ubuntu1910_x11),
    "ubuntu19.10-x11-hw": render_service(ubuntu1910_x11_hw),
    "ubuntu20.04": render_service(ubuntu2004),
    "ubuntu20.04-x11": render_service(ubuntu2004_x11),
    "ubuntu20.04-x11-hw": render_service(ubuntu2004_x11_hw),
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
    "php": render_service(php),
    "jackaudio": render_service(jackaudio),
    "quod-libet": render_service(quod_libet),
    "retropie": render_service(retropie),
    "retroarch": render_service(retroarch),
    "system-tools": render_service(system_tools),
    "jupyter": render_service(jupyter),
    "jupyter-dind": render_service(jupyter_dind),
    "rclone-browser": render_service(rclone_browser),
    "upsource": render_service(upsource),
    "glances": render_service(glances),
    "tiddlywiki": render_service(tiddlywiki),
  },
  "networks": {
    "default": {},
    "webdev": {
      "external": {
        "name": "webdev_default"
      }
    }
  }
}

print(render_config(docker_compose))
