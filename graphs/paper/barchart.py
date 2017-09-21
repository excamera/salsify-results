#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import os

# parse the data
TRACES = ['verizon-lte', 'att-lte', 'tmobile-umts', 'on-off']
#TRACES = ['verizon-lte', 'att-lte', 'on-off']
DATA = []
for trace in TRACES:    
    with open(trace+'.list', 'r') as f:
        lines = f.read().strip().split('\n')
    QoE = []
    error = []
    for line in lines:
        dat_filename = os.path.join(trace,line.split(' ')[1]+'.dat')

        with open(dat_filename, 'r') as ff:
            print(dat_filename)
            p95_delay, _, _, mean_ssim, _, _ = ff.read().strip().split('\n')[-1].split(' ')
            #_, _, p95_delay, mean_ssim, _, _ = ff.read().strip().split('\n')[-1].split(' ')
            p95_delay = float(p95_delay)
            mean_ssim = float(mean_ssim)

            QoE.append(max(-0.000639*p95_delay + 0.062275*mean_ssim + 3.296, 1))
            error.append(0.0000731*p95_delay + 0.02*mean_ssim + 0.307)

    DATA.append((QoE, error))

print(DATA)

QoEs = []
errors = []
for i in range(8):
    systemq = []
    systeme = []
    for j in range(len(DATA)):
        q = DATA[j][0][i]
        e = DATA[j][1][i]

        systemq = [q] + systemq
        systeme = [e] + systeme

    QoEs.append(systemq)
    errors.append(systeme)

N = len(TRACES)

# plot the data
ind = np.arange(N)  # the x locations for the groups
width = 0.125       # the width of the bars
space = 0.05

fig, ax = plt.subplots(figsize=(6.775,5))
# rects1 = ax.bar(ind, QoEs[6], width-space, color='#333333', yerr=errors[6])
# rects2 = ax.bar(ind + width, QoEs[4], width-space, color='#DF006F', yerr=errors[4])
# rects3 = ax.bar(ind + 2*width, QoEs[2], width-space, color='#37A313', yerr=errors[2])
# rects4 = ax.bar(ind + 3*width, QoEs[3], width-space, color='#7E4CB6', yerr=errors[3])
# rects5 = ax.bar(ind + 4*width, QoEs[0], width-space, color='#F26822', yerr=errors[0])
# rects6 = ax.bar(ind + 5*width, QoEs[1], width-space, color='#AC4F1F', yerr=errors[1])
# rects7 = ax.bar(ind + 6*width, QoEs[7], width-space, color='#1A95C2', yerr=errors[7])

rects1 = ax.barh(ind, QoEs[6], width-space, color='#333333', label='Salsify-1')
rects2 = ax.barh(ind + width, QoEs[4], width-space, color='#DF006F', label='Salsify-1')
rects3 = ax.barh(ind + 2*width, QoEs[2], width-space, color='#37A313', label='Salsify-1')
rects4 = ax.barh(ind + 3*width, QoEs[3], width-space, color='#7E4CB6', label='Salsify-1')
rects5 = ax.barh(ind + 4*width, QoEs[0], width-space, color='#F26822', label='Salsify-1')
rects6 = ax.barh(ind + 5*width, QoEs[1], width-space, color='#AC4F1F', label='Salsify-1')
rects7 = ax.barh(ind + 6*width, QoEs[7], width-space, color='#1A95C2', label='Salsify-1')

# add some text for labels, title and axes ticks
ax.set_ylabel('Estimated QoE')
ax.set_xlabel('Network Trace')
ax.set_title('Predicted QoE Score')

ax.set_xticks([1,2,3,4,5])
ax.set_yticks(ind + 3*width )

#ax.set_yticklabels(('Lossy Link', 'AT&T', 'Verizon'))
ax.set_yticklabels(('Lossy Link', 'T-Mobile', 'AT&T', 'Verizon'))
plt.axis([0.9, 5, None, None])

# ax.legend((rects1[0], rects2[0], rects3[0], rects4[0], rects5[0], rects6[0], rects7[0]),
#           ('Salsify-1', 'Salsify-2', 'Facetime', 'Hangouts', 'WebRTC', 'WebRTC-SVC', 'Skype'), ncol=4)

def autolabel(rects):
    count = 0
    for rect in rects:
        if count != 3:
            count += 1
            continue
        
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() + 0.1, rect.get_y() - 0.05,
                rect.get_label(),
                ha='center', va='bottom')
# autolabel(rects1)
# autolabel(rects2)
# autolabel(rects3)
# autolabel(rects4)
# autolabel(rects5)
# autolabel(rects6)
# autolabel(rects7)

plt.show()
