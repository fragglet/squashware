#!/bin/bash

set -eu -o pipefail

rm -f newdoom1.wad

if ! deutex -version >/dev/null; then
    echo "deutex not installed."
    exit 1
fi

deutex -doom2 bootstrap/ -iwad -build wadinfo.txt newdoom1.wad

if wadptr -version >/dev/null; then
    wadptr -q -c newdoom1.wad
else
    echo "wadptr not installed; can't compress WAD."
fi
