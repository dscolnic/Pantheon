#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 12:15:44 2017

@author: elizabethjohnson
"""

import numpy as np
from pylab import *
import matplotlib.pylab as plt

fig, ax1 = plt.subplots(1,1)

files = open("/project/rkessler/SN/SNDATA_ROOT/INTERNAL/PS1/S16Analysis/DATA/COSMO/sys_DS17f_G10_0.txt")
lines = files.readlines()
files.close()

data = []

for line in lines:
    if line.startswith('#'): continue
    c=line.rstrip().replace('INDEF','Nan').split()
    data.append([float(x) for x in c])



array = []
cnt = 0 
line = []

for i in range(0, len(data)):
    cnt += 1
    #print(cnt)
    line.append(data[i][0])
    if cnt % 40 == 0:
        cnt = 0
        if len(line) > 0:
            array.append(line)
        line = []
        
print(array)

#imshow(array, interpolation='nearest')  
 
## YOU CAN CHANGE THE COLORS BY EDITING "CMAP"
imgplot = plt.imshow(array, cmap='bone', vmin=-0.001, vmax=0.001)   
ax1.set_xticklabels(['', 0.01,'',0.1,'',.50,'',1.0,'',2.0])
ax1.set_yticklabels(['', 0.01,'',0.1,'',.50,'',1.0,'',2.0])
ax1.set_xlabel('z')
ax1.set_ylabel('z')

plt.colorbar()
plt.show()
plt.savefig('covplot.png')
