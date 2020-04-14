#!/usr/bin/env python3

from playbox.RFID_Reader import RFID_Reader
from playbox.Player import Player
from playbox.AudioLibrary import AudioLibrary

library = AudioLibrary()
library.registerAudio("03242743", "/root/mount/test.MP3")

player = Player(library)
reader = RFID_Reader(player)
reader.aqcuireDevice("HID 413d:2107")
reader.run()
