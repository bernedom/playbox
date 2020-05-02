#!/usr/bin/env python3

from time import sleep
from playbox import AudioLibrary, Player, RFID_Reader

library = AudioLibrary()

library.readFromCsv("/var/playbox/audio.csv")
# TODO  sleep because of race condition on startup
sleep(5.0)

player = Player(library)
reader = RFID_Reader(player)
reader.aqcuireDevice("HID 413d:2107")
player.playuri("file:///opt/playbox/ready.mp3")
reader.run()
