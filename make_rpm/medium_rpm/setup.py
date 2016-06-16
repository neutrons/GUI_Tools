from distutils.core import setup

setup(name = 'my_thread',
      scripts=['scripts/run_me'],
      version = '1.0',
      author = 'Jean Bilheux',
      packages = ['my_thread','my_thread.thread'],
      )