FROM debian:latest

ENV DEBIAN_FRONTEND=noninteractive
ARG SPOTIFY_USER
ARG SPOTIFY_PASS
ARG SPOTIFY_CLIENT_ID
ARG SPOTIFY_CLIENT_SECRET

RUN apt update
RUN apt install -y gnupg2 wget apt-transport-https ca-certificates

RUN wget -q -O - https://apt.mopidy.com/mopidy.gpg | apt-key add -
RUN wget -q -O /etc/apt/sources.list.d/mopidy.list https://apt.mopidy.com/buster.list
RUN apt update

RUN apt install -y vim python3 python3-dev gcc g++ mopidy mpc wget libffi-dev python3-pip mopidy-spotify
RUN pip3 install --upgrade pip


# System packages 
RUN pip3 install Mopidy-MusicBox-Webclient Mopidy-MPD

#debug tools
RUN apt install -y sox nmap procps

COPY dist/playbox-0.0.1a0.tar.gz /root/playbox-install.tar.gz
COPY requirements.txt /root/

# Packages used in the scripts
RUN pip3 install -r /root/requirements.txt

# install playbox
RUN cd /root/ && tar -xvzf playbox-install.tar.gz && cd playbox-0.0.1a0 && python3 setup.py install

#patch spotify config
RUN echo "[spotify]" >> /etc/mopidy/mopidy.conf
RUN echo "password = ${SPOTIFY_PASS}" >> /etc/mopidy/mopidy.conf
RUN echo "username = ${SPOTIFY_USER}" >> /etc/mopidy/mopidy.conf
RUN echo "client_id = ${SPOTIFY_CLIENT_ID}" >> /etc/mopidy/mopidy.conf
RUN echo "client_secret = ${SPOTIFY_CLIENT_SECRET}" >> /etc/mopidy/mopidy.conf

EXPOSE 10000

CMD mopidy --config /etc/mopidy/mopidy.conf