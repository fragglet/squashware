
FASTDOOM_FILES = fastdoom/doom1.tcf fastdoom/fdoom.exe fastdoom/fdsetup.exe \
                 fastdoom/readme.txt

doof.img: empty.img install/doof.dat DOOF.EXE
	cp empty.img $@
	SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy \
	    dosbox -conf mkdisk.cfg

install/doof.dat: doof.dat.template DOOF.EXE
	sed "s/9999999/$$(stat -c "%s" DOOF.EXE)/" \
          < $< > $@

DOOF.EXE: staging
	SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy \
	    dosbox -conf mksfx.cfg

staging: $(FASTDOOM_FILES)
	rm -rf staging
	mkdir -p staging/inter
	cp $(FASTDOOM_FILES) staging/
	cp fastdoom/inter/e1.txt staging/inter/
	cp ../newdoom1.wad staging/doom1.wad

clean:
	rm -rf doof.img staging DOOF.EXE DOOF.LZH \
               install/doof.dat

