FROM alpine:latest

RUN apk add moc xorg-server vim python3 linux-headers python3-dev gcc g++
RUN pip3 install --upgrade pip
RUN pip3 install evdev