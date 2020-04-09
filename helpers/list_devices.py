#!/usr/bin/env python3

import evdev
from evdev import InputDevice, list_devices


def get_devices():
    return [InputDevice(fn) for fn in list_devices()]


print(get_devices())

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
    print(device.path, device.name, device.phys)
