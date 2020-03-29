FROM alpine:latest

RUN apk add moc xorg-server vim python3 python2 linux-headers python3-dev gcc g++ mopidy mpc nmap
RUN pip3 install --upgrade pip
RUN pip3 install Mopidy-MusicBox-Webclient Mopidy-MPD
RUN pip3 install evdev python-mpd2 

## chach which one is actually needed
COPY resource/mopidy.conf /etc/mopidy/mopidy.conf

#COPY test.MP3 /var/lib/mopidy/media/test.MP3

#RUN mopidyctl local scan

EXPOSE 6680
#RUN mopidy &

CMD mopidy --config /etc/mopidy/mopidy.conf