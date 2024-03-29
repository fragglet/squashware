#!/usr/bin/env python3

import mido
import sys

def used_channels(f):
	return {
		m.channel for m in f.tracks[0]
		if isinstance(m, mido.Message)
	}

def make_sequence(t, msg_type="note_on", chan=None):
	result = []
	curr_time = 0
	for msg in t:
		curr_time += msg.time
		if msg.type != msg_type or msg.channel == 9:
			continue
		if chan is not None and msg.channel != chan:
			continue
		result.append((curr_time, msg.channel, msg.note))
	return result

def match_start(seq, match_len=10):
	if len(seq) == 0:
		return
	print("\tsequence starts at %s, will subtract" % seq[0][0])
	for i in range(len(seq)):
		j = 0
		while i + j < len(seq):
			t1, c1, n1 = seq[j]
			t2, c2, n2 = seq[i + j]
			if c1 != c2 or n1 != n2:
				break
			j += 1
		if j > match_len:
			print("\tmatch_start at time %s: %d notes" % (
				seq[i][0] - seq[0][0], j))

def match_end(seq, match_len=10):
	for i in reversed(range(len(seq))):
		j = 0
		while i - j >= 0:
			t1, c1, n1 = seq[len(seq) - 1 - j]
			t2, c2, n2 = seq[i - j]
			if c1 != c2 or n1 != n2:
				break
			j += 1
		if j > match_len:
			print("\tmatch_end at time %s: %d notes" % (
				seq[i][0], j))

def crop_file(f, new_len):
	outfile = mido.MidiFile(type=f.type, ticks_per_beat=f.ticks_per_beat)
	outfile.add_track("")
	t = outfile.tracks[0]

	curr_time = 0
	curr_real_time = 0
	time_adjust = 0
	target_len = int((new_len // 275.4) * 275.4)
	speedup = target_len / new_len

	for msg in f.tracks[0]:
		curr_time += msg.time
		print(curr_time, msg)
		if not isinstance(msg, mido.Message):
			continue

		msg = msg.copy()
		time_adjust += msg.time * speedup
		msg.time = int(time_adjust)
		time_adjust -= msg.time
		curr_real_time += msg.time
		if (curr_real_time + 15) >= target_len:
			break
		t.append(msg)

	print(curr_real_time, target_len)

	# "All notes off" for all channels, no hanging notes at end of track.
	for chan in sorted(used_channels(f)):
		t.append(mido.Message("control_change", channel=chan,
		                      control=123))

	t.append(mido.MetaMessage("end_of_track"))

	return outfile

def detect_loop_points(f):
	for chan in used_channels(f):
		for nt in ("note_on", "note_off"):
			print("chan=%s, type=%s:" % (chan, nt))
			seq = make_sequence(f.tracks[0], nt, chan)
			match_start(seq)
			match_end(seq)


if __name__ == "__main__":
	with mido.MidiFile(sys.argv[1]) as f:
		if len(sys.argv) == 4:
			cropped = crop_file(f, int(sys.argv[2]))
			cropped.save(sys.argv[3])
		else:
			detect_loop_points(f)

