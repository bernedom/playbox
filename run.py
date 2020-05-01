#!/usr/bin/env python3

from time import sleep
from playbox import AudioLibrary, Player, RFID_Reader

library = AudioLibrary()

# temporary set up
library.registerAudio("03242743", "/var/playbox/audio/test.MP3")
# library.registerAudio("99999999", "spotify:track:0tKcYR2II1VCQWT79i5NrW")
library.registerSpotifyAudio(
    "03046971", "https://open.spotify.com/track/1zB4vmk8tFRmM9UULNzbLB")
library.saveToCsv("/var/playbox/music.csv")
#

library.readFromCsv("/var/playbox/music.csv")
# TODO  sleep because of race condition on startup
sleep(5.0)

player = Player(library)
reader = RFID_Reader(player)
reader.aqcuireDevice("HID 413d:2107")
player.playuri("file:///opt/playbox/ready.mp3")
reader.run()
