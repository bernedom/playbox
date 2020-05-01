#!/usr/bin/env python3

from setuptools import setup

__author__ = 'Dominik Berner'

setup(
    name='playbox',
    version='0.0.1-alpha',
    description='RFID player for raspberry pi. Using Mopidy/MPD to play back songs triggered by RFID cards.',
    author='Dominik Berner',
    author_email='dominik.berner@gmail.com',
    license='GNU',
    url='https: // github.com/bernedom/playbox',
    packages=['playbox'],
    entry_points={'console_scripts': ['tvb=tvb:main']},
    scripts=['run.py']
)
