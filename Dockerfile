FROM debian:10.5

ENV DEBIAN_FRONTEND=noninteractive
ARG PLAYBOX_PYTHON_VERSION

RUN apt-get update && apt-get install -y --no-install-recommends gnupg2 wget apt-transport-https ca-certificates

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN wget -q -O - https://apt.mopidy.com/mopidy.gpg | apt-key add - && \
    wget -q -O /etc/apt/sources.list.d/mopidy.list https://apt.mopidy.com/buster.list

RUN apt-get update && apt-get install -y --no-install-recommends vim python3 python3-dev \
    gcc g++ mopidy mpc libffi-dev python3-pip mopidy-spotify \
    gstreamer1.0-alsa gstreamer1.0-tools gstreamer1.0-pulseaudio

# install python packages for the system
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install Mopidy-MPD==3.0.0 Mopidy-Iris==3.54.2

# Packages used in the scripts 
COPY requirements.txt /root/
RUN pip3 install -r /root/requirements.txt

# Cleanup tools only needed for setup to make container image smaller
RUN apt-get remove -y python3-dev gcc g++ && apt-get autoremove -y

RUN echo "[http]" >> /etc/mopidy/mopidy.conf && \
    echo "hostname = 0.0.0.0" >> /etc/mopidy/mopidy.conf

RUN echo "defaults.pcm.card 1" >> /etc/asound.conf && \
    echo "defaults.ctl.card 1" >> /etc/asound.conf

# install playbox
COPY dist/playbox-${PLAYBOX_PYTHON_VERSION}.tar.gz /root/playbox-install.tar.gz
RUN cd /root/ && tar -xvzf playbox-install.tar.gz && cd playbox-${PLAYBOX_PYTHON_VERSION} && python3 setup.py install

EXPOSE 10000
EXPOSE 6680
EXPOSE 6600

CMD mopidy --config /etc/mopidy & playbox ${PLAYBOX_DEBUG}

