#!/usr/bin/env python3

import os
import sys
import string

PLOT_TEMPLATE = '''"{file}" using 3:4 with linespoints ls {i} ps 3 lt rgb "{color}", \\\n"{file}" using 3:4:("{label}") with labels left offset 2.2, char 0 font "Arial:Bold, 28" tc rgb "{color}" notitle'''


curdir = os.path.dirname(__file__)
TEMPLATE_FILE = os.path.join(curdir, 'template.gnu')

COLORS = [
    "#F26822",
    "#37A313",
    "#7E4CB6",
    "#DF0000",
    "#1A95C2",
]

def get_color(i):
    return COLORS[i % len(COLORS)]

def usage(argv0):
    print("{argv0} DATA-DIR".format(argv0=argv0))

def main(data_dir):
    plot_data = []

    i = 1
    for f in os.listdir(data_dir):
        if not f.endswith(".dat"): continue

        label = f.split(".")[0]
        plot_data += [PLOT_TEMPLATE.format(file=f, i=i, color=get_color(i), label=label)]

        i += 1

    with open(TEMPLATE_FILE) as tfin:
        template_data = tfin.read()

    template = string.Template(template_data)

    with open(os.path.join(data_dir, 'graph.gnu'), "w") as fout:
        s = template.safe_substitute(
            XMIN=9000,
            XMAX=500,
            YMIN=9,
            YMAX=17,
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
