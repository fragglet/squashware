#!/usr/bin/env python3

from glob import glob
from PIL import Image
import struct
import sys

def read_cel(filename):
    with open(filename, "rb") as f:
        result = {}
        while True:
            hdr = f.read(8)
            if len(hdr) < 8:
                return result
            name, cnt = struct.unpack(">4sI", hdr)
            name = name.decode("ASCII")
            data = f.read(cnt - 8)
            result[name] = data

def decode_pal(paldata):
    paldata = paldata[4:]  # skip header
    result = []
    for i in range(len(paldata) // 2):
        off = i * 2
        rgb, = struct.unpack(">H", paldata[off:off+2])
        print("%04x" % rgb)
        r = ((rgb >> 10) & 0x1f) << 3
        g = ((rgb >> 5) & 0x1f) << 3
        b = (rgb & 0x1f) << 3
 #       print("%02x%02x%02x" % (r,g,b))
        result.append((r, g, b))
    return result

def cel_to_image(sections):
    pal = decode_pal(sections['PLUT'])
    ccb, pdat = sections['CCB '], sections['PDAT']
    packed = (pdat[6] & 0x1) == 0
    h, w = struct.unpack(">II", ccb[0x40:0x48])
    img = Image.new("RGB", (w, h))
    for x in range(w):
        for y in range(h):
            off = x * h + y
            if packed:
                b, n = off // 2, 1 - (off % 2)
                i = (pdat[b] >> (n * 4)) & 0xf
            else:
                i = pdat[off]
            img.putpixel((x, y), pal[i])
    return img

for filename in sys.argv[1:]:
    print(filename)
    sections = read_cel(filename)
    img = cel_to_image(sections)
    outfile = filename.replace("cel", "png")
    img.save(outfile)

