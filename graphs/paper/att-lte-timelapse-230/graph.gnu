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
set output 'graph.svg'
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
set logscale x 10
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
set xtics  norangelimit
set xtics (100, 300, 500, 1000, 2000, 3000, 5000)
set ytics border in scale 1,0.5 nomirror norotate  autojustify
set ytics  norangelimit autofreq
#set ytics (8,10,12,14,16)
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
set xlabel "Video Delay (95th percentile ms)"
set xlabel  font "Arial, 28" textcolor lt -1 norotate  offset 0, -0.6
set x2label ""
set x2label  font "" textcolor lt -1 norotate
set x2range [ * : * ] noreverse nowriteback
set ylabel "Video Quality (SSIM dB)"
set ylabel font "Arial, 28" textcolor lt -1 rotate by -270 offset -2, 0
set y2label ""
set y2label  font "" textcolor lt -1 rotate by -270
set xrange [ 2500 : 50 ] noreverse nowriteback
set yrange [ 5 : 20 ] noreverse nowriteback
set xtics (50, 100, 200, 300, 500, 1000, 2000, 5000, 7000, 9500)
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

plot \
"Salsify-2-timelapse.dat" using 1:2 with lines ls 8 lw 0.25 lt rgb "#66DF006F",\
"Facetime-timelapse.dat" using 1:2 with lines ls 8 lw 3 lt rgb "#3337A313",\
"Skype-timelapse.dat" using 1:2 with lines ls 8 lt rgb "#661A95C2",\
"WebRTC-timelapse.dat" using 1:2 with lines ls 8 lw 3 lt rgb "#55F26822",\
"Hangouts-timelapse.dat" using 1:2 with lines ls 8 lw 2 lt rgb "#667E4CB6",\
"WebRTC.dat" using 1:2 with linespoints ls 8 ps 3.5 lt rgb "#FFFFFF", \
"WebRTC.dat" using 1:2 with linespoints ls 8 ps 2.5 lt rgb "#F26822", \
"Salsify-2.dat" using 1:2 with linespoints ls 7 ps 3.5 lt rgb "#FFFFFF",\
"Salsify-2.dat" using 1:2 with linespoints ls 7 ps 2.5 lt rgb "#DF006F",\
"Facetime.dat" using 1:2 with linespoints ls 4 ps 3.5 lt rgb "#FFFFFF", \
"Facetime.dat" using 1:2 with linespoints ls 4 ps 2.5 lt rgb "#37A313", \
"Skype.dat" using 1:2 with linespoints ls 4 ps 3.5 lt rgb "#FFFFFF", \
"Skype.dat" using 1:2 with linespoints ls 4 ps 2.5 lt rgb "#1A95C2", \
"Hangouts.dat" using 1:2 with linespoints ls 4 ps 3.5 lt rgb "#FFFFFF", \
"Hangouts.dat" using 1:2 with linespoints ls 4 ps 2.5 lt rgb "#7E4CB6", \
"WebRTC.dat" using 1:2:("WebRTC") with labels center offset 0, char -6 font "Arial:Bold, 28" tc rgb "#F26822" notitle,\
"Salsify-2.dat" using 1:2:("Salsify-2c") with labels right offset -2, char 4.9 font "Arial:Bold, 28" tc rgb "#DF006F" notitle,\
"Skype.dat" using 1:2:("Skype") with labels center offset 0, char -3 font "Arial:Bold, 28" tc rgb "#1A95C2" notitle,\
"Facetime.dat" using 1:2:("FaceTime") with labels center offset 0, char 4 font "Arial:Bold, 28" tc rgb "#37A313" notitle,\
"Hangouts.dat" using 1:2:("Hangouts") with labels center offset 0, char -2 font "Arial:Bold, 28" tc rgb "#7E4CB6" notitle,\
#"WebRTC-SVC.dat" using 3:4 with linespoints ls 1 ps 3 lt rgb "#AC4F1F", \
#"WebRTC-SVC.dat" using 3:4:("WebRTC (VP9-SVC)") with labels center offset 2, char 2 font "Arial:Bold, 28" tc rgb "#AC4F1F" notitle,\
#"Skype.dat" using 3:4 with linespoints ls 2 ps 3 lt rgb "#1A95C2", \
#"Skype.dat" using 3:4:("Skype") with labels center offset 0, char 2 font "Arial:Bold, 28" tc rgb "#1A95C2" notitle,\
#"Hangouts.dat" using 3:4 with linespoints ls 5 ps 3 lt rgb "#7E4CB6", \
#"Hangouts.dat" using 3:4:("Hangouts") with labels center offset 0, char 2 font "Arial:Bold, 28" tc rgb "#7E4CB6" notitle,\
#"Salsify-1.dat" using 3:4 with linespoints ls 6 ps 3 lt rgb "#333333", \
#"Salsify-1.dat" using 3:4:("Salsify-1c") with labels right offset -3, char 0 font "Arial:Bold, 28" tc rgb "#333333" notitle,\

#"Salsify-4.dat" using 3:4 with linespoints ls 3 ps 3 lt rgb "#DF0000", \
#"Salsify-4.dat" using 3:4:("Salsify-4") with labels center offset 0, char -2 font "Arial:Bold, 28" tc rgb "#DF0000" notitle,\
