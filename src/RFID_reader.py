#!/usr/bin/env python3

import sys
import evdev
from evdev import InputDevice, ecodes, list_devices


def get_devices():
    return [InputDevice(fn) for fn in list_devices()]


print(get_devices())

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
    print(device.path, device.name, device.phys)


device = evdev.InputDevice('/dev/input/event6')
print(device.capabilities(verbose=True))


for event in device.read_loop():
    # print(evdev.categorize(event))
    if event is evdev.KeyEvent:
        print(event.keycode)
