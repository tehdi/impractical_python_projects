# https://hub.docker.com/_/python

FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt && rm requirements.txt

CMD [ "bash" ]
