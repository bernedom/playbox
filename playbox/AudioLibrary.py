#!/usr/bin/env python3

import pathlib
import logging
import re
import csv


class AudioLibrary:

    def __init__(self):
        self.__audio = {}

    def registerAudio(self, key: str, audio_path: str):
        if(not pathlib.Path(audio_path).is_absolute()):
            audio_path = pathlib.Path(audio_path).absolute()

        logging.debug(
            "Matching key {} to audio file {}".format(key, audio_path))
        self.__audio[key] = pathlib.Path(audio_path).as_uri()

    def registerSpotifyAudio(self, key: str, url: str):
        pattern = re.compile(
            "^(http[s]?:\\/\\/)(open\\.spotify\\.com)\\/(track)\\/([a-zA-Z\\d]+)")
        match = pattern.match(url)
        if match:
            self.__audio[key] = "spotify:{}:{}".format(
                match.group(3),  match.group(4))
        else:
            raise Exception("Not a spotify URL")

    def saveToCsv(self, path):
        logging.info("Saving to {}".format(path))
        writer = csv.writer(open(path, 'w'), delimiter=";")
        for key, value in self.__audio.items():
            writer.writerow([key, value])

    def getAudio(self, key: str):
        return self.__audio[key]

    def hasAudio(self, key: str):
        return key in self.__audio
