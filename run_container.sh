#!/bin/bash
#docker run -v $(pwd):/root/mount -ti  --device /dev/snd phoniedocker
docker run -v $(pwd):/root/mount \
-v /tmp/.X11-unix:/tmp/.X11-unix \
-e DISPLAY=$DISPLAY -d \
--device /dev/snd --privileged -p 6680:6680 --rm phoniedocker
