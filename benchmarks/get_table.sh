#!/bin/bash

LIST=(
    Verizon-LTE-driving/salsify-1
    Verizon-LTE-driving/facetime
    Verizon-LTE-driving/hangouts
    Verizon-LTE-driving/apprtc-rerun-2017-09-07
    Verizon-LTE-driving/apprtc-svc-2s-3t
    Verizon-LTE-driving/skype
    ATT-LTE-driving/salsify-1
    ATT-LTE-driving/facetime
    ATT-LTE-driving/hangouts
    ATT-LTE-driving/apprtc-rerun-2017-09-07
    ATT-LTE-driving/apprtc-svc-2s-3t
    ATT-LTE-driving/skype
    TMobile-UMTS-driving/salsify-1
    TMobile-UMTS-driving/facetime
    TMobile-UMTS-driving/hangouts
    TMobile-UMTS-driving/apprtc
    TMobile-UMTS-driving/apprtc-svc-2s-3t
    TMobile-UMTS-driving/skype
    12mbps/salsify-1
    12mbps/facetime-on-off
    12mbps/hangouts-on-off
    12mbps/apprtc-rerun-2017-09-07-onoff
    12mbps/apprtc-svc-2s-3t-onoff
    12mbps/skype-on-off    
)

NAMES=(
    Salsify
    Facetime
    Hangouts
    WebRTC
    WebRTC-SVC
    Skype
    Salsify
    Facetime
    Hangouts
    WebRTC
    WebRTC-SVC
    Skype
    Salsify
    Facetime
    Hangouts
    WebRTC
    WebRTC-SVC
    Skype
    Salsify
    Facetime
    Hangouts
    WebRTC
    WebRTC-SVC
    Skype
)

TRACES=(
    Verizon
    Verizon
    Verizon
    Verizon
    Verizon
    Verizon
    'AT&T'
    'AT&T'
    'AT&T'
    'AT&T'
    'AT&T'
    'AT&T'
    T-Mobile
    T-Mobile
    T-Mobile
    T-Mobile
    T-Mobile
    T-Mobile
    'Lossy Link'
    'Lossy Link'
    'Lossy Link'
    'Lossy Link'
    'Lossy Link'
    'Lossy Link'
)

for i in $(seq 0 24); do
    path=${LIST[i]}
    name=${NAMES[i]}
    trace=${TRACES[i]}

    cd $path/video3_720p60
    output=$(../../../../scripts/table.py  video3_720p60.analysis.csv video3_720p60.playback.csv downlink.log)
    echo $name '&' $trace '&' $output
    cd ../../..
done
