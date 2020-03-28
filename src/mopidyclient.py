#!/usr/bin/env python3

from mpd import MPDClient
client = MPDClient()               # create client object
# network timeout in seconds (floats allowed), default: None
client.timeout = 10
# timeout for fetching the result of the idle command is handled seperately, default: None
client.idletimeout = None
client.connect("localhost", 6660)  # connect to localhost:6600
print(client.mpd_version)          # print the MPD version
# print result of the command "find any house"
print(client.find("any", "test"))

client.iterate = True
for song in client.playlistinfo():
    print(song["file"])

print(client.stats())
print(client.currentsong())

client.close()                     # send the close command
client.disconnect()
