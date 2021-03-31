#!/bin/sh

# create "local" copies of files we want copied into the container
# because... Dockerfile file referencing is weird
cp /usr/share/dict/british-english ./words

# build (or rebuild) the python-base container using the Dockerfile in the current directory
docker build -t impractical-base .

# clean up any local temp files we created for the sake of copying into the image
rm ./words
