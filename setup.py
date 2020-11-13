#!/usr/bin/env python3

from setuptools import setup

__author__ = 'Dominik Berner'

setup(
    name='playbox',
    version='0.1.3',
    description='RFID player for raspberry pi. Using Mopidy/MPD to play back songs triggered by RFID cards.',
    author='Dominik Berner',
    author_email='dominik.berner@gmail.com',
    license='GPLv3',
    url='https: // github.com/bernedom/playbox',
    packages=['playbox'],
    entry_points={'console_scripts': ['playbox=playbox.command_line:main']},

    data_files=[('/var/playbox/', ['resource/ready.mp3'])]


)
