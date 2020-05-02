#!/usr/bin/env python3

from mpd import MPDClient
from playbox import AudioLibrary
import logging

# TODO add sanitizer for registering keys
# TODO check if mpc client is connected before calling its functions


class Player:

    def __init__(self, audio_library: AudioLibrary):
        self.mpd_client = MPDClient()
        self.mpd_client.timeout = 10
        # timeout for fetching the result of the idle command is handled seperately, default: None
        self.mpd_client.idletimeout = None
        self.__library = audio_library
        self.__stopKey = ""

    def connect(self, port=6600):
        self.mpd_client.connect("localhost", 6600)  # connect to localhost:6600

    def registerStop(self, key: str):
        self.__stopKey = key

    def play(self, key: str):
        if key == self.__stopKey:
            self.stop()
            return

        try:
            self.playuri(self.__library.getAudio(key))
        except KeyError:
            logging.info("Trying to play back unregistered key: " + key)

    def stop(self):
        logging.info("Stopping play")
        self.mpd_client.stop()

    def playuri(self, audio_file):
        logging.info("playing audio_file " + audio_file)
        self.mpd_client.clear()
        self.mpd_client.add(audio_file)
        self.mpd_client.next()
        self.mpd_client.play()
