#!/usr/bin/env python

from distutils.core import setup

setup(name='corow',
      packages=['corow'],
      version='0.1',
      scripts=['bin/cl_corow.py', 'bin/tk_corow.py', 'bin/tk_tablediff.py']
      )
