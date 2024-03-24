#!/bin/bash

set -eu -o pipefail

rm -f kernel.wad \
      newdoom1_1lev_silent.wad 1lev.wad \
      newdoom1_1lev.wad 1lev_sounds.wad \
      newdoom1_silent.wad sounds.wad \
      newdoom1.wad main.wad

if ! deutex -version >/dev/null; then
    echo "deutex not installed."
    exit 1
fi

deutex -doom2 bootstrap/ -iwad -build kernel.txt kernel.wad

# E1M1-only WAD
cp kernel.wad newdoom1_1lev_silent.wad
deutex -doom2 bootstrap/ -build 1lev.txt 1lev.wad
deutex -doom2 bootstrap/ -join newdoom1_1lev_silent.wad 1lev.wad

cp newdoom1_1lev_silent.wad newdoom1_1lev.wad
deutex -doom2 bootstrap/ -build 1lev_sounds.txt 1lev_sounds.wad
deutex -doom2 bootstrap/ -join newdoom1_1lev.wad 1lev_sounds.wad

# Silent WAD
deutex -doom2 bootstrap/ -build main.txt main.wad
cp newdoom1_1lev_silent.wad newdoom1_silent.wad
deutex -doom2 bootstrap/ -join newdoom1_silent.wad main.wad

# Full WAD
deutex -doom2 bootstrap/ -build sounds.txt sounds.wad
cp newdoom1_silent.wad newdoom1.wad
deutex -doom2 bootstrap/ -join newdoom1.wad 1lev_sounds.wad
deutex -doom2 bootstrap/ -join newdoom1.wad sounds.wad

# TODO: We should strip the _DEUTEX_ lump that deutex leaves behind.

if wadptr -version >/dev/null; then
    wadptr -wipesides -q -c newdoom1.wad
    wadptr -wipesides -q -c newdoom1_silent.wad
    wadptr -wipesides -q -c newdoom1_1lev.wad
    wadptr -wipesides -q -c newdoom1_1lev_silent.wad
else
    echo "wadptr not installed; can't compress WAD."
fi
