#!/usr/bin/env python

import sys
import os
from distutils.core import setup

from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install
from utils import Init, w
from datetime import datetime


def write_ts_now(key):
    with open(key + ".ts", "w") as f:
        f.write(datetime.now().isoformat())

def _setup():
    # Init()
    pass

class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        print("post-develop command")
        write_ts_now("develop")
        w("Setting eveything up!", "a")
        develop.run(self)

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        print("post-install command")
        write_ts_now("install")
        install.run(self)

setup(name='img2banner',
      version='1.3',
      description='Use an image as banner',
      author='Better Fork Inc',
      author_email='betterfork@protonmail.com',
      url='https://github.com/betterfork/img2banner',
      packages=['img2banner'],
      cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,
      }
     )
