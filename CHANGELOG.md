# Changelog

# 0.1.8

* Fix bug where playbox crashed after a disconnect from mpd
* Add key to toggle pause/play

# 0.1.7

* Put special keys and RFID-reader configuration into a config file

# 0.1.6

* Remove MPD timeout of 10 seconds to avoid losing connection while running
* Renamed play() function to handleToken()

# 0.1.5

* Playbox is able to reconnect if connection to mpd is lost

# 0.1.4

* Putting the same token on the box twice does no longer restart the play
* Linting `Dockerfile` to fix version and make the image smaller

# 0.1.3

* Python module gets version from git
* Initial connection timeout moved to 10s
* Linting in docker

# 0.1.2

* Version bumps to get CI/CD running properly for releases

# 0.1.1 / 0.1.2 

* Add Changelog to project
* Enable deployment on release

## 0.1.0 -  Initial release

* Playback files (mp3, wav, ogg)
* Playback tracks, albums and playlists from spotify
* Emulate RFID-Reader for development
* See the [README](./README.md) for more details
