#!/bin/bash

docker run -ti -v $(pwd):/root/mount \
-v $(pwd)/resource/audio.csv:/var/playbox/audio.csv \
-v /dev/bus/usb:/dev/bus/usb \
-e DISPLAY=$DISPLAY \
--device /dev/snd \
--privileged -p 10000:10000 --rm playbox
