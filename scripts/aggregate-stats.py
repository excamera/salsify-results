#!/usr/bin/env python2

from __future__ import print_function, division

import os
import sys
import math
import numpy as np

from pprint import pprint

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

def usage(argv0):
    print("{} <analysis_file> <playback_file> <downlink_log>", file=sys.stderr)

def parse_playback_file(playback_file):
    print("> reading the playback file: {}".format(playback_file), file=sys.stderr)

    result = {}

    with open(playback_file) as f:
        i = 0
        for line in f:
            line = line.strip()
            if line.startswith("#"): continue

            data = [int(x) for x in line.split(",")]

            assert len(data) == 8, "missing fields in frame: {}".format(i)
            assert data[0] == i, "frame not find: {}".format(i)
            assert data[1] == data[2], "UL and LR barcodes don't match for frame {}".format(i)

            i += 1

    print("> reading playback file done successfully.", file=sys.stderr)

    result['played_frames'] = i

    return result

def parse_analysis_file(analysis_file):
    print("> reading the analysis file: {}".format(analysis_file), file=sys.stderr)

    result = {
        'first_received': None,
        'last_received': None,
        'count_received': 0,
        'average_ssim': 0,
        'min_ssim': 65536,
        'max_ssim': -1,
        'delays': []
    }

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
            assert not result['last_received'] or result['last_received'] <= data[5]
            assert data[5] > data[4], "send time is before receive time for frame {}".format(i)
            assert (data[5] - data[4]) == data[6], "delay value is wrong for frame {}".format(i)

            if not result['first_received']:
                result['first_received'] = data[5]

            result['last_received'] = data[5]

            result['max_ssim'] = max(result['max_ssim'], data[8])
            result['min_ssim'] = min(result['min_ssim'], data[8])

            result['average_ssim'] = (result['average_ssim'] * result['count_received'] \
                                                             + SSIM.db2n(data[8])) \
                                                             / (result['count_received'] + 1)
            result['count_received'] += 1

            result['delays'] += [data[6]]

            i = data[0]

    assert len(result['delays']) == result['count_received'], "count mismatch"

    print("> reading analysis file done successfully.", file=sys.stderr)

    return {
        'ssim': {
            'mean': SSIM.n2db(result['average_ssim']),
            'min': result['min_ssim'],
            'max': result['max_ssim'],
        },
        'frame_delay': {
            'mean': '{:.2f} ms'.format((np.mean(result['delays']) - INVARIANT_DELAY) / 1000),
            'p95': '{:.2f} ms'.format((np.percentile(result['delays'], 95) - INVARIANT_DELAY) / 1000),
        },
        'total_time': '{:.2f} s'.format((result['last_received'] - result['first_received']) / 1000 ** 2),
        'fps': result['count_received'] / ((result['last_received'] - result['first_received']) / 1000 ** 2),
    }


if __name__ == '__main__':
    if len(sys.argv) == 0:
        sys.exit(1)

    if len(sys.argv) != 3:
        usage(sys.argv[0])
        sys.exit(1)

    parse_playback_file(sys.argv[2])
    result = parse_analysis_file(sys.argv[1])

    print()
    pprint(result, indent=1)
