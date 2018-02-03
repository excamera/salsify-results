#!/usr/bin/env python3

import os
import sys
import re
import statistics

def usage(argv0):
    print("{argv0} LINK-LOG".format(argv0=argv0))

def main(link_log):
    points = []

    with open(link_log) as fin:
        for line in fin:
            line = line.strip()

            if line.startswith('#'):
                continue

            if '#' in line:
                tokens = line.split(' ')
                assert(tokens[1] == '#')
                points += [(int(tokens[0]), int(tokens[2]))]

    bin_size = 500
    max_timestamp = max([x[0] for x in points])
    min_timestamp = min([x[0] for x in points])

    bin_start, bin_end = min_timestamp, min_timestamp + bin_size

    new_points = []
    while bin_start <= max_timestamp:
        new_points += [(bin_start, sum([x[1] for x in points if bin_start <= x[0] < bin_end]))]
        bin_start = bin_end
        bin_end += bin_size

    for point in new_points:
        print(point[0], point[1], sep='\t')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage(sys.argv[0])
        sys.exit(1)

    main(sys.argv[1])
