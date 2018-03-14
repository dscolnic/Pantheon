import os
import string
import numpy as np


v1=open('vari_ps1m.tex','w')
hmass=open('/project/rkessler/dscolnic/PS1_analysis/ps1_mass.txt','r')
line1=hmass.readline()
line1s=line1.split()
v1.write('\\newcommand{\\masslow}{\ensuremath{'+line1s[0]+'}}\n')
v1.write('\\newcommand{\\masshigh}{\ensuremath{'+line1s[1]+'}}\n')
line1=hmass.readline()
line1s=line1.split()
v1.write('\\newcommand{\\hmass}{\ensuremath{'+line1s[0]+'}}\n')
v1.write('\\newcommand{\\hmerr}{\ensuremath{'+line1s[1]+'}}\n')
v1.close()
