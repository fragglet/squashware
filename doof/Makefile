
FASTDOOM_FILES = fastdoom/doom1.tcf fastdoom/fdoom.exe fastdoom/fdsetup.exe

doof.img: empty.img staging
	cp empty.img $@
	SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy \
	    dosbox -conf mkdisk.cfg

staging: $(FASTDOOM_FILES)
	rm -rf staging
	mkdir -p staging/inter
	cp $(FASTDOOM_FILES) staging/
	cp fastdoom/inter/e1.txt staging/inter/
	cp ../newdoom1.wad staging/doom1.wad

clean:
	rm -rf doof.img staging DOOF.EXE DOOF.LZH

