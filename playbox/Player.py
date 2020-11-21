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
        # TODO put function pointers/lambda or similar into a dict
        # TODO handle duplicate registration (probably done by moving to a dict)
        self.__stopKey = ""
        self.__nextKey = ""
        self.__previousKey = ""
        self.__currentKey = ""

    def connect(self, port=6600):
        self.mpd_client.connect("localhost", 6600)  # connect to localhost:6600

    def registerStop(self, key: str):
        self.__stopKey = key

    def registerNext(self, key: str):
        self.__nextKey = key

    def registerPrevious(self, key: str):
        self.__previousKey = key

    # TODO rename to handle token
    def play(self, key: str):
        if key == self.__stopKey:
            self.stop()
            return
        elif key == self.__nextKey:
            self.next()
            return
        elif key == self.__previousKey:
            self.previous()
            return

        try:
            if self.__currentKey != key:
                self.playuri(self.__library.getAudio(key))
            self.__currentKey = key
        except KeyError:
            logging.info("Trying to play back unregistered key: " + key)

    def stop(self):
        logging.info("Stopping play")
        self.mpd_client.stop()
        self.__currentKey = ""

    def next(self):
        logging.info("Jumping to next track")
        self.mpd_client.next()

    def previous(self):
        logging.info("Jumping to previous track")
        self.mpd_client.previous()

    def playuri(self, audio_file):
        logging.info("playing audio_file " + audio_file)
        self.mpd_client.clear()
        self.mpd_client.add(audio_file)
        self.mpd_client.next()
        self.mpd_client.play()
