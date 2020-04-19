FROM debian:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update
RUN apt install -y gnupg2 wget

RUN wget -q -O - https://apt.mopidy.com/mopidy.gpg | apt-key add -
RUN wget -q -O /etc/apt/sources.list.d/mopidy.list https://apt.mopidy.com/buster.list
RUN apt update

RUN apt install -y vim python3 python3-dev gcc g++ mopidy mpc wget libffi-dev python3-pip mopidy-spotify
RUN pip3 install --upgrade pip


# System packages 
RUN pip3 install Mopidy-MusicBox-Webclient Mopidy-MPD


#debug tools
RUN apt install -y sox nmap

COPY resource/mopidy.conf /etc/mopidy/mopidy.conf
COPY requirements.txt /root/

# Packages used in the scripts
RUN pip3 install -r /root/requirements.txt

EXPOSE 10000

CMD mopidy --config /etc/mopidy/mopidy.conf