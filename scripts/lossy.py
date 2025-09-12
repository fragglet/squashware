#!/usr/bin/env python3
#
# "Lossy compression" script that identifies similar columns and
# combines them, so that wadptr will be able to produce a smaller
# resulting graphic lump.

import PIL.Image
import colorsys
import math
import sys

# Larger value tries harder to preserve brightness level; lower value
# tries harder to preserve color.
COLOR_BALANCE = 3.0

# If two columns are at most this similar, they will be merged.
THRESHOLD = 0.008

def rgba_to_xyza(rgba):
    """Maps from RGB colorspace to a more perceptual colorspace.

    This maps to a HSV color "cone" where euclidean distance better
    matches human perception.
    """
    r, g, b, a = rgba
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    v = v / 255.0
    angle = 2 * math.pi * h
    return (
        math.cos(angle) * s * v,
        math.sin(angle) * s * v,
        v * COLOR_BALANCE,
        a / 255.0,
    )

def compare_colors(rgba1, rgba2):
    x1, y1, z1, a1 = rgba_to_xyza(rgba1)
    x2, y2, z2, a2 = rgba_to_xyza(rgba2)
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2
          + (z1 - z2) ** 2 + (a1 - a2) ** 2)

def compare_columns(im, x1, x2):
    _, h = im.size

    total_diff = 0

    for y in range(h):
        diff = compare_colors(im.getpixel((x1, y)),
                              im.getpixel((x2, y)))
        total_diff += diff

    return math.sqrt(total_diff) / h

def copy_column(im, to_x, from_x):
    _, h = im.size
    modified = False
    for y in range(h):
        old_color = im.getpixel((to_x, y))
        new_color = im.getpixel((from_x, y))
        if old_color != new_color:
            im.putpixel((to_x, y), new_color)
            modified = True
    return modified

def process_image(filename):
    im = PIL.Image.open(filename).convert("RGBA")

    w, h = im.size
    total_merged = 0
    for x in range(2, w):
        best_x = None
        best_diff = 999999999
        # Don't copy from the column right next to this one, as it
        # is a lot more obvious/visible:
        for x2 in range(x - 1):
            diff = compare_columns(im, x, x2)
            if diff < best_diff:
                best_x = x2
                best_diff = diff
        #print("%4d: closest is %4d (%6f)" % (x, best_x, best_diff))

        if best_diff < THRESHOLD and copy_column(im, x, best_x):
            total_merged += 1

    print("%s: %d columns merged" % (filename, total_merged))
    if total_merged > 0:
        im.save(filename)


for filename in sys.argv[1:]:
    process_image(filename)
