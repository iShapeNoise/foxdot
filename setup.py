#!/usr/bin/env python

from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

with open("FoxDot/lib/.version", "r") as f:
    version = f.read()

setup(name='FoxDot',
      version=version,
      description='Live coding music with SuperCollider',
      author='Ryan Kirkbride',
      modified_by='Jens Meisner',
      author_email='ryan@foxdot.org',
      license='cc-by-sa-4.0',
      url='http://foxdot.org/',
      packages=['FoxDot',
                'FoxDot.lib',
                'FoxDot.lib.Code',
                'FoxDot.lib.Custom',
                'FoxDot.lib.Extensions',
                'FoxDot.lib.Extensions.VRender',
                'FoxDot.lib.Extensions.SonicPi',
                'FoxDot.lib.Workspace',
                'FoxDot.lib.Workspace.img',
                'FoxDot.lib.Workspace.themes',
                'FoxDot.lib.EspGrid',
                'FoxDot.lib.Effects',
                'FoxDot.lib.Patterns',
                'FoxDot.lib.SCLang',
                'FoxDot.lib.Settings',
                'FoxDot.lib.Utils'],
      long_description=long_description,
      long_description_content_type="text/markdown",
      entry_points={'gui_scripts': ['FoxDot = FoxDot.__init__:main']},
      # data_files=[('', 'LICENSE')],
      package_data={'FoxDot': ['snd/0/*/*/*.*',
                               'snd/0/_loop_/foxdot.wav',
                               'snd/0/_loop_/drums130.wav',
                               'snd/0/_loop_/dirty120.wav',
                               'snd/0/_loop_/afro105.wav',
                               'snd/0/_loop_/break170.wav',
                               'snd/0/_loop_/cowbells110.wav',
                               'snd/0/_loop_/robot110.wav',
                               'snd/0/_loop_/techno130.wav',
                               'osc/*.scd',
                               'osc/sceffects/*.scd',
                               'osc/scsyndef/*.scd',
                               'demo/*.py',
                               'rec/.null',
                               'lib/Extensions/*/*.*',
                               'lib/Extensions/*/*/*.*',
                               'lib/.version',
                               'README.md',
                               ],
                    'FoxDot.lib.Workspace': ['img/*', 'tmp/*'],
                    'FoxDot.lib.Settings': ['conf.json']},
      install_requires=[
          'python-rtmidi',
          'soundplay',
          'python-osc',
          'textual']
      )
