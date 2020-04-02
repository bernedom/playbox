# playbox
RFID player for raspberry pi


## Running the tests

```bash
python3 -m unittest discover ./test
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