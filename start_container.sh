#!/bin/sh

# run the base container that I'm using for Impractical Python Projects,
# drop me into a cmd inside it,
# then rm the container when I exit
docker run --rm -ti \
    -v $(pwd):/usr/src/app/ \
    impractical-base
