#!/usr/bin/env python
import sys
import os
from distutils.core import setup

from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install

class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        print("Setting eveything up!")
        develop.run(self)

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        print("post-install command")
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