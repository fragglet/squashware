#!/bin/sh
rm -f newdoom1.wad
deutex -doom2 bootstrap/ -iwad -build wadinfo.txt newdoom1.wad
wadptr -q -c newdoom1.wad
