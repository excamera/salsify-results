#!/usr/bin/env python3

import os
import sys
import re
import statistics

def usage(argv0):
    print("{argv0} SENDER-LOG".format(argv0=argv0))

frame_log_pattern = re.compile(r"\[(?P<timestamp>\d+)\] Frame (?P<frame_no>\d+): (?P<job_name>[-\w]+) \((?P<quantizer>\d+)\) = (?P<fragments>\d+) fragments \((?P<encode_time>\d+) ms, ssim=(?P<ssim>[0-9]+(\.[0-9]+)?)\) \{\d+ -> \d+\} intersend_delay = \d+ us,  state-count = (?P<state_count>\d+)( \<mem = (?P<mem_usage>\d+)\>)?")

skip_log_pattern = re.compile(r"\[(?P<timestamp>\d+)\] Skipping frame (?P<frame_no>\d+)")
toomany_log_pattern = re.compile(r"Too many skipped frames; sending the bad-quality option on \d+")

def main(sender_log, start_time, end_time):
    points = []
    state_counts = []
    sent = 0
    skipped = 0
    options = {}

    with open(sender_log) as fin:
        for line in fin:
            line = line.strip()

            r1 = frame_log_pattern.match(line)
            r2 = skip_log_pattern.match(line)
            r3 = toomany_log_pattern.match(line)

            if r1:
                timestamp = int(r1.group('timestamp'))
                quantizer = 127 - int(r1.group('quantizer'))
                state_count = int(r1.group('state_count'))

                if start_time <= timestamp <= end_time:
                    sent += 1
                    options[r1.group('job_name')] = options.get(r1.group('job_name'), 0) + 1

            elif r2:
                timestamp = int(r2.group('timestamp'))
                quantizer = None

                if start_time <= timestamp <= end_time:
                    skipped += 1
            elif r3:
                pass
            elif line == "Going into 'conservative' mode for next 5 seconds.":
                pass
            else:
                print(line)
                raise Exception('unknown line')

            if timestamp < start_time or timestamp > end_time:
                continue

            state_counts += [state_count]

    # print(statistics.mean(state_counts))
    # print(statistics.stdev(state_counts))
    # print(max(state_counts))

    print(skipped / (sent + skipped))
    print(options)


    # bin_size = 100
    # max_timestamp = max([x[0] for x in points])
    # min_timestamp = min([x[0] for x in points])
    #
    # bin_start, bin_end = min_timestamp, min_timestamp + bin_size
    #
    # new_points = []
    # while bin_start <= max_timestamp:
    #     d = [x[1] for x in points if (bin_start <= x[0] < bin_end) and x[1] is not None]
    #     if len(d) > 0:
    #         value = statistics.median(d)
    #         new_points += [(bin_start, value, len([x[1] for x in points if (bin_start <= x[0] < bin_end) and x[1] is None]) > 0)]
    #     bin_start = bin_end
    #     bin_end += bin_size
    #
    # for point in new_points:
    #     print(point[0], point[1], '10' if point[2] else '0', sep='\t')

if __name__ == '__main__':
    if len(sys.argv) != 4:
        usage(sys.argv[0])
        sys.exit(1)

    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
