FROM debian:10.5

ENV DEBIAN_FRONTEND=noninteractive

# TODO deploy to dockerhub

RUN apt update
RUN apt install -y gnupg2 wget apt-transport-https ca-certificates

RUN wget -q -O - https://apt.mopidy.com/mopidy.gpg | apt-key add -
RUN wget -q -O /etc/apt/sources.list.d/mopidy.list https://apt.mopidy.com/buster.list
RUN apt update

RUN apt install -y vim python3 python3-dev gcc g++ mopidy mpc wget libffi-dev python3-pip mopidy-spotify
RUN pip3 install --upgrade pip


# System packages 
RUN pip3 install Mopidy-MPD Mopidy-Iris

#debug tools
RUN apt install -y sox nmap procps libsox-fmt-mp3

RUN apt install -y alsa-utils

COPY requirements.txt /root/

# Packages used in the scripts
RUN pip3 install -r /root/requirements.txt

RUN echo "[http]" >> /etc/mopidy/mopidy.conf
RUN echo "hostname = 0.0.0.0" >> /etc/mopidy/mopidy.conf

RUN echo "defaults.pcm.card 1" >> /etc/asound.conf
RUN echo "defaults.ctl.card 1" >> /etc/asound.conf

# install playbox
COPY dist/playbox-0.1.1.tar.gz /root/playbox-install.tar.gz
RUN cd /root/ && tar -xvzf playbox-install.tar.gz && cd playbox-0.1.1 && python3 setup.py install

EXPOSE 10000

CMD mopidy --config /etc/mopidy & playbox ${PLAYBOX_DEBUG}

