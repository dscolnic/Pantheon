import numpy as np
import matplotlib.pyplot as plt
import array
import math
from astropy.cosmology import FlatLambdaCDM
import matplotlib
from matplotlib import gridspec
import plotsetup
import linef
plotsetup.halfpaperfig()


cosmo = FlatLambdaCDM(H0=70, Om0=0.3)

gs1 = gridspec.GridSpec(2, 1)
gs1.update(hspace=0.04,bottom=0.13,top=0.92)
ax2= plt.subplot(gs1[1])
ax1= plt.subplot(gs1[0])
ax=[ax1,ax2]
pos=[]
for i in range(1,2999):
    pos.append(i/1000.0)


headn=linef.linef('../DATA/SALT2mu/SALT2mu_fitoptg0.fitres','zCMB')
data1=np.genfromtxt('../DATA/SALT2mu/SALT2mu_fitoptg0.fitres',skip_header=headn,names=True,comments='#')
cid=np.genfromtxt('../DATA/SALT2mu/SALT2mu_fitoptg0.fitres',skip_header=headn,usecols=(1),comments='#',dtype='str')[1:]
z1 = data1['zCMB'].astype(float)
mu1=data1['MU'].astype(float)
mu1e = data1['MUERR'].astype(float)
idsurvey=data1['IDSURVEY'].astype(float)                                    






x=cosmo.luminosity_distance(pos).value
y=5.0*(np.log10(x))+25.0

x=cosmo.luminosity_distance(z1).value
mu_syn=5.0*(np.log10(x))+25.0
line, = ax[0].plot(pos, y, lw=2)
line, = ax[1].plot(pos, y*0, lw=2)


survey=1
tempsurv=[]
tempz=[]
tempmu=[]
tempmue=[]
uniqsurv=set(idsurvey)
uniqsurv=['61','62','63','64','65','66', '5','1', '4', '101','106','100','15']
uniqsurv=[61,62,63,64,65,66, 5,1, 4, 101,106,100,15]
labels=['CFA1','CFA2','CFA3S','CFA3K','CFA4p1','CFA4p2','CSP','SDSS','SNLS','SCP','CANDELS\n+CLASH','GOODS','PS1']
xpos=[0.018,0.018,0.018,0.018,0.018,0.018,0.018,
      .08,.27,1.2,.69,.87,
      .28]
ypos=[37,38.2,39.4,40.6,41.8,43,44.2,
      41.0,43.9,43.1,40.5,46
      ,38.4]
fo=[10,10,10,10,10,10,10,16,16,10,10,10,16]
col=['Red', 'orangered','indianred','RosyBrown','LightSalmon','Pink','DarkKhaki','Green','DimGray','DarkRed','DarkBlue','Purple','Blue']
#col=['DimGray','DimGray','DimGray','DimGray','DimGray','DimGray','DimGray','DimGray','DimGray','DimGray','DimGray','DimGray','DimGray''DimGray','DimGray','DimGray','DimGray','DimGray','DimGray','DimGray','DimGray','DimGray','DimGray']
print len(uniqsurv),len(xpos), len(ypos), len(labels), len(fo), len(col)
#13 15 21 12 14 16

#stop
co2=0
for uniqsu in uniqsurv:
        print uniqsu
        xx=np.where((idsurvey==uniqsu))        
        print len(xx[0])
        if len(xx[0]>1):
            print 'co2', len(xx[0])
            tempz=z1[xx[0]]
            tempmu=mu1[xx[0]]
            tempmu2=mu1[xx[0]]-mu_syn[xx[0]]
            tempmue=mu1e[xx[0]]
            cide=cid[xx[0]]
            #print 'col2', co2, col[co2],len(col)
            ax[0].errorbar(tempz, tempmu, yerr=tempmue, fmt='o', color=col[co2],ecolor=col[co2],alpha=0.3)
            ax[0].text(xpos[co2],ypos[co2],labels[co2],fontdict={'fontsize':fo[co2]}, color=col[co2])
            ax[1].errorbar(tempz, tempmu2, yerr=tempmue, fmt='o', color=col[co2],ecolor=col[co2],alpha=0.3)
            print cide[np.absolute(tempmu2/tempmue)>3], tempmu2[np.absolute(tempmu2/tempmue)>3]/tempmue[np.absolute(tempmu2/tempmue)>3]
            print np.amin(tempmu2)
            
            #print 'errorbar', tempz, tempmu2
        co2=co2+1
    #stop

