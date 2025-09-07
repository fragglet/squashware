<img src="disks.png" height="120">

## Doom On One Floppy (DOOF)

DOOF combines Squashware Doom with the
[FastDoom source port](https://github.com/viti95/FastDoom) to create a complete
shareware version that fits on a single floppy disk (1.44 MB 3½" or 1.2 MB
5¼"). There are two versions:

* `doof.img` is a 1.2MiB floppy disk image that contains a copy of Squashware
  Doom along with the [DEICE](https://doomwiki.org/wiki/DEICE) installer. You
  can use this to install to a hard drive.

* `doofboot.img` is a 1.2MiB floppy disk image that will run Squashware Doom
  from boot. It contains a minimal copy of [SVARDOS](http://svardos.org/);
  the game files are automatically extracted to a RAM disk on startup and the
  game is then launched.
