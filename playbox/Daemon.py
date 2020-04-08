#!/usr/bin/env python3

from RFID_Reader import RFID_Reader
from Player import Player

if __name__ == "__main__":

    player = Player()
    reader = RFID_Reader(player)
