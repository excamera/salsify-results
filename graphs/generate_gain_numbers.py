#!/usr/bin/env python3

import os
import sys
import subprocess as sub
import json
import math

def usage(argv0):
    print("{argv0} EXPERIMENT-LIST-FILES...".format(argv0=argv0))

curdir = os.path.dirname(__file__)

AGGREGATE_PROGRAM = os.path.join(curdir, "../scripts/aggregate-stats.py")
BENCHMARKS_ROOT = os.path.join("../benchmarks")

BASE = "Salsify-1"
SKIP = ["Salsify-1", "Salsify-2", "Salsify-4"]

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

def get_data_for(run_path):
    return eval(sub.check_output([
        AGGREGATE_PROGRAM,
        os.path.join(run_path, "video3_720p60.analysis.csv"),
        os.path.join(run_path, "video3_720p60.playback.csv"),
        os.path.join(run_path, "downlink.log"),
    ]))

def process_list(experiment_list_file):
    programs = {}
    with open(experiment_list_file) as fin:
        for line in fin:
            line = line.strip()
            if not line:
                continue

            label = line.split(" ")[1]
            path = line.split(" ")[0]
            data = get_data_for(os.path.join(BENCHMARKS_ROOT, path))

            programs[label] = {
                'ssim': SSIM.db2n(float(data['ssim']['mean'])),
                'delay': float(data['signal_delay']['p95'])
            }

    gains = {'ssim': 0, 'delay': 0, 'count': 0}
    for program, data in programs.items():
        if (program in SKIP) or (program == BASE): continue
        gains['count'] += 1
        gains['ssim'] += data['ssim'] / programs[BASE]['ssim']
        gains['delay'] += data['delay'] / programs[BASE]['delay']

    return gains

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage(sys.argv[0])
        sys.exit(1)

    total_gains = {'ssim': 0, 'delay': 0, 'count': 0}

    for list_file in sys.argv[1:]:
        gains = process_list(list_file)
        total_gains['ssim'] += gains['ssim']
        total_gains['delay'] += gains['delay']
        total_gains['count'] += gains['count']

    print("SSIM:  ", 1 / (total_gains['ssim'] / total_gains['count']))
    print("Delay: ", total_gains['delay'] / total_gains['count'])
    print("Count: ", total_gains['count'])
