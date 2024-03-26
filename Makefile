#!/bin/bash

WADPTR_FLAGS = -wipesides -q
DEUTEX_FLAGS = -doom2 build/kernel

WADS = newdoom1.wad newdoom1_silent.wad \
       newdoom1_1lev.wad newdoom1_1lev_silent.wad

all: $(WADS)

# The very first thing we build is the "kernel" WAD. This then gets used
# as the IWAD file used when building all the other WADs. This is necessary
# because the PNAMES lump generated for TEXTURE2 needs to be compatible with
# the one generated for TEXTURE1.
build/kernel/doom.wad: kernel.txt
	@rm -f $@
	@mkdir -p build/kernel
	deutex -doom2 bootstrap/ -iwad -build $< $@

%.wad: build/kernel/doom.wad

build/%.wad: %.txt build/kernel/doom.wad
	@rm -f $@
	@mkdir -p build
	deutex $(DEUTEX_FLAGS) -build $< $@

# E1M1-only WAD
newdoom1_1lev_silent.wad: build/1lev.wad
	cp build/kernel/doom.wad $@
	deutex $(DEUTEX_FLAGS) -join $@ $<
	wadptr $(WADPTR_FLAGS) -c $@

newdoom1_1lev.wad: build/1lev_sounds.wad newdoom1_1lev_silent.wad
	cp newdoom1_1lev_silent.wad $@
	deutex $(DEUTEX_FLAGS) -join $@ $<
	wadptr $(WADPTR_FLAGS) -c $@

# Silent WAD
newdoom1_silent.wad: build/main.wad newdoom1_1lev_silent.wad
	cp newdoom1_1lev_silent.wad $@
	deutex $(DEUTEX_FLAGS) -join $@ $<
	wadptr $(WADPTR_FLAGS) -c $@

# Full WAD
newdoom1.wad: build/1lev_sounds.wad build/sounds.wad newdoom1_silent.wad
	cp newdoom1_silent.wad $@
	deutex $(DEUTEX_FLAGS) -join $@ build/1lev_sounds.wad
	deutex $(DEUTEX_FLAGS) -join $@ build/sounds.wad
	wadptr $(WADPTR_FLAGS) -c $@

# TODO: We should strip the _DEUTEX_ lump that deutex leaves behind.

check: $(WADS)
	make -C playthru check

doof: $(WADS)
	make -C doof

clean:
	make -C playthru clean
	make -C doof clean
	rm -f $(WADS)
	rm -rf build

.PHONY: check clean doof all
