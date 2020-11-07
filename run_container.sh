#!/bin/bash

docker run -ti -v $(pwd):/root/mount \
-v $(pwd)/resource/audio.csv:/var/playbox/audio.csv \
-v $(pwd)/.vscode/spotify.conf:/etc/mopidy/spotify.conf \
-v /dev/bus/usb:/dev/bus/usb \
--device /dev/snd \
-e PLAYBOX_DEBUG=-d \
--privileged -p 10000:10000 --rm playbox


