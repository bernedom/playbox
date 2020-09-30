#!/bin/bash
#docker run -v $(pwd):/root/mount -ti  --device /dev/snd phoniedocker
docker run -ti -v $(pwd):/root/mount \
-v /tmp/.X11-unix:/tmp/.X11-unix \
-v $(pwd)/resource/audio.csv:/var/playbox/audio.csv \
-e DISPLAY=$DISPLAY -d \
--device /dev/snd --privileged -p 10000:10000 --rm phoniedocker
