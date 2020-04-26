#!/usr/bin/env python3

import pathlib
import logging
import re
import csv


class AudioLibrary:

    def __init__(self):
        self.__audio = {}

    def registerAudio(self, key: str, audio_path: str):

        if(audio_path.startswith("file:///")):
            self.__audio[key] = audio_path
            return

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

        pathlib.Path(pathlib.Path(path).parent.absolute()).mkdir(
            parents=True, exist_ok=True)
        logging.info("Saving to {}".format(path))

        writer = csv.writer(open(path, 'w'), delimiter=";")
        for key, value in self.__audio.items():
            writer.writerow([key, value])

    def readFromCsv(self, path):
        logging.info("Reading from {}".format(path))
        f = open(path, 'r')
        lss = f.readlines()
        logging.warning(lss)
        f.close()
        reader = csv.reader(open(path, 'r'), delimiter=";")
        for row in reader:
            self.registerAudio(row[0], row[1])

    def getAudio(self, key: str):
        return self.__audio[key]

    def hasAudio(self, key: str):
        return key in self.__audio
