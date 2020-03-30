FROM alpine:latest

RUN apk add moc xorg-server vim python3 python2 linux-headers python3-dev gcc g++ mopidy mpc

RUN pip3 install --upgrade pip
RUN pip3 install Mopidy-MusicBox-Webclient Mopidy-MPD evdev python-mpd2 

#debug tools
RUN apk add sox nmap

COPY resource/mopidy.conf /etc/mopidy/mopidy.conf

EXPOSE 10000

CMD mopidy --config /etc/mopidy/mopidy.conf