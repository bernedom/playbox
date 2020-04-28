# playbox
RFID player for raspberry pi. Using Mopidy/MPD to play back songs triggered by RFID cards

# Installation

System tested on a raspberry pi 3 running a [Raspian lite](https://www.raspberrypi.org/downloads/raspbian/)

Since playbox is still under development the best way to find out needed system requirements is to look inside the [Dockerfile](Dockerfile). 

Start mopidy by using 
```bash 
systemctl enable mopidy
systemclt start mopidy
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

# Setting up VirtualEnv

It is suggested to set up a virtualenv to develop the playbox

```bash
pip3 install virtualenv
virtualenv .venv
```