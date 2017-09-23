#!/bin/bash

DIRS=(att-lte
      buffer-1024
      buffer-256
      buffer-64
      on-off
      tmobile-umts
      verizon-lte)

for dir in ${DIRS[@]}; do
    cd $dir

    echo $(pwd)
    
    gnuplot graph.gnu
    inkscape graph.svg --export-pdf=$dir.pdf
    cp $dir.pdf ../../../../salsify-paper/figures/

    cd ..
done

make -C ../../../salsify-paper/
