#!/usr/bin/env python3

from time import sleep
from playbox import AudioLibrary, Player, RFID_Reader


def main():
    library = AudioLibrary()

    library.readFromCsv("/var/playbox/audio.csv")
    # TODO  sleep because of race condition on startup
    sleep(5.0)

    # TODO move configuration to a config file and create setup routine
    player = Player(library)
    player.registerStop("03331943")
    reader = RFID_Reader(player)
    reader.aqcuireDevice("HID 413d:2107")
    player.playuri("file:///var/playbox/ready.mp3")
    reader.run()
