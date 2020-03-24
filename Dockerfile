FROM alpine:latest

RUN apk add moc xorg-server vim python3 linux-headers python3-dev gcc g++ mopidy
RUN pip3 install --upgrade pip
RUN pip3 install evdev python-mpd2

COPY resource/mopidy.conf /root/.config/mopidy
#RUN mopidy config

#COPY test.MP3 /var/lib/mopidy/media/test.MP3
#RUN mopidy &
#RUN mopidyctl local scan

EXPOSE 6680