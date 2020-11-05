#!/usr/bin/env python3

import logging
from playbox.Player import Player
from playbox.RFID_Reader import RFID_Reader
import sys

# Mock class for testing without an RFID-Reader present
class stdin_Reader(RFID_Reader):
    def __init__(self, player: Player, device_id=''):
        # self.device_id = '/dev/input/event20'
        self.player = player
        self.player.connect()

    def aqcuireDevice(self, name: str):
        pass

    def hasDeviceAqcuired(self):
        return True

    def run(self):
        
        for message in sys.stdin:
            message.rstrip()
            if message != "":
                self.player.play(message.strip())
                message = ""
    
    }