#stop
bins = np.linspace(0, 1, 11)
bins=np.append(bins,[1.15,1.4,1.7,2.3])

digitized = np.digitize(z1, bins)
bin_means = [mu1[digitized == i].mean() for i in range(0, len(bins))]
bin_z = [z1[digitized == i].mean() for i in range(0, len(bins))]
bin_std = [np.std(mu1[digitized == i])/np.sqrt(len(mu1[digitized == i])) for i in range(0, len(bins))]

        #ax1.errorbar(bin_z, bin_means, yerr=bin_std, fmt='ko', ecolor='k')
        
        
    #plt.annotate('local max', xy=(.5, 43), xytext=(3, 1.5),
        #            arrowprops=dict(facecolor='black', shrink=0.05),
        #            )
    
        
ax[0].set_ylabel('Distance Modulus (mag)')
ax[0].set_xlim(0.008,2.4)
ax[0].set_ylim(32.6,47.5)

ax[0].set_xscale('log')
#ax[0].set_xscale('log')

digitized = np.digitize(z1, bins)
bin_means = [(mu1[digitized == i]-mu_syn[digitized == i]).mean() for i in range(0, len(bins))]
bin_z = [z1[digitized == i].mean() for i in range(0, len(bins))]
bin_std = [np.std(mu1[digitized == i]-mu_syn[digitized == i])/np.sqrt(len(mu1[digitized == i])) for i in range(0, len(bins))]

#ax2.errorbar(bin_z, bin_means, yerr=bin_std, fmt='ko', ecolor='k')
headn=linef.linef('../DATA/SALT2mu_SNLS+SDSS+LOWZ+PS1_Scolnic2+HST/DS17/SALT2mu_FITOPT'+str('000')+'_MUOPT'+str('000')+'.M0DIF','VARN')
z1,mures, murese = np.loadtxt('../DATA/SALT2mu_SNLS+SDSS+LOWZ+PS1_Scolnic2+HST/DS17/SALT2mu_FITOPT'+str('000')+'_MUOPT'+str('000')+'.M0DIF', usecols=(4,5,6), unpack=True, dtype='string', skiprows=headn+1)
z1 = z1.astype(float)
mures1 = mures.astype(float)
murese1 = murese.astype(float)

z2,mures2, murese2 = np.loadtxt('../DATA/SALT2mu_SNLS+SDSS+LOWZ+PS1_Scolnic2+HST/DS17/SALT2mu_FITOPT'+str('000')+'_MUOPT'+str('001')+'.M0DIF', usecols=(4,5,6), unpack=True, dtype='string', skiprows=headn+1)
z2 = z2.astype(float)
mures2 = mures2.astype(float)
murese2 = murese2.astype(float)

mures=(mures1+mures2)*.5
murese=(murese1+murese2)*.5


line, = ax[1].plot(pos, y*0, lw=2,color='black')

ax[1].errorbar(z1, mures, yerr=murese, fmt='o', color='yellow',ecolor='yellow')
ax[1].errorbar([0.0997],[5*np.log(40)+25], yerr=[2*.08],color='green', ecolor='green', fmt='o')
ax[1].errorbar([0.0997],[5*np.log(50)+25], yerr=[2*.04],color='green', ecolor='green', fmt='o')

ax[1].set_xlim(0.008,2.4)


#ax[1].set_xlim(0.01,2)
#ax[1].set_xlim(0.008,0.1)

ax[1].set_xscale('log')
ax[1].set_ylim(-0.99,0.99)
ax[1].set_xlabel('z')
ax[1].set_ylabel('Hubble Res. (mag)')

ax1.set_xticks([0.01,0.1,1.0])
ax1.set_xticklabels(['','',''])
ax2.set_xticks([0.01,0.1,1.0])
ax2.set_xticklabels(['0.01','0.10','1.0'])

# these are matplotlib.patch.Patch properties
props = dict(boxstyle='round', facecolor='black', alpha=0.5)

# place a text box in upper left in axes coords
ax2.text(0.4, -0.8, 'Binned Distance Residuals', fontsize=6,color='yellow', bbox=props)

plt.show()
    
plt.savefig('hubble.png')
    
