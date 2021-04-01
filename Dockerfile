# https://hub.docker.com/_/python

FROM python:3

RUN useradd --shell /bin/bash --create-home --home-dir /home/pythondev pythondev
USER pythondev

WORKDIR /home/pythondev/

COPY requirements.txt ./
RUN pip3 install --no-warn-script-location --user --no-cache-dir -r requirements.txt \
    && rm requirements.txt
COPY config.pylintrc ./
COPY words /usr/share/dict/words

CMD [ "/bin/bash" ]
