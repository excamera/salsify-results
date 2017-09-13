#!/usr/bin/env python3

import os
import sys
import string
import math

PLOT_TEMPLATE = '''"{file}" using 3:4 with linespoints ls {i} ps 3 lt rgb "{color}", \\\n"{file}" using 3:4:("{label}") with labels center offset 0, char 2 font "Arial:Bold, 28" tc rgb "{color}" notitle'''


curdir = os.path.dirname(__file__)
TEMPLATE_FILE = os.path.join(curdir, 'template.gnu')

COLORS = {
    'Salsify': '#DF0000',
    'Facetime': '#37A313',
    'Hangouts': '#7E4CB6',
    'WebRTC': '#F26822',
    'Skype': '#1A95C2',
    'WebRTC-SVC': '#AC4F1F',
    'Diet-Salsify': '#DF006F'
}

def usage(argv0):
    print("{argv0} DATA-DIR".format(argv0=argv0))

def main(data_dir):
    plot_data = []

    x_min = 100000
    x_max = 0
    y_min = 25
    y_max = 0


    i = 1
    for f in os.listdir(data_dir):
        if not f.endswith(".dat"): continue

        with open(os.path.join(data_dir, f), "r") as dfin:
            data = dfin.read().split("\n")[1].split(" ")
            (x, y) = (float(data[2]), float(data[3]))
            x_min = min(x, x_min)
            x_max = max(x, x_max)
            y_min = min(y, y_min)
            y_max = max(y, y_max)

        label = f.split(".")[0]
        plot_data += [PLOT_TEMPLATE.format(file=f, i=i, color=COLORS[label], label=label)]

        i += 1

    with open(TEMPLATE_FILE) as tfin:
        template_data = tfin.read()

    template = string.Template(template_data)

    with open(os.path.join(data_dir, 'graph.gnu'), "w") as fout:
        s = template.safe_substitute(
            XMIN=(500 * math.ceil(x_max / 500)) + 1990,
            XMAX=(100 * math.floor(x_min / 100)) - 100,
            YMIN=math.floor(y_min),
            YMAX=math.ceil(y_max),
            PLOTDATA=",\\\n".join(plot_data)
        )

        fout.write(s)

    os.chdir(data_dir)
    os.system("gnuplot graph.gnu")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage(sys.argv[0])
        sys.exit(1)

    main(sys.argv[1])
