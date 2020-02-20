#!/usr/bin/env python3

import pprint
import copy

def render_service(service):
  if 'volumes' in service:
    service['volumes'] = list('{}:{}'.format(key, value) for key, value in service['volumes'].items())
  return service


def create_service(image_name: str, version: str = None, build_args: dict = None, environment: dict = {}, volumes: dict = {}, extends: dict = None) -> dict:
  if not isinstance(image_name, str):
    raise AssertionError("Name has to be a string " + type(str) + " given")
  if version is None:
    raise AssertionError("version has to be provided!")
  result = copy.deepcopy(extends)

  if extends is None:
    result = {
        "image": f"mandy91/{image_name}:{version}",
        "hostname": image_name,
        "volumes": volumes,
        "environment": environment,
        "ports": [],
        "init": True,
        "restart": 'unless-stopped'
      }

  if extends is not None:
    result['environment'] = {**result['environment'], **environment}
    result['volumes'] = {**result['volumes'], **volumes}
    result['image'] =  f"mandy91/{image_name}:{version}"
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
      result['build']["context"] = f"./dockerfiles/{image_name}"


  elif 'build' not in result and build_args is not None:
      result["build"] = {
          "context": f"./dockerfiles/{image_name}",
          "args": dict(build_args)
      }

  return result
  