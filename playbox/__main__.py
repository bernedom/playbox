#!/usr/bin/env python3

from playbox.RFID_Reader import RFID_Reader
from playbox.Player import Player


player = Player()
reader = RFID_Reader(player)
reader.aqcuireDevice("HID 413d:2107")
reader.run()
