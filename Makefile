#!/bin/bash

WADPTR_FLAGS = -wipesides -q
DEUTEX_FLAGS = -doom2 bootstrap/

WADS = newdoom1.wad newdoom1_1lev.wad newdoom1_silent.wad

all: $(WADS)

kernel.wad: kernel.txt
	@rm -f $@
	deutex $(DEUTEX_FLAGS) -iwad -build $< $@

1lev.wad: 1lev.txt
	@rm -f $@
	deutex $(DEUTEX_FLAGS) -build $< $@

1lev_sounds.wad: 1lev_sounds.txt
	@rm -f $@
	deutex $(DEUTEX_FLAGS) -build $< $@

main.wad: main.txt
	rm -f $@
	deutex $(DEUTEX_FLAGS) -build $< $@

sounds.wad: sounds.txt
	rm -f @$
	deutex $(DEUTEX_FLAGS) -build $< $@

# E1M1-only WAD
newdoom1_1lev_silent.wad: 1lev.wad kernel.wad
	cp kernel.wad $@
	deutex $(DEUTEX_FLAGS) -join $@ $<
	wadptr $(WADPTR_FLAGS) -c $@

newdoom1_1lev.wad: 1lev_sounds.wad newdoom1_1lev_silent.wad
	cp newdoom1_1lev_silent.wad $@
	deutex $(DEUTEX_FLAGS) -join $@ $<
	wadptr $(WADPTR_FLAGS) -c $@

# Silent WAD
newdoom1_silent.wad: main.wad newdoom1_1lev_silent.wad
	cp newdoom1_1lev_silent.wad $@
	deutex $(DEUTEX_FLAGS) -join $@ $<
	wadptr $(WADPTR_FLAGS) -c $@

# Full WAD
newdoom1.wad: 1lev_sounds.wad sounds.wad newdoom1_silent.wad
	cp newdoom1_silent.wad $@
	deutex $(DEUTEX_FLAGS) -join $@ 1lev_sounds.wad
	deutex $(DEUTEX_FLAGS) -join $@ sounds.wad
	wadptr $(WADPTR_FLAGS) -c $@

# TODO: We should strip the _DEUTEX_ lump that deutex leaves behind.

check: $(WADS)
	make -C playthru check

doof: $(WADS)
	make -C doof

clean:
	rm -f kernel.wad \
	      newdoom1_1lev_silent.wad 1lev.wad \
	      newdoom1_1lev.wad 1lev_sounds.wad \
	      newdoom1_silent.wad sounds.wad \
	      newdoom1.wad main.wad

.PHONY: check clean doof all
