#!/usr/bin/env python3
import evdev


devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
    print(device.path, device.name, device.phys)

print("Done")
# needed for a clean shutdown
del devices
