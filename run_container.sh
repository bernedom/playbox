#!/bin/bash
#docker run -v $(pwd):/root/mount -ti  --device /dev/snd phoniedocker
docker run -v $(pwd):/root/mount \
-v /tmp/.X11-unix:/tmp/.X11-unix \
-e DISPLAY=$DISPLAY -ti \
--device /dev/snd --privileged -v /dev/bus/usb:/dev/bus/usb phoniedocker
