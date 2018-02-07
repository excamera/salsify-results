#!/usr/bin/gnuplot -persist
#
#
#    	G N U P L O T
#    	Version 5.0 patchlevel 3    last modified 2016-02-21
#
#    	Copyright (C) 1986-1993, 1998, 2004, 2007-2016
#    	Thomas Williams, Colin Kelley and many others
#
#    	gnuplot home:     http://www.gnuplot.info
#    	faq, bugs, etc:   type "help FAQ"
#    	immediate help:   type "help"  (plot window: hit 'h'
#set terminal svg enhanced size 800, 650 background rgb 'white'
set terminal svg enhanced size 1000, 500 background rgb 'white'
set output 'ssim-graph.svg'
unset clip points
set clip one
unset clip two
set bar 1.000000 front
set border 3 front lt black linewidth 1.000 dashtype solid
set zdata
set ydata
set xdata
set y2data
set x2data
set boxwidth
set style fill  empty border
set style rectangle back fc  bgnd fillstyle   solid 1.00 border lt -1
set style circle radius graph 0.02, first 0.00000, 0.00000
set style ellipse size graph 0.05, 0.03, first 0.00000 angle 0 units xy
set dummy x, y
set format x "%g"
set format y "% h"
set format x2 "% h"
set format y2 "% h"
set format z "% h"
set format cb "% h"
set format r "% h"
set timefmt "%d/%m/%y,%H:%M"
set angles radians
set tics back
unset grid
set raxis
set style parallel front  lt black linewidth 2.000 dashtype solid
set key title "" center
set key inside right top vertical Right noreverse enhanced autotitle nobox
set key noinvert samplen 4 spacing 1 width 0 height 0
set key maxcolumns 0 maxrows 0
set key noopaque
unset key
unset label
unset arrow
set style increment default
unset style line

# Please change the colors...
set style line 1 linewidth 1.000 dashtype solid pointtype 7 pointsize default pointinterval 0
set style line 2 linewidth 1.000 dashtype solid pointtype 7 pointsize default pointinterval 0
set style line 3 linewidth 1.000 dashtype solid pointtype 7 pointsize default pointinterval 0
set style line 4 linewidth 1.000 dashtype solid pointtype 7 pointsize default pointinterval 0
set style line 5 linewidth 1.000 dashtype solid pointtype 7 pointsize default pointinterval 0
set style line 6 linewidth 1.000 dashtype solid pointtype 7 pointsize default pointinterval 0
set style line 7 linewidth 1.000 dashtype solid pointtype 7 pointsize default pointinterval 0
set style line 8 linewidth 1.000 dashtype solid pointtype 7 pointsize default pointinterval 0
set style line 9 linewidth 1.000 dashtype solid pointtype 7 pointsize default pointinterval 0
set style line 10 linewidth 1.000 dashtype solid pointtype 7 pointsize default pointinterval 0
set style line 11 linewidth 1.000 dashtype solid pointtype 7 pointsize default pointinterval 0
set style line 12 linewidth 1.000 dashtype solid pointtype 7 pointsize default pointinterval 0
set style line 13 linewidth 1.000 dashtype solid pointtype 7 pointsize default pointinterval 0
set style line 14 linewidth 1.000 dashtype solid pointtype 7 pointsize default pointinterval 0
set style line 15 linewidth 1.000 dashtype solid pointtype 7 pointsize default pointinterval 0
set style line 16 linewidth 1.000 dashtype solid pointtype 7 pointsize default pointinterval 0
set style line 17 linewidth 1.000 dashtype solid pointtype 7 pointsize default pointinterval 0

