FROM resin/rpi-raspbian:jessie

RUN apt-get -q update \
  && apt-get -qy install \
    python \
    python-dev \
    python-pip \
    gcc \
    make \
  && pip install rpi.gpio

COPY src/ /app

WORKDIR /app

CMD [ "python", "blink.py" ]
