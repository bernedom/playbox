#!/usr/bin/env python3

from mpd import MPDClient
import mpd
from playbox import AudioLibrary
import logging

# TODO add sanitizer for registering keys
# TODO check if mpc client is connected before calling its functions


class Player:

    def __init__(self, audio_library: AudioLibrary):
        self.mpd_client = MPDClient()
        # timeout for fetching the result of the idle command is handled seperately, default: None
        self.mpd_client.idletimeout = None
        self.__library = audio_library
        # TODO put function pointers/lambda or similar into a dict
        # TODO handle duplicate registration (probably done by moving to a dict)
        self.__stopKey = ""
        self.__nextKey = ""
        self.__previousKey = ""
        self.__currentKey = ""

    def isConnected(self):
        try:
            self.mpd_client.fileno()
            return True
        except mpd.base.ConnectionError:
            return False

    def connect(self, port=6600):
        if self.isConnected():
            return True
        try:
            # connect to localhost:6600
            self.mpd_client.connect("localhost", 6600)
            return True
        except mpd.base.ConnectionError:
            logging.error("Could not connect to mpd")
        except ConnectionRefusedError:
            logging.error("Could not connect to mpd")

        return False

    def registerStop(self, key: str):
        self.__stopKey = key

    def registerNext(self, key: str):
        self.__nextKey = key

    def registerPrevious(self, key: str):
        self.__previousKey = key

    # TODO rename to handle token
    def play(self, key: str):
        if not self.connect():
            return
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
        if not self.connect():
            return
        self.mpd_client.stop()
        self.__currentKey = ""

    def next(self):
        logging.info("Jumping to next track")
        if not self.connect():
            return
        self.mpd_client.next()

    def previous(self):
        logging.info("Jumping to previous track")
        if not self.connect():
            return
        self.mpd_client.previous()

    def playuri(self, audio_file):
        logging.info("playing audio_file " + audio_file)
        if not self.connect():
            return
        self.mpd_client.clear()
        self.mpd_client.add(audio_file)
        self.mpd_client.next()
        self.mpd_client.play()
