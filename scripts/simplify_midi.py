#!/usr/bin/env python3
#
# This script rewrites a MIDI file to strip out "insignificant" volume change
# events (where a particular channel's volume is being changed less than a
# threshold number units compared to its previous value). This significantly
# reduces the size of some of Doom's MIDI tracks, especially D_E1M8 which
# continually changes volume levels of some channels.

import mido
import sys

def simplify_track(events):
    volumes = [99999] * 100
    result = []
    rollover_time = 0
    for e in events:
        # Is this a volume change event? Drop volume change events that
        # are only small adjustments compared to the current value.
        if e.type == "control_change" and e.control == 7:
            curr_volume = volumes[e.channel]
            new_volume = e.value
            if abs(curr_volume - new_volume) < 16:
                print("DROPPED %r" % e)
                rollover_time += e.time
                continue
            volumes[e.channel] = new_volume
        print(e)
        e.time += rollover_time
        rollover_time = 0
        result.append(e)
    return result

f = mido.MidiFile(sys.argv[1])
f.tracks = [simplify_track(t) for t in f.tracks]
f.save(sys.argv[2])
