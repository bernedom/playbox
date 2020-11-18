FROM debian:10.5

ENV DEBIAN_FRONTEND=noninteractive
ARG PLAYBOX_PYTHON_VERSION

RUN test -n "$PLAYBOX_PYTHON_VERSION" || (echo "PLAYBOX_PYTHON_VERSION  not set" && false)


RUN apt update
RUN apt install -y gnupg2 wget apt-transport-https ca-certificates

RUN wget -q -O - https://apt.mopidy.com/mopidy.gpg | apt-key add -
RUN wget -q -O /etc/apt/sources.list.d/mopidy.list https://apt.mopidy.com/buster.list
RUN apt update

RUN apt install -y vim python3 python3-dev gcc g++ mopidy mpc wget libffi-dev python3-pip mopidy-spotify git
RUN pip3 install --upgrade pip


# Python packages for the system
RUN pip3 install Mopidy-MPD Mopidy-Iris

#debug tools TODO remove for production containers
RUN apt install -y sox nmap procps libsox-fmt-mp3 alsa-utils

# Packages used in the scripts
COPY requirements.txt /root/
RUN pip3 install -r /root/requirements.txt

RUN echo "[http]" >> /etc/mopidy/mopidy.conf
RUN echo "hostname = 0.0.0.0" >> /etc/mopidy/mopidy.conf

RUN echo "defaults.pcm.card 1" >> /etc/asound.conf
RUN echo "defaults.ctl.card 1" >> /etc/asound.conf

# install playbox
COPY dist/playbox-${PLAYBOX_PYTHON_VERSION}.tar.gz /root/playbox-install.tar.gz
RUN cd /root/ && tar -xvzf playbox-install.tar.gz && cd playbox-${PLAYBOX_PYTHON_VERSION} && python3 setup.py install

EXPOSE 10000
EXPOSE 6680
EXPOSE 6600

CMD mopidy --config /etc/mopidy & playbox ${PLAYBOX_DEBUG}

