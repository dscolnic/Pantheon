import numpy as np
import matplotlib.pyplot as plt
import array
import math
from astropy import cosmology as cosmo
import matplotlib
import plotsetup
from matplotlib import gridspec
import matplotlib.ticker as ticker

plotsetup.halfpaperfig()

#NewDan100f-590005.LCPLOT.TEXT
#NewDan100f-590031.LCPLOT.TEXT
#PS1_DS15-110719.LCPLOT.TEXT
mjd1,flux1,fluxe1,flag1,filt1 = np.loadtxt('LCPLOT/PS1_DS15-520022.LCPLOT.TEXT', usecols=(2,3,4,5,6), unpack=True, dtype='string') 
mjd2,flux2,fluxe2,flag2,filt2 = np.loadtxt('LCPLOT/PS1_DS15-370394.LCPLOT.TEXT', usecols=(2,3,4,5,6), unpack=True, dtype='string')
mjd3,flux3,fluxe3,flag3,filt3 = np.loadtxt('LCPLOT/PS1_DS15-380040.LCPLOT.TEXT', usecols=(2,3,4,5,6), unpack=True, dtype='string')
zred=['0.12','0.33','0.68']
names=['PS1-10caz','PS1-10caz','PS1-10bzp']
names=['PS1-520022','PS1-370394','PS1-380040']
#380040
mjd1=mjd1.astype(float)
flux1=flux1.astype(float)
fluxe1=fluxe1.astype(float)

mjd2=mjd2.astype(float)
flux2=flux2.astype(float)
fluxe2=fluxe2.astype(float)

mjd3=mjd3.astype(float)
flux3=flux3.astype(float)
fluxe3=fluxe3.astype(float)


col=['b','r','c','y','m','y','r','g','m','b','g']

pos=[]



for i in range(1,299):
    pos.append(i-35)
pos2=[]

for i in range(1,299):
    pos2.append(0.0/100.0+0)

plt.figure(1)

gs1 = gridspec.GridSpec(3, 1)
gs1.update(bottom=0.15, top=0.95, hspace=0.05)
ax1= plt.subplot(gs1[0])
ax2= plt.subplot(gs1[1])
ax3= plt.subplot(gs1[2])



str2=['g','r','i','z']
for i in range(0,3):
    line, = ax1.plot(pos, pos2, lw=2,color='black')
    xx=np.where((filt1==str2[i]) & (flag1=='1')&(flux1!=0))
    print 'mjd1[xx[0]]', mjd1[xx[0]]
    ax1.errorbar(mjd1[xx[0]], flux1[xx[0]], yerr=fluxe1[xx[0]], fmt='ko', color=col[i])
    xx=np.where((filt1==str2[i]) & (flag1=='0')&(flux1!=0))
    line, = ax1.plot(mjd1[xx[0]], flux1[xx[0]], lw=2, color=col[i])

ax1.text(32,650,"z="+zred[0])
ax1.text(32,900,names[0])
ax1.yaxis.set_major_locator(ticker.MultipleLocator(300))

ax1.set_xlim(-30,60)
ax1.set_ylim(-15,1199.0)
#str2=['red','green','blue']                                                                                                           
proxy = [plt.Rectangle((0,0),1,1,fc = col[pc]) for pc in range(0,4)]
ax1.legend(fontsize=9,loc='upper left')

for i in range(0,4):
    line, = ax2.plot(pos, pos2, lw=2,color='black')
    print 'filt2', filt2
    xx=np.where((filt2==str2[i]) & (flag2=='1')&(flux2!=0))
    ax2.errorbar(mjd2[xx[0]], flux2[xx[0]], yerr=fluxe2[xx[0]], fmt='ko', color=col[i],label=str2[i])
    xx=np.where((filt2==str2[i]) & (flag2=='0')&(flux2!=0))
    line, = ax2.plot(mjd2[xx[0]], flux2[xx[0]], lw=2, color=col[i])
ax2.legend(fontsize=9,loc='upper left')

ax2.set_xlim(-30,60)
ax2.set_ylim(-15,299.0)
ax2.text(32,170,"z="+zred[1])
ax2.text(32,240,names[1])
ax2.set_ylabel("Flux")
ax2.yaxis.set_major_locator(ticker.MultipleLocator(100))

for i in range(0,4):
    line, = ax3.plot(pos, pos2, lw=2,color='black')
    xx=np.where((filt3==str2[i]) & (flag3=='1')&(flux3!=0))
    ax3.errorbar(mjd3[xx[0]], flux3[xx[0]], yerr=fluxe3[xx[0]], fmt='ko', color=col[i])
    xx=np.where((filt3==str2[i]) & (flag3=='0')&(flux3!=0))
    line, = ax3.plot(mjd3[xx[0]], flux3[xx[0]], lw=2, color=col[i])

ax3.set_xlim(-30,60)
ax3.set_ylim(-15,99.0)
ax3.set_xlabel('Observed Frame Days From Peak Brightness')
ax3.text(32,40,"z="+zred[2])
ax3.text(32,60,names[2])
ax3.yaxis.set_major_locator(ticker.MultipleLocator(20))


ax1.set_xticklabels(['','','','',''])
ax2.set_xticklabels(['','','','',''])

                    
plt.show()
plt.savefig('lcplot.png')

asdf
