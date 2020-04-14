#!/usr/bin/env python3


class AudioLibrary:

    def __init__(self):
        self.__audio = {}

    def registerAudio(self, key: str, audio_uri: str):
        self.__audio[key] = audio_uri

    def getAudio(self, key: str):
        return self.__audio[key]

    def hasAudio(self, key: str):
        return key in self.__audio
