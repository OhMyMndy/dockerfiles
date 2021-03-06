#!/usr/bin/env python3

import pprint
import copy
import os
import pwd
import grp
import subprocess
import yaml
try:
  uid = os.environ['UID']
except:
  uid = os.getuid()

try:
  gid = os.environ['GID'] # os.getgid()
except:
  gid = os.getgid()

try:
  docker_gid = grp.getgrnam('docker').gr_gid
except:
  docker_gid = 0
  
try:
  input_gid = grp.getgrnam('input').gr_gid
except:
  input_gid = 0
try:
  plugdev_gid = grp.getgrnam('plugdev').gr_gid
except:
  plugdev_gid = 0

try:  
  home = os.environ['HOME']
except:
  home = "/home/mandy"
try:
  user = os.environ['USER']
except:
  user = "mandy"



x11_environment = {
  "DOCKER_GID": docker_gid,
  "INPUT_GROUP_ID": input_gid,
  "PLUGDEV_GROUP_ID": plugdev_gid
}

if 'DISPLAY' in os.environ:
  x11_environment["DISPLAY"] = os.environ['DISPLAY']

default_build_args = {
   "USER": f"{user}",
   "PUID": f"{uid}",
   "PGID": f"{gid}"
}



def docker_network_exists(network_name):
  out = subprocess.Popen(['docker', 'network', 'ls', '--format', '{{.Name}}'], 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)
  stdout,stderr = out.communicate()
  
  return network_name in stdout.decode("utf-8").split()


def render_config(config):
  if 'networks' in config:
    networks = config['networks'].copy().items()
    for key, network in networks:
      if 'external' in network and 'name' in network['external'] and not docker_network_exists(network['external']['name']):
        del config['networks'][key]['external']
  return yaml.dump(config)

def render_service(service):
  if 'volumes' in service:
    service['volumes'] = list('{}:{}'.format(key, value) for key, value in service['volumes'].items())
    
  if 'network_mode' in service:
    del service['hostname']
      
  return service


def create_service(image_name: str, version: str = None, build_args: dict = None, environment: dict = {}, volumes: dict = {}, extends: dict = None, devices: list = None) -> dict:
  cwd = os.getcwd()
  if not isinstance(image_name, str):
    raise AssertionError("Name has to be a string " + type(str) + " given")
  if version is None:
    raise AssertionError("version has to be provided!")
  result = copy.deepcopy(extends)

  if isinstance(build_args, dict):
    environment.update(build_args)

  if extends is None:
    result = {
        "image": f"ohmymndy/{image_name}:{version}",
        "hostname": image_name,
        "volumes": volumes,
        "environment": environment,
        "ports": [],
        "init": True,
        "restart": 'unless-stopped',
        "devices": []
      }

  if extends is not None:
    result['environment'] = {**result['environment'], **environment}
    result['volumes'] = {**result['volumes'], **volumes}
    result['image'] =  f"ohmymndy/{image_name}:{version}"
    result['hostname'] = image_name
    if build_args and 'build' not in result:
      result['build'] = {
        'args': {}
      }
    
    if 'build' in result:
      if build_args:
        args = result['build']['args'].copy()
        args.update(build_args)
        result['build']["args"] = args
      result['build']["context"] = f"{cwd}/dockerfiles/"
      result['build']["dockerfile"] = f"{cwd}//dockerfiles/{image_name}/Dockerfile"


  elif 'build' not in result and build_args is not None:
      result["build"] = {
          "context": f"{cwd}/dockerfiles/",
          "dockerfile": f"{cwd}/dockerfiles/{image_name}/Dockerfile",
          "args": dict(build_args)
      }

  if isinstance(devices, list):
    result['devices'] = list(set(devices + result['devices']))

  return result
  
  

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

# global_volumes = {k:v for k,v in global_volumes.items() if os.path.isfile(k) or os.path.isdir(k)}




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
    # "/usr/share/fonts": "/usr/share/fonts:ro",
    # "/usr/share/themes": "/usr/share/themes:ro",
    # "/usr/share/icons": "/usr/share/icons:ro",
    # "/usr/share/fontconfig": "/usr/share/fontconfig:ro",
    f"{home}/.local/share/fonts": f"{home}/.local/share/fonts:ro",
}
x11_volumes = {k:v for k,v in x11_volumes.items() if os.path.isfile(k) or os.path.isdir(k)}
