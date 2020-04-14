#!/usr/bin/env python3

import validators
import pathlib
import logging


class AudioLibrary:

    def __init__(self):
        self.__audio = {}

    def registerAudio(self, key: str, audio_path: str):
        if(not pathlib.Path(audio_path).is_absolute()):
            audio_path = pathlib.Path(audio_path).absolute()

        logging.debug(
            "Matching key {} to audio file {}".format(key, audio_path))
        self.__audio[key] = pathlib.Path(audio_path).as_uri()

    def getAudio(self, key: str):
        return self.__audio[key]

    def hasAudio(self, key: str):
        return key in self.__audio
