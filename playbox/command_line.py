#!/usr/bin/env python3

from time import sleep
from playbox import AudioLibrary, Player, RFID_Reader, stdin_Reader
import atexit
import argparse
import time
import logging
import configparser

# Todo add arguments to find the audio database and config file
player = None
parser = argparse.ArgumentParser()
parser.add_argument(
    "-d", help="Run in dev mode - RFID input is emulated over keyboard", action='store_true')
arguments = parser.parse_args()


def shutdown():
    if player is not None:
        player.stop()


def main():
    global parser
    global player
    atexit.register(shutdown)
    library = AudioLibrary()

    library.readFromCsv("/var/playbox/audio.csv")
    config = configparser.ConfigParser()
    config.read("/etc/playbox/playbox.conf")
    special_keys = config["SPECIALKEYS"]

    player = Player(library)
    player.registerStop(special_keys["stop"])
    player.registerNext(special_keys["next"])
    player.registerPrevious(special_keys["previous"])

    reader = None
    if arguments.d:
        reader = stdin_Reader(player)
    else:
        reader = RFID_Reader(player)
    reader.aqcuireDevice("HID 413d:2107")

    while not player.connect():
        time.sleep(0.3)
        logging.debug("Connection failed, trying again")

    player.play("file:///var/playbox/ready.mp3")
    reader.run()
