
OUTPUTS = output/13skill1.txt \
          output/45skill1.txt \
          output/67skill1.txt \
          output/8skill1.txt  \
          output/9skill1.txt  \
          output/12skill3.txt \
          output/34skill3.txt \
          output/1skill4.txt

all: check

output/%.txt: demos/%.lmp ../newdoom1.wad ../newdoom1_1lev.wad testrunner
	@mkdir -p output
	./testrunner $< > $@

check: $(OUTPUTS)
	@diff -q -x .gitignore -r expected output && echo all tests passed

clean:
	rm -rf output

.PHONY: check clean all
