#!/usr/bin/env python3

from mpd import MPDClient
import mpd
from playbox import AudioLibrary
import logging

# TODO add sanitizer for registering keys


class Player:

    def __init__(self, audio_library: AudioLibrary):
        self.mpd_client = MPDClient()
        # timeout for fetching the result of the idle command is handled seperately, default: None
        self.mpd_client.idletimeout = None
        self.__library = audio_library

        # TODO handle duplicate registration (probably done by moving to a dict)
        self.__specialKeys = {}
        self.__specialFunctions = {
            "stop": self.stop, "next": self.next, "previous": self.previous, "pause": self.pause}
        self.__currentKey = ""
        self.__isPaused = False

    def connect(self, port=6600):

        # Disconnect first, to make sure a fresh connection is established
        try:
            self.mpd_client.close()
            self.mpd_client.disconnect()
        except (mpd.base.ConnectionError):
            pass

        try:
            # connect to localhost:6600
            self.mpd_client.connect("localhost", 6600)
            return True
        except mpd.base.ConnectionError:
            logging.error("Could not connect to mpd")
        except ConnectionRefusedError:
            logging.error("Could not connect to mpd")

        return False

    def registerSpecialKey(self, function: str, key: str):
        logging.info(
            "Registering special function '{}', to key '{}'".format(function, key))
        self.__specialKeys[key] = function

    def registerStop(self, key: str):
        self.registerSpecialKey("stop", key)

    def registerNext(self, key: str):
        self.registerSpecialKey("next", key)

    def registerPrevious(self, key: str):
        self.registerSpecialKey("previous", key)

    def registerPause(self, key: str):
        self.registerSpecialKey("pause", key)

    def handleToken(self, key: str):
        if not self.connect():
            return

        if key in self.__specialKeys and self.__specialKeys[key] in self.__specialFunctions:
            self.__specialFunctions[self.__specialKeys[key]]()
            return

        try:
            if self.__currentKey != key:
                self.play(self.__library.getAudio(key))
                self.__currentKey = key
            elif self.__isPaused:
                self.pause()

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

    def pause(self):
        logging.info("Pausing play")
        if not self.__isPaused:
            self.mpd_client.pause()
            self.__isPaused = True
        else:
            self.mpd_client.play()
            self.__isPaused = False

    def play(self, audio_file):
        logging.info("playing audio_file " + audio_file)
        self.mpd_client.clear()
        self.mpd_client.add(audio_file)
        self.mpd_client.next()
        self.mpd_client.play()
