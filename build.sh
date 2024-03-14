#!/bin/bash

set -eu -o pipefail

rm -f newdoom1.wad newdoom1_silent.wad silent.wad

if ! deutex -version >/dev/null; then
    echo "deutex not installed."
    exit 1
fi

deutex -doom2 bootstrap/ -iwad -build wadinfo.txt newdoom1.wad

deutex -doom2 bootstrap/ -build silent.txt silent.wad
cp newdoom1.wad newdoom1_silent.wad
# TODO: We should strip the _DEUTEX_ lump that deutex leaves behind.
deutex -doom2 bootstrap/ -join newdoom1_silent.wad silent.wad

if wadptr -version >/dev/null; then
    wadptr -wipesides -q -c newdoom1.wad
    wadptr -wipesides -q -c newdoom1_silent.wad
else
    echo "wadptr not installed; can't compress WAD."
fi
