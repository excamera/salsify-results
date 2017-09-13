#!/usr/bin/env python3

import os
import sys
import subprocess as sub
import json

def usage(argv0):
    print("{argv0} EXPERIMENT-LIST-FILE OUTPUT-DIR".format(argv0=argv0))

curdir = os.path.dirname(__file__)

AGGREGATE_PROGRAM = os.path.join(curdir, "../scripts/aggregate-stats.py")
BENCHMARKS_ROOT = os.path.join("../benchmarks")

COLUMNS = [
    "signal_delay_mean", "signal_delay_p5", "signal_delay_p95",
    "ssim_mean", "ssim_p5", "ssim_p95"
]

def get_data_for(run_path):
    return eval(sub.check_output([
        AGGREGATE_PROGRAM,
        os.path.join(run_path, "video3_720p60.analysis.csv"),
        os.path.join(run_path, "video3_720p60.playback.csv"),
        os.path.join(run_path, "downlink.log"),
    ]))

def main(experiment_list_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    with open(experiment_list_file) as fin:
        for line in fin:
            line = line.strip()
            if not line:
                continue

            label = line.split(" ")[1]
            path = line.split(" ")[0]
            data = get_data_for(os.path.join(BENCHMARKS_ROOT, path))

            row = [
                data['signal_delay']['mean'],
                data['signal_delay']['p5'],
                data['signal_delay']['p95'],
                data['ssim']['mean'],
                data['ssim']['p5'],
                data['ssim']['p95'],
            ]

            row = [str(x) for x in row]

            with open(os.path.join(output_dir, "%s.dat" % label), "w") as fout:
                fout.write("# " + " ".join(COLUMNS) + "\n")
                fout.write(" ".join(row))
                fout.write("\n")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        usage(sys.argv[0])
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])
