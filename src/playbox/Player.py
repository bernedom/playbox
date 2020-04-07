#!/usr/bin/env python3

from mpd import MPDClient


class Player:

    def __init__(self):
        self.mpd_client = MPDClient()
        self.mpd_client.timeout = 10
        # timeout for fetching the result of the idle command is handled seperately, default: None
        self.mpd_client.idletimeout = None

    def connect(self, port=6600):
        self.mpd_client.connect("localhost", 6600)  # connect to localhost:6600

    def play(self, song: str):
        self.mpd_client.add
        self.mpd_client.add(song)
        self.mpd_client.next()
        self.mpd_client.play()
