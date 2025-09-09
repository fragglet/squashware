#!/usr/bin/env python3
#
# "Lossy compression" script that identifies similar columns and
# combines them, so that wadptr will be able to produce a smaller
# resulting graphic lump.

import PIL.Image
import math
import sys

# If two columns are at most this similar, they will be merged.
THRESHOLD = 0.005

def compare_columns(im, x1, x2):
    _, h = im.size

    total_diff = 0

    for y in range(h):
        r1, g1, b1, a1 = im.getpixel((x1, y))
        r2, g2, b2, a2 = im.getpixel((x2, y))
        diff = ((r1 - r2) ** 2 +
                (g1 - g2) ** 2 +
                (b1 - b2) ** 2 +
                (a1 - a2) ** 2)
        diff = diff / (255 * 255)
        total_diff += diff

    return math.sqrt(total_diff) / h

def process_image(filename):
    im = PIL.Image.open(filename).convert("RGBA")

    w, h = im.size
    total_merged = 0
    for x in range(1, w):
        best_x = None
        best_diff = 999999999
        for x2 in range(x):
            diff = compare_columns(im, x, x2)
            if diff < best_diff:
                best_x = x2
                best_diff = diff
        #print("%4d: closest is %4d (%6f)" % (x, best_x, best_diff))

        if best_diff < THRESHOLD:
            for y in range(h):
                im.putpixel((x, y), im.getpixel((best_x, y)))
            total_merged += 1

    print("%s: %d columns merged" % (filename, total_merged))
    im.save(filename)


for filename in sys.argv[1:]:
    process_image(filename)
