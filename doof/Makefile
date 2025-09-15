
FASTDOOM_FILES = fastdoom/doom1.tcf fastdoom/fdoom.exe fastdoom/fdsetup.exe \
                 fastdoom/readme.txt

all: doof-1.2M.img doof-1.44M.img

doof-1.2M.img: svdos-1.2M.img install/doof.dat DOOF.EXE
	cp svdos-1.2M.img $@
	SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy \
	    dosbox -conf mkdisk-1.2M.cfg
	@echo
	@cat DIRLIST.TXT
	@rm -f DIRLIST.TXT

doof-1.44M.img: svdos-1.44M.img install/doof.dat DOOF.EXE
	cp svdos-1.44M.img $@
	SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy \
	    dosbox -conf mkdisk-1.44M.cfg
	@echo
	@cat DIRLIST2.TXT
	@rm -f DIRLIST2.TXT

install/doof.dat: doof.dat.template DOOF.EXE
	sed "s/9999999/$$(stat -c "%s" DOOF.EXE)/" \
          < $< > $@

DOOF.EXE: doof.lzh
	SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy \
	    dosbox -conf mksfx.cfg

doof.lzh: staging
	rm -f $@
	cd $<; lha -ao6 ../$@ *

check: doof-1.2M.img staging
	rm -rf /tmp/doof-autoinst
	mkdir /tmp/doof-autoinst
	SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy \
	    dosbox -conf autoinst.cfg
	[ -e /tmp/doof-autoinst/DOOFINST/FDOOM.CFG ]
	diff -u ../newdoom1.wad /tmp/doof-autoinst/DOOFINST/DOOM1.WAD
	diff -u staging/fdoom.exe /tmp/doof-autoinst/DOOFINST/FDOOM.EXE
	echo Install worked successfully

staging: $(FASTDOOM_FILES) ../newdoom1.wad
	rm -rf staging
	mkdir -p staging/inter
	cp $(FASTDOOM_FILES) staging/
	upx --lzma staging/fdoom.exe
	upx --lzma staging/fdsetup.exe
	cp fastdoom/inter/e1.txt staging/inter/
	cp ../newdoom1.wad staging/doom1.wad

clean:
	rm -rf doof-1.2M.img doof-1.44M.img staging \
	       DOOF.EXE doof.lzh install/doof.dat
