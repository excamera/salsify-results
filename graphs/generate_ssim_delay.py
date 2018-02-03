#!/usr/bin/env python3

import os
import sys
import math

import numpy as np

def usage(argv0):
    print("{argv0} PLAYBACK-LOG ANALYSIS-LOG".format(argv0=argv0))

INVARIANT_DELAY = 66733 # us

class SSIM:
    @staticmethod
    def db2n(db):
        n = -10 ** (-db / 10) + 1
        assert 0.0 <= n <= 1.0, "ssim={} not in [0, 1]".format(n)
        return n

    @staticmethod
    def n2db(n):
        assert 0.0 <= n <= 1.0, "ssim must be in [0, 1]"
        db = 10 * math.log10(1 / (1 - n))
        return db

def parse_playback_file(playback_file):
    print("> reading the playback file: {}".format(playback_file), file=sys.stderr)

    frames = []

    with open(playback_file) as f:
        i = 0
        for line in f:
            line = line.strip()
            if line.startswith("#"): continue

            data = [int(x) for x in line.split(",")]

            assert len(data) == 8, "missing fields in frame: {}".format(i)
            assert data[0] == i, "frame not find: {}".format(i)
            assert data[1] == data[2], "UL and LR barcodes don't match for frame {}".format(i)

            frames += [{
                'sent': data[7]
            }]

            i += 1

    print("> reading playback file done successfully.", file=sys.stderr)

    return frames

def parse_analysis_file(analysis_file, frames):
    print("> reading the analysis file: {}".format(analysis_file), file=sys.stderr)

    with open(analysis_file) as f:
        i = 0
        for line in f:
            line = line.strip()
            if line.startswith("#"): continue

            data = line.split(",")

            for j in range(len(data)):
                if j < 7:
                    data[j] = int(data[j])
                else:
                    data[j] = float(data[j])

            assert len(data) == 11, "missing fields in frame: {}".format(i)
            assert data[0] >= i, "frame appeared not in order: {}".format(i)

            i = data[0]

            assert data[5] > data[4], "send time is before receive time for frame {}".format(i)
            assert (data[5] - data[4]) == data[6], "delay value is wrong for frame {}".format(i)

            frames[i]['received'] = data[5]
            frames[i]['ssim'] = data[8]
            frames[i]['delay'] = frames[i]['received'] - frames[i]['sent'] - INVARIANT_DELAY

    print("> reading analysis file done successfully.", file=sys.stderr)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        usage(sys.argv[0])
        sys.exit(1)

    frames = parse_playback_file(sys.argv[1])
    parse_analysis_file(sys.argv[2], frames)

    earliest = min([frame.get('sent') for frame in frames if frame.get('received')])

    for frame in frames:
        if frame.get('received'):
            print((frame['received'] - earliest) / 1e6, frame['delay'] / 1e3, frame['ssim'], sep='\t')
