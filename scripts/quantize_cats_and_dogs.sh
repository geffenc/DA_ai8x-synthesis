#!/bin/sh
./quantize.py trained/qat_cats_and_dogs__best.pth.tar trained/qat_cats_and_dogs-q.pth.tar --device MAX78000 -v "$@"
