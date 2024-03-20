
FASTDOOM_FILES = fastdoom/doom1.tcf fastdoom/fdoom.exe fastdoom/fdsetup.exe \
                 fastdoom/readme.txt

doof.img: empty.img install/doof.dat DOOF.EXE
	cp empty.img $@
	SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy \
	    dosbox -conf mkdisk.cfg
	@echo
	@cat DIRLIST.TXT
	@rm -f DIRLIST.TXT

install/doof.dat: doof.dat.template DOOF.EXE
	sed "s/9999999/$$(stat -c "%s" DOOF.EXE)/" \
          < $< > $@

DOOF.EXE: doof.lzh
	SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy \
	    dosbox -conf mksfx.cfg

doof.lzh: staging
	rm -f $@
	cd $<; lha -ao5 ../$@ *

check:
	rm -rf /tmp/doof-autoinst
	mkdir /tmp/doof-autoinst
	SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy \
	    dosbox -conf autoinst.cfg
	[ -e /tmp/doof-autoinst/DOOFINST/FDOOM.CFG ]
	diff -u ../newdoom1.wad /tmp/doof-autoinst/DOOFINST/DOOM1.WAD
	diff -u fastdoom/fdoom.exe /tmp/doof-autoinst/DOOFINST/FDOOM.EXE
	echo Install worked successfully

staging: $(FASTDOOM_FILES) ../newdoom1.wad
	rm -rf staging
	mkdir -p staging/inter
	cp $(FASTDOOM_FILES) staging/
	cp fastdoom/inter/e1.txt staging/inter/
	cp ../newdoom1.wad staging/doom1.wad

clean:
	rm -rf doof.img staging DOOF.EXE doof.lzh \
               install/doof.dat

