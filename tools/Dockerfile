# https://hub.docker.com/_/python
FROM python:3

# set up a local user
RUN useradd --shell /bin/bash --create-home --home-dir /home/pythondev pythondev
USER pythondev
WORKDIR /home/pythondev/

# install dependencies
COPY requirements.txt ./
RUN pip3 install --no-warn-script-location --no-cache-dir --user -r requirements.txt \
    && rm requirements.txt

# add tools and config files
COPY config.pylintrc ./
COPY bash_aliases ./.bash_aliases
COPY check.sh ./bin/

# add project resources
COPY words ./impractical-resources/chapter-2/words

CMD [ "/bin/bash" ]
