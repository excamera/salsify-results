#!/bin/bash

DIRS=(att-lte
      on-off
      tmobile-umts
      verizon-lte
      wifi)

for dir in ${DIRS[@]}; do
    cd $dir

    echo $(pwd)

    gnuplot graph.gnu
    inkscape graph.svg --export-pdf=$dir.pdf
    cp $dir.pdf ../../../../salsify-paper/figures/

    cd ..
done

make -C ../../../salsify-paper/
