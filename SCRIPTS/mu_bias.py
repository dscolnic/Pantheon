import numpy as np
import matplotlib.pyplot as plt
import array
import math
from astropy import cosmology as cosmo
import wmom
from scipy.interpolate import interp1d
import matplotlib
import linef


import plotsetup
from matplotlib import gridspec
import matplotlib.ticker as ticker
plotsetup.halfpaperfig()

#malmquist_tree12z.txt
#Restetal.fitres
#SALT2mu_PS1.M0DIF
#SALT2mu_PS1_conv.M0DIF
#SALT2mu_Rest_pre.M0DIF

#SALT2mu/SALT2mu_fitoptgs_ps1
#SALT2mu/SALT2mu_fitoptgos_ps1
headn=linef.linef('../DATA/SALT2mu/SALT2mu_fitoptgos_ps1.M0DIF','VARN')
z1,muerr1,mures1 = np.loadtxt('../DATA/SALT2mu/SALT2mu_fitoptgos2_ps1.M0DIF', usecols=(4,6,5), unpack=True, dtype='string', skiprows=headn+1)
z1b,muerr1b,mures1b = np.loadtxt('../DATA/SALT2mu/SALT2mu_fitoptgs2_ps1.M0DIF', usecols=(4,6,5), unpack=True, dtype='string', skiprows=headn+1)

headn=linef.linef('SALT2mu/SALT2mu_Rest_pre.M0DIF','VARN')
z2,muerr2,mures2 = np.loadtxt('SALT2mu/SALT2mu_Rest_pre.M0DIF', usecols=(2,4,3), unpack=True, dtype='string', skiprows=headn+1)
z2b,muerr2b,mures2b = np.loadtxt('SALT2mu/SALT2mu_Rest_pre.M0DIF', usecols=(2,4,3), unpack=True, dtype='string', skiprows=headn+1)


z2c,mucorr2=np.loadtxt('malmquist_tree12z.txt',usecols=(0,1), unpack=True, dtype='string')
#z2,mures2  = np.loadtxt('../DATA/SALT2mu/SALT2mu_fitoptg0.fitres', usecols=(8,40), unpack=True, dtype='string', skiprows=16)
#z4,mures4  = np.loadtxt('../DATA/SALT2mu/SALT2mu_fitoptc0.fitres', usecols=(8,40), unpack=True, dtype='string', skiprows=16)


z1 = z1.astype(float)
z2=z2.astype(float)
z1b=z1b.astype(float)
z2b=z2b.astype(float)
z2c=z2c.astype(float)

mures1=mures1.astype(float)
mures1b=mures1b.astype(float)
mures2=mures2.astype(float)
mures2b=mures2b.astype(float)


muerr1=muerr1.astype(float)
muerr1b=muerr1b.astype(float)
muerr2=muerr2.astype(float)
muerr2b=muerr2b.astype(float)

xx=(muerr1<0.2)
z1=z1[xx]; muerr1=muerr1[xx]; mures1=mures1[xx]
xx=(muerr1b<0.2)
z1b=z1b[xx]; muerr1b=muerr1b[xx]; mures1b=mures1b[xx]


#mucorr1=mucorr1.astype(float)
mucorr2=mucorr2.astype(float)
                    
#muerrcorr1=muerrcorr1.astype(float)


ff=interp1d(z2c,mucorr2)
print 'z2b', z2b
print ff(z2b)
mures2b=mures2b-ff(z2b)
#print muerrcorr1

gs1 = gridspec.GridSpec(2, 1)
gs1.update(bottom=0.15, top=0.95, hspace=0.05)
ax1= plt.subplot(gs1[0])
ax2= plt.subplot(gs1[1])
ax=[ax1,ax2]

lx=np.arange(0,3,.3)
ax[0].errorbar(z1, mures1, yerr=muerr1, fmt='ko', ecolor='black', color='black',label='D15 Data',marker='o')
ax[0].errorbar(z2, mures2, yerr=muerr2, fmt='ko', ecolor='red', color='red',label='D15 Data',marker='D',alpha=0.5)
line, = ax[0].plot(lx,lx*0, lw=2)
ax[0].set_xlim(0,.7)
ax[0].set_ylim(-.19,.39)

ax[1].errorbar(z1b, mures1b, yerr=muerr1b, fmt='ko', ecolor='black', color='black',label='D15 Data',marker='o')
ax[1].errorbar(z2b, mures2b, yerr=muerr2b, fmt='ko', ecolor='red', color='red',label='D15 Data',marker='D',alpha=0.5)
line, = ax[1].plot(lx,lx*0, lw=2)
ax[1].set_xlim(0,.7)
ax[1].set_ylim(-.19,.39)

#plt.gca().add_artist(l1)

ax1.set_xticklabels(['','','','','','','',''])
plt.xlabel('z')
ax[0].set_ylabel(r'$\mu-\mu_{\rm ref}$ (mag)')
ax[1].set_ylabel(r'$\mu-\mu_{\rm ref}$ (mag)')

ax[0].text(0.05,0.3,"R14", color='red')
ax[0].text(0.05,0.235,"This Work", color='black')

ax[1].text(0.05,0.3,"R14", color='red')
ax[1].text(0.05,0.235,"This Work", color='black')

ax[0].text(0.3,0.3,"Before Distance", color='blue')
ax[0].text(0.3,0.255,"Bias Corrections", color='blue')

ax[1].text(0.3,0.3,"After Distance", color='blue')
ax[1].text(0.3,0.255,"Bias Corrections", color='blue')



plt.show()


plt.savefig('mu_bias.png')

asdf
