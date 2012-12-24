#!/usr/bin/env python

from   appscript import *
import os
import subprocess
import time
import tornado.autoreload
import tornado.ioloop
import tornado.web

# Change if necessary
PORT = 1223


class Application(tornado.web.Application):
  def __init__(self):
    handlers = [
      (r'/', MainHandler)
    ]

    settings = {
      'static_path': os.path.join(os.path.dirname(__file__), 'static'),
      'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
      'debug': True
    }

    tornado.web.Application.__init__(self, handlers, **settings)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
      # Template
      d = time.strftime('%Y-%m-%d %I:%M:%S %p')
      self.render('main.html', d=d)


    def post(self):
      ev = app("Evernote")
      es = app("ExactScan Pro")

      ### First, lets scan...
      # ExactScan doesn't work well w/ py-appscript *sigh*

      # side - can only be set by switching profile
      # 10: duplex, 11: front, 12: back
      side = self.get_argument('side', None)
      if side == 'duplex':
        subprocess.call(['osascript', '-e', 'tell application "ExactScan Pro"', '-e', 'set profile to 10', '-e', 'end tell'])
      elif side == 'back':
        subprocess.call(['osascript', '-e', 'tell application "ExactScan Pro"', '-e', 'set profile to 12', '-e', 'end tell'])
      else:
        subprocess.call(['osascript', '-e', 'tell application "ExactScan Pro"', '-e', 'set profile to 11', '-e', 'end tell'])

      # dpi
      dpi = self.get_argument('dpi', '300')
      subprocess.call(['osascript', '-e', 'tell application "ExactScan Pro"', '-e', 'set resolution to %s' % dpi, '-e', 'end tell'])

      # type - Color, Gray, Lineart
      type = self.get_argument('type', 'Color')
      subprocess.call(['osascript', '-e', 'tell application "ExactScan Pro"', '-e', 'set document type to "%s"' % type, '-e', 'end tell'])

      # scan!
      es.scan()


      ### Post to Evernote
      title = self.get_argument('title', time.strftime('%Y-%m-%d %I:%M:%S %p'))
      notebook = 'scan._inbox'
      body = self.get_argument('body', '')
      from_file = '/tmp/scan.pdf'

      ev.create_note(title=title, notebook=notebook, with_text=body, attachments=from_file)

      # run
      self.write('ok')
     

if __name__ == '__main__':
  try:
    Application().listen(PORT)
    ioloop = tornado.ioloop.IOLoop.instance()
    tornado.autoreload.start(io_loop=ioloop)

    c = app('Google Chrome')
    w = c.make(new='cwin')
    t = w.active_tab()
    t.URL.set('http://localhost:%s/' % PORT)

    ioloop.start()

  except:
    c = app('Google Chrome')
    w = c.make(new='cwin')
    t = w.active_tab()
    t.URL.set('http://localhost:%s/' % PORT)
