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


def registerSpecialKey(config: configparser.SectionProxy, player: Player, key: str):
    try:
        player.registerSpecialKey(key, config[key])
    except KeyError:
        pass


def main():
    global parser
    global player
    atexit.register(shutdown)
    library = AudioLibrary()

    library.readFromCsv("/var/playbox/audio.csv")
    config = configparser.ConfigParser()
    config.read("/etc/playbox/playbox.conf")
    special_keys = config["SPECIALKEYS"]
    rfid_config = config["RFID"]

    player = Player(library)
    registerSpecialKey(special_keys, player, "stop")
    registerSpecialKey(special_keys, player, "next")
    registerSpecialKey(special_keys, player, "previous")
    registerSpecialKey(special_keys, player, "pause")

    reader = None
    if arguments.d:
        reader = stdin_Reader(player)
    else:
        reader = RFID_Reader(player)
    reader.aqcuireDevice(rfid_config["usb_id"])

    while not player.connect():
        time.sleep(0.3)
        logging.debug("Connection failed, trying again")

    player.play("file:///var/playbox/ready.mp3")
    reader.run()
