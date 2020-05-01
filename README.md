# playbox
RFID player for raspberry pi. Using Mopidy/MPD to play back songs triggered by RFID cards. This is currently in very early development and should be considered a hack. There likely many security and stability issues with the code. Use at your own risk. 

# Installation

System tested on a raspberry pi 3 running a [Raspian lite](https://www.raspberrypi.org/downloads/raspbian/)

Since playbox is still under development the best way to find out needed system requirements is to look inside the [Dockerfile](Dockerfile). 

Start mopidy by using 
```bash 
systemctl enable mopidy
systemclt start mopidy
```

Until a proper python package is there pull this github repo into a folder and copy the run.py and playbox module into `/opt/`. Put the playbox.service file into `/lib/systemd/system/playbox.service` 
then reconfigure systemd

```bash
sudo systemctl daemon-reload
sudo systemctl enable playbox.service
```

# Registering audio

Matchings between RFID tag-IDs and audio URIs are stored in `/var/playbox/audio.csv` the format is 

|TagID|AudioURI|

## Running the tests

```bash
pytest
```

# Hints for myself
user should be member of group `input` to access devices
evdev documentation
https://python-evdev.readthedocs.io/en/latest/

python packaging help: https://docs.python.org/3/distutils/setupscript.html

Debian packaging intro: https://wiki.debian.org/Packaging/Intro?action=show&redirect=IntroDebianPackaging

# Setting up VirtualEnv

It is suggested to set up a virtualenv to develop the playbox

```bash
pip3 install virtualenv
virtualenv .venv
```