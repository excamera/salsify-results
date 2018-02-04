#!/usr/bin/env python3

import os
import sys
import math
import statistics

import numpy as np

def usage(argv0):
    print("{argv0} TRACE-PATH START-TIME(second) LENGTH(second) OUTPUT-DIR".format(argv0=argv0))

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
                'sent': data[7],
                'received': None,
                'delay': None,
                'ssim': None
            }]

            i += 1

    return frames

def parse_analysis_file(analysis_file, frames):
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

            i = data[0]

            frames[i]['received'] = data[5]
            frames[i]['delay'] = data[6]
            frames[i]['ssim'] = data[8]

def compute_signal_delay(frames):
    delays = []

    v = []

    for frame in frames:
        v += [frame['sent']]
        if frame.get('received'):
            delays += [frame.get('received') - x for x in v]
            v = []

    return {
        'signal_delay': {
            'mean': '{:.2f}'.format((np.mean(delays) - INVARIANT_DELAY) / 1000),
            'median': '{:.2f}'.format((np.median(delays) - INVARIANT_DELAY) / 1000),
            'p5':   '{:.2f}'.format((np.percentile(delays, 5) - INVARIANT_DELAY) / 1000),
            'p95':  '{:.2f}'.format((np.percentile(delays, 95) - INVARIANT_DELAY) / 1000),
            'p25':  '{:.2f}'.format((np.percentile(delays, 25) - INVARIANT_DELAY) / 1000),
            'p75':  '{:.2f}'.format((np.percentile(delays, 75) - INVARIANT_DELAY) / 1000),
        }
    }

SCHEMES = [
    ("WebRTC", "apprtc-rerun-2017-09-07"),
    ("Salsify-2", "salsify2"),
    ("Facetime", "facetime"),
    ("Skype", "skype"),
    ("Hangouts", "hangouts")
]

if __name__ == '__main__':
    if len(sys.argv) != 5:
        usage(sys.argv[0])
        sys.exit(1)


    trace_path = sys.argv[1]
    output_path = sys.argv[4]
    start_time = int(sys.argv[2]) * 1000 * 1000 # usec
    length = int(sys.argv[3]) * 1000 * 1000 # usec

    for scheme in SCHEMES:
        playback_file = os.path.join(trace_path, scheme[1], 'video3_720p60', 'video3_720p60.playback.csv')
        analysis_file = os.path.join(trace_path, scheme[1], 'video3_720p60', 'video3_720p60.analysis.csv')
        output_file_1 = os.path.join(output_path, "%s.dat" % scheme[0])
        output_file_2 = os.path.join(output_path, "%s-timelapse.dat" % scheme[0])

        of1 = open(output_file_1, "w")
        of2 = open(output_file_2, "w")

        frames = parse_playback_file(playback_file)
        parse_analysis_file(analysis_file, frames)

        this_start = start_time + frames[0]['sent']
        this_end = this_start + length

        target_frames = [f for f in frames if f.get('received') and this_start <= f['sent'] < this_end]
        signal_delay_target = [f for f in frames if this_start <= f['sent'] < this_end]

        last_ssim = None

        v = []

        for frame in signal_delay_target:
            v += [frame['sent']]

            if frame.get('received'):
                for s in v:
                    print(
                    "{:.2f} {}".format((frame['received'] - s - INVARIANT_DELAY) / 1000.0, frame['ssim']),
                    file=of2
                    )
                v = []

        print(compute_signal_delay(signal_delay_target)['signal_delay']['p95'],
            SSIM.n2db(statistics.mean([SSIM.db2n(x['ssim']) for x in target_frames])),
            file=of1
        )
