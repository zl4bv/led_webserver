#!/usr/bin/env python

import json
import subprocess
import web

render = web.template.render('html/', cache=True)

urls = (
  '/', 'index',
  '/example', 'example',
  '/irsend', 'list_devices',
  '/irsend/([\w\-_]+)', 'list_codes',
  '/irsend/([\w\-_]+)/([\w\-_]+)', 'get_code',
  '/irsend/([\w\-_]+)/([\w\-_]+)/send_once', 'send_code_once'
)

app = web.application(urls, globals())

class index:
  def GET(self):
    return render.index()

class example:
  def GET(self):
    return render.example()

class list_devices:
  def GET(self):
    return json.dumps({'devices': irsend_list()}, indent=2)

class list_codes:
  def GET(self, device):
    if device in irsend_list_devices():
      return json.dumps({'device': device, 'codes': irsend_list(device)}, indent=2)
    else:
      return web.notfound()

class get_code:
  def GET(self, device, code):
    if device in irsend_list():
      if code in irsend_list(device):
        return json.dumps({'device': device, 'code': code}, indent=2)
      else:
        return web.notfound()
    else:
      return web.notfound()

class send_code_once:
  def GET(self, device, code):
    if device in irsend_list():
      if code in irsend_list(device):
        return json.dumps(irsend_send_once(device, code), indent=2)
      else:
        return web.notfound()
    else:
      return web.notfound()

def irsend_list(device=""):
  p = subprocess.Popen('irsend LIST "%s" ""' % device, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  return map(lambda code: code.split(' ')[-1].strip(), p.stdout.readlines())

def irsend_send_once(device, code):
  p = subprocess.Popen('irsend SEND_ONCE %s %s' % (device, code), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  msg = p.stdout.read()
  status = 'success' if p.wait() == 0 else 'failure'
  return {'message': msg, 'status': status, 'device': device, 'code': code, 'directive': 'SEND_ONCE'}

if __name__ == "__main__":
  app.run()
