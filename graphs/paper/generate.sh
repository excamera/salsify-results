#!/bin/bash

DIRS=(
    att-lte
    tmobile-umts
    verizon-lte
    on-off
    )

for dir in ${DIRS[@]}; do
    cd $dir
    gnuplot graph.gnu
    inkscape graph.svg --export-pdf=graph.pdf
    cp graph.pdf ../$dir.pdf
    cd ..
done
