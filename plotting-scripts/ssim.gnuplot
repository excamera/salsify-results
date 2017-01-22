set term png
#set output "output.svg" 

set datafile separator ","
plot "video1_720p60.analysis.csv" using 0:8 with lines