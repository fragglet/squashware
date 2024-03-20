This is a work-in-progress discussion of the techniques used for compression
in this project.

# Background

Back in 2019 I released [miniwad](https://github.com/fragglet/miniwad), a
Doom IWAD file that is less than 250KB in size. The project was
intended as an exercise in minimalism and as a demo of the
[wadptr](https://github.com/fragglet/wadptr) WAD compression tool, which
exploits various details of the Doom WAD format to shrink WADs. To my
surprise, it was later used in a port of [Doom to the Nintendo
Game & Watch](https://www.youtube.com/watch?v=sNg_S9UM5ps), a device with
very limited internal storage.

In March 2024 I came across [Doom on a
Toothbrush](https://www.youtube.com/watch?v=cO-Are8053g), another port making
use of miniwad's tiny size. But the version seen in the video was a bit
different - Doom's first level had been added back, along with some of its
textures and other graphics, to give something that was more visibly "Doom".

While it's flattering to see people making use of my projects, I started to
feel a bit sad for the authors of such ports being forced to compromise for
the sake of space. It got me wondering how small a *real* Doom IWAD file
might be made. The Doom shareware IWAD ([DOOM1.WAD](https://doomwiki.org/wiki/DOOM1.WAD))
is over 4MB, and after compression, fitted onto two floppy disks. With some
clever hackery, how much smaller could it get?

# Redundancy

Despite its small size, DOOM1.WAD contains a whole bunch of unused resources
that either are used only for the registered version, or seem to have snuck
in accidentally during the development process.

Some of these I wasn't even aware of until I started poring through the
contents. For example, [one of the BFG sound effects](https://github.com/fragglet/squashware/commit/0aaa2c22f9d20944fbb3ae0aba503ef1a3226848)
is in the shareware WAD. The most surprising were a small collection of sprites
that were accidentally added while developing Doom II -
[the Arachnotron and Mancubus](https://github.com/fragglet/squashware/commit/1d5fc52bd87a5450f56385c6a4f129fea55a4a1b)
projectiles, and even [the spinning cube](https://github.com/fragglet/squashware/commit/2f009b6b81b9435175b71de7deec3e6e1f9ef1ea)
used for the Doom II final boss.

- Using wadptr to combine resources

# The levels

- Only E1
- Switched to Console Doom levels
- The bigger deal is the knock-on effects:
  - Reduced texture set
  - Some items can be removed
- ZokumBSP

# Graphics

- Overview of how graphic squashing works
- Improving compressability
- SKY1 example
- Title screen

# Sprites

- Mirrored rotations eg. for Baron
- Reduced walking frames
- 3-rotations

# UI

- eg. menu font
- Intermission screen flat wall
- Status bar

# Textures

- Rebuilding out of patches
- Compare startan and SW1STRTN

# Sound effects

- Speedups
- Shortening the biggest sounds
- Cropping eg. chainsaw sounds

# Music

- MUS is smaller than MIDI
- Cropping, eg. D\_VICTOR and D\_INTER
- Volume changes in D\_E1M9