unset style arrow
set style histogram clustered gap 2 title textcolor lt -1
unset object
set style textbox transparent margins  1.0,  1.0 border
unset logscale
set offsets 0, 0, 0, 0
set pointsize 1
set pointintervalbox 1
set encoding default
unset polar
unset parametric
unset decimalsign
set view 60, 30, 1, 1
set samples 100, 100
set isosamples 10, 10
set surface
unset contour
set cntrlabel  format '%8.3g' font '' start 5 interval 20
set mapping cartesian
set datafile separator whitespace
unset hidden3d
set cntrparam order 4
set cntrparam linear
set cntrparam levels auto 5
set cntrparam points 5
set size ratio 0.5
set origin 0,0
set style data points
set style function lines
unset xzeroaxis
unset yzeroaxis
unset zzeroaxis
unset x2zeroaxis
unset y2zeroaxis
set xyplane relative 0.5
set tics scale  1, 0.5, 1, 1, 1
set mxtics default
set mytics default
set mztics default
set mx2tics default
set my2tics default
set mcbtics default
set mrtics default
set xtics border in scale 1,0.5 nomirror norotate  autojustify
set xtics  norangelimit autofreq
set ytics border in scale 1,0.5 nomirror norotate  autojustify
set ytics  norangelimit autofreq
set ztics border in scale 1,0.5 nomirror norotate  autojustify
set ztics  norangelimit autofreq
set xtics font "Arial, 24"
set ytics font "Arial, 24"
unset x2tics
unset y2tics
set cbtics border in scale 1,0.5 mirror norotate  autojustify
set cbtics  norangelimit autofreq
set rtics axis in scale 1,0.5 nomirror norotate  autojustify
set rtics  norangelimit autofreq
unset paxis 1 tics
unset paxis 2 tics
unset paxis 3 tics
unset paxis 4 tics
unset paxis 5 tics
unset paxis 6 tics
unset paxis 7 tics
set title ""
set title  font "" norotate
set timestamp bottom
set timestamp ""
set timestamp  font "" norotate
set rrange [ * : * ] noreverse nowriteback
set trange [ * : * ] noreverse nowriteback
set urange [ * : * ] noreverse nowriteback
set vrange [ * : * ] noreverse nowriteback
set xlabel "Display Time (s)"
set xlabel  font "Arial, 28" textcolor lt -1 norotate  offset 0, -0.6
set x2label ""
set x2label  font "" textcolor lt -1 norotate
set x2range [ * : * ] noreverse nowriteback
set ylabel "Frame Quality (SSIM dB)"
set ylabel font "Arial, 28" textcolor lt -1 rotate by -270 offset -2, 0
set y2label ""
set y2label  font "" textcolor lt -1 rotate by -270
set xrange [ -5 : 6 ] noreverse nowriteback
set yrange [ 9 : 15 ] noreverse nowriteback
set y2range [ * : * ] noreverse nowriteback
set zlabel ""
set zlabel  font "" textcolor lt -1 norotate
set zrange [ * : * ] noreverse nowriteback
set cblabel ""
set cblabel  font "" textcolor lt -1 rotate by -270
set cbrange [ * : * ] noreverse nowriteback
set paxis 2 range [ * : * ] noreverse nowriteback
set paxis 3 range [ * : * ] noreverse nowriteback
set paxis 4 range [ * : * ] noreverse nowriteback
set paxis 5 range [ * : * ] noreverse nowriteback
set paxis 1 range [ * : * ] noreverse nowriteback
set paxis 6 range [ * : * ] noreverse nowriteback
set paxis 7 range [ * : * ] noreverse nowriteback
set zero 1e-08
set lmargin  10
set bmargin  4.5
set rmargin  -1
set tmargin  -1
set locale "en_US.UTF-8"
set pm3d explicit at s
set pm3d scansautomatic
set pm3d interpolate 1,1 flush begin noftriangles noborder corners2color mean
set palette positive nops_allcF maxcolors 0 gamma 1.5 color model RGB
set palette rgbformulae 7, 5, 15
set colorbox default
set colorbox vertical origin screen 0.9, 0.2, 0 size screen 0.05, 0.6, 0 front bdefault
set style boxplot candles range  1.50 outliers pt 7 separation 1 labels auto unsorted
set loadpath
set fontpath
set psdir
set fit brief errorvariables nocovariancevariables errorscaling prescale nowrap v5
set xtics 1

set style rect fc rgb "#FFBABA" fs pattern 1 noborder
set obj rect from 0, graph 0 to 1, graph 1

set label "Salsify-2c" at first -2.75, first 13.75 font "Arial:Bold, 27" tc rgb "#44DF006F"
set label "WebRTC" at first -2.75, first 10.75 font "Arial:Bold, 27" tc rgb "#440000a0"
set label "outage" at first 0.5, first 12 rotate center font "Arial:Bold, 37" tc rgb "#FF9999"
#set label "WebRTC" at first -2.75, first 11 font "Arial:Bold, 27" tc rgb "#440000a0"

plot \
     "WebRTC-new.dat" using ($2-150):3 with points ls 1 lt rgb "#440000a0",\
     "Salsify.dat" using ($2-150):3 with points ls 1 lt rgb "#44DF006F",\
     #"WebRTC.dat" using ($2-150):3 with points ls 1 lt rgb "#440000a0",\
