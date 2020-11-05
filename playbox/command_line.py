#!/usr/bin/env python3

from time import sleep
from playbox import AudioLibrary, Player, RFID_Reader, stdin_Reader
import atexit
import argparse

player = None
parser = argparse.ArgumentParser()
parser.add_argument("-d", help="Run in dev mode - RFID input is emulated over keyboard")
parser.parse_args()

def shutdown():
    if player is not None:
        player.stop()


def main():
    global parser
    global player
    atexit.register(shutdown)
    library = AudioLibrary()

    library.readFromCsv("/var/playbox/audio.csv")
    # TODO  sleep because of race condition on startup
    sleep(5.0)

    # TODO move configuration to a config file and create setup routine
    player = Player(library)
    player.registerStop("03331943")
    player.registerNext("04029591")
    player.registerPrevious("03331879")

    reader = None
    if parser.d:
        reader = stdin_Reader(player)
    else:
        reader = RFID_Reader(player)
    reader.aqcuireDevice("HID 413d:2107")
    player.playuri("file:///var/playbox/ready.mp3")
    reader.run()
