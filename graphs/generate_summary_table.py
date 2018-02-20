#!/usr/bin/env python3

import os
import sys
import subprocess as sub
import json
import math
import pprint

def usage(argv0):
    print("{argv0} EXPERIMENT-LIST-FILES...".format(argv0=argv0))

curdir = os.path.dirname(__file__)

AGGREGATE_PROGRAM = os.path.join(curdir, "../scripts/aggregate-stats.py")
BENCHMARKS_ROOT = os.path.join("../benchmarks")

ORDER = [
    ('Salsify-1', 'Salsify-1c'),
    ('Salsify-2', 'Salsify-2c'),
    ('FaceTime', 'FaceTime'),
    ('Facetime', 'FaceTime'),
    ('Hangouts', 'Hangouts'),
    ('Skype', 'Skype'),
    ('WebRTC', 'WebRTC'),
    ('WebRTC-SVC', 'WebRTC (VP9-SVC)')
]

TRACES = {
    'paper/verizon-lte.list': 'Verizon LTE',
    'paper/att-lte.list': 'AT\&T LTE',
    'paper/tmobile-umts.list': 'T-Mobile UMTS',
    'paper/on-off.list': 'Lossy Link',
    'paper/wifi.list': 'Emulated WiFi Link',
}

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
                'ssim-p25': "%.1f" % float(data['ssim']['p25']),
                'ssim-mean': "%.1f" % float(data['ssim']['mean']),
                'delay-mean': "%.1f" % float(data['signal_delay']['mean']),
                'delay-p95': "%.1f" % float(data['signal_delay']['p95'])
            }

    return programs

CELLCOLOR = "\cellcolor{blue!20}"

def winner(programs, metric, value, f):
    target_val = "%.1f" % (f([float(values[metric]) for prog, values in programs.items()]))
    return CELLCOLOR if target_val == value else ''

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage(sys.argv[0])
        sys.exit(1)

    results = {}

    for trace in sys.argv[1:]:
        results[trace] = process_list(trace)

    for trace in sys.argv[1:]:
        for k, v in ORDER:
            if k in results[trace]:
                print("{system} & {trace} & {ssim_p25_best}{ssim_p25}{skewed_ssim} & {ssim_mean_best}{ssim_mean} & & {delay_mean_best}{delay_mean} & {delay_p95_best}{delay_p95} \\\\".format(
                    system=v, trace=TRACES.get(trace, trace),
                    ssim_p25_best=winner(results[trace], 'ssim-p25', results[trace][k]['ssim-p25'], max),
                    ssim_p25=results[trace][k]['ssim-p25'],
                    skewed_ssim='*' if float(results[trace][k]['ssim-p25']) > float(results[trace][k]['ssim-mean']) else '',
                    ssim_mean_best=winner(results[trace], 'ssim-mean', results[trace][k]['ssim-mean'], max),
                    ssim_mean=results[trace][k]['ssim-mean'],
                    delay_mean_best=winner(results[trace], 'delay-mean', results[trace][k]['delay-mean'], min),
                    delay_mean=results[trace][k]['delay-mean'],
                    delay_p95_best=winner(results[trace], 'delay-p95', results[trace][k]['delay-p95'], min),
                    delay_p95=results[trace][k]['delay-p95'],
                ))

        print("& & & & & & \\\\")
