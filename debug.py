from datetime import datetime
import random
import os
import re

colors = ['31', '32', '33', '34', '35', '36']
gray = '\033[37m'

env = os.getenv('DEBUG')


def noop(*args):
  return


def Debug(name):
  if env is None:
    return noop

  escaped_env = re.escape(env)
  escaped_env = escaped_env.replace('\\*', '.*?')
  escaped_env = escaped_env.replace(',', '|')
  pattern = re.compile('^(' + escaped_env + ')$')

  if not pattern.match(name):
    return noop

  color = '\033[' + colors[random.randint(0, len(colors) - 1)] + 'm'

  def debug(format, *args):
    print(gray + now() + color + name + ' ' + format % args)

  return debug


def now():
  t = datetime.now()
  return str(t.hour) + ':' + str(t.minute) + ':' + str(t.second) + ' ' + str(
      int(t.microsecond / 1000)) + 'ms '
