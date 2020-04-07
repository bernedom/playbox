# playbox
RFID player for raspberry pi. Using Mopidy/MPD to play back songs triggered by RFID cards


## Running the tests

```bash
pytest
```

# Hints for myself
user should be memeber of group `input` to access devices
evdev documentation
https://python-evdev.readthedocs.io/en/latest/

# Setting up VirtualEnv

It is suggested to set up a virtualenv to develop the playbox

```bash
pip3 install virtualenv
virtualenv .venv
```