#!/usr/bin/env python3

import sys
import evdev
from evdev import InputDevice, ecodes, list_devices
from mpd import MPDClient

device_id = '/dev/input/event18'
device = evdev.InputDevice(device_id)
# print(device.capabilities(verbose=True))

scancodes = {
    # Scancode: ASCIICode
    0: None, 1: u'ESC', 2: u'1', 3: u'2', 4: u'3', 5: u'4', 6: u'5', 7: u'6', 8: u'7', 9: u'8',
    10: u'9', 11: u'0', 12: u'-', 13: u'=', 14: u'BKSP', 15: u'TAB', 16: u'Q', 17: u'W', 18: u'E', 19: u'R',
    20: u'T', 21: u'Y', 22: u'U', 23: u'I', 24: u'O', 25: u'P', 26: u'[', 27: u']', 28: u'CRLF', 29: u'LCTRL',
    30: u'A', 31: u'S', 32: u'D', 33: u'F', 34: u'G', 35: u'H', 36: u'J', 37: u'K', 38: u'L', 39: u';',
    40: u'"', 41: u'`', 42: u'LSHFT', 43: u'\\', 44: u'Z', 45: u'X', 46: u'C', 47: u'V', 48: u'B', 49: u'N',
    50: u'M', 51: u',', 52: u'.', 53: u'/', 54: u'RSHFT', 56: u'LALT', 100: u'RALT'
}

print("reading from RFID-reader: " + device_id)


def printMsg(message: str):
    print("MESSAGE@" + message + "@")


def playSong():
    client.add("file:///root/mount/test.MP3")
    client.next()
    client.play()
    print("Playing song")


client = MPDClient()               # create client object
# network timeout in seconds (floats allowed), default: None
client.timeout = 10
# timeout for fetching the result of the idle command is handled seperately, default: None
client.idletimeout = None
client.connect("localhost", 6600)  # connect to localhost:6600
print(client.mpd_version)          # print the MPD version


message = ""
for event in device.read_loop():

    if event.type == ecodes.EV_KEY and event.value == 1:
        cat_event = evdev.categorize(event)
        if cat_event.scancode > 1 and cat_event.scancode < 12:
            message += scancodes[cat_event.scancode]
        elif message != "":
            # printMsg(message)
            playSong()
            message = ""
