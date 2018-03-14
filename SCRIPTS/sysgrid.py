import numpy as np
from astropy.cosmology import FlatwCDM
from astropy.cosmology import w0waCDM
from astropy.cosmology import FlatLambdaCDM
from astropy.cosmology import LambdaCDM
import matplotlib.pyplot as plt
from astropy import cosmology as cosmo
import wmom as wmom
import matplotlib
import linef
import matplotlib
import plotsetup
from matplotlib import gridspec
import matplotlib.ticker as ticker
plotsetup.halfpaperfig()

gs1 = gridspec.GridSpec(1,4)
gs1.update(bottom=0.6, top=0.95, hspace=0.0)
ax1= plt.subplot(gs1[0])
ax2= plt.subplot(gs1[1])
ax3= plt.subplot(gs1[2])                                                                                 
ax4= plt.subplot(gs1[3])

gs1 = gridspec.GridSpec(1,4)
gs1.update(bottom=0.34, top=0.57, hspace=0.0)
ax5= plt.subplot(gs1[0])
ax6= plt.subplot(gs1[1])
ax7= plt.subplot(gs1[2])
ax8= plt.subplot(gs1[3])

gs1 = gridspec.GridSpec(1,4)
gs1.update(bottom=0.1, top=0.31, hspace=0.0)
ax9= plt.subplot(gs1[0])
ax10= plt.subplot(gs1[1])
ax11= plt.subplot(gs1[2])
ax12= plt.subplot(gs1[3])

#ax13= plt.subplot(gs1[1,0])
#ax14= plt.subplot(gs1[1,1])
#ax15= plt.subplot(gs1[1,2])
#ax16= plt.subplot(gs1[1,3])

ax=[ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8,ax9,ax10,ax11,ax12]
ran=[0.04,0.04,0.04,0.04,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02]
headn=linef.linef('../DATA/SALT2mu_SNLS+SDSS+LOWZ+PS1_Scolnic2+HST/DS17/SALT2mu_FITOPT'+str('000')+'_MUOPT'+str('000')+'.M0DIF','VARN')
z1,mures, murese = np.loadtxt('../DATA/SALT2mu_SNLS+SDSS+LOWZ+PS1_Scolnic2+HST/DS17/SALT2mu_FITOPT'+str('000')+'_MUOPT'+str('000')+'.M0DIF', usecols=(4,5,6), unpack=True, dtype='string', skiprows=headn+1)
z1 = z1.astype(float)
mures1 = mures.astype(float)
murese1 = murese.astype(float)


#FITOPT: color #GLOBAL GROUP 1
#FITOPT: massstep #GLOBAL GROUP 1
#FITOPT: massevol #GLOBAL GROUP 1
#FITOPT: colorevol #GLOBAL GROUP 1


#p1=plt.errorbar(z1, mures, yerr=murese, fmt='ko', ecolor='black', color='black',label='D15 Data')
#xp=[0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3]
#yp=[0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3]
#syslabel=['SALT2 Cal','Beta Evol.','Intr Scat.','Selection',
# 'MW Ext.','Mass Split','Mass Evol.','Pec. Vel.',
#          'HST Cal', 'SDSS g','PS1 r','SNLS i','Supercal', 'SDSS r','PS1 i','SNLS z']
#r'$\beta$'+' Evol. & '
#$\gamma$'+' Evol. & '
#$m_{\rm step}$'+'Shift

syslabel=['SALT2 Cal',r'$\mathbf{\beta}$'+' Evol. ','Intr Scat.','Selection',
 'MW Ext.',r'$\mathbf{ m_{\rm step}}$'+' Shift',r'$\mathbf{\gamma}$'+' Evol. ','Pec. Vel.',
          'HST Cal', 'Supercal','PS1 r','SNLS i'];#,'Supercal', 'SDSS r','PS1 i','SNLS z']

#sysnum1=['001','012','000','000','011','000','000','013','012','015','037','046','084','016','038','047']
#sysnum2=['000','000','001','002','000','006','011','000','000','000','000','000','000','000','000','000']
#weights=[1,1,0.5,1,
#         1,1,1,1,
#         1,.5,.3,.5,.5,.5,.5,.5]
sysnum1=['001','012','000','000','011','000','000','013','012','084','037','046']
sysnum2=['000','000','001','002','000','006','011','000','000','000','000','000']
weights=[1,0.5,0.5,1,
                  1,1,1,1,
                  1,.5,.3,.5]

#sysnum=[1,84,85,86,
# 11,83,13,11,
#        28,15,37,50,29,16,38,51]
#sysnum=[1,11,12,86,83,84,85,15,28,37,51]
#syslabel=['SALT2 Cal','MW Ext','HST Cal','Int. Scat','Mass Split','Mass Evol','Color Evol','SDSS g','CSP B','PS1 r', 'SNLS z']
print len(sysnum1)
#stop
for x in range(0,len(sysnum1)):
    z2,mures2, murese2 = np.loadtxt('../DATA/SALT2mu_SNLS+SDSS+LOWZ+PS1_Scolnic2+HST/DS17/SALT2mu_FITOPT'+str(sysnum1[x])+'_MUOPT'+str(sysnum2[x])+'.M0DIF', usecols=(4,5,6), unpack=True, dtype='string', skiprows=headn+1)
    z2 = z2.astype(float)
    mures2 = mures2.astype(float)
    murese2 = murese2.astype(float)

    ax[x].errorbar(z1, (mures1-mures2)*weights[x], yerr=murese2*0, fmt='go', ecolor='g', alpha=.95)
    ax[x].set_ylim(-ran[x]*.99,ran[x]*.99)
    ax[x].set_xlim(0.005,1.7)
    ax[x].set_xscale('log')
    line, = ax[x].plot(np.arange(0,2,.1), np.arange(0,2,.1)*0.0, lw=2)
    if (x<8): ax[x].text(.01,-.88*ran[x], syslabel[x],fontdict={'fontsize':10}, color='black')
    if (x>7): ax[x].text(.01,-.88*ran[x], syslabel[x],fontdict={'fontsize':10}, color='black')
        
    ax[x].set_xticks([0.01,0.1,1.0])
    if (x<4): ax[x].yaxis.set_major_locator(ticker.MultipleLocator(0.02))
    if (x>3): ax[x].yaxis.set_major_locator(ticker.MultipleLocator(0.01))
    if (x>7): ax[x].yaxis.set_major_locator(ticker.MultipleLocator(0.01))
        
    if ((x!=0)&(x!=4)&(x!=8)&(x!=12)):
                     ax[x].set_yticklabels(['','','','','','',''])
    if (x<9):
         ax[x].set_xticklabels(['','','','',''])
    if (x>7):
        ax[x].set_xlabel('z',labelpad=-1)
        ax[x].set_xticklabels([' 0.01','0.1','1.0  ',''])
        #ax[x].set_xticklabels(['0.0','','0.5','','1.0'])
    #if ((x==8)|(x==12)):
    #    ax[x].set_yticklabels(['','-0.01','0.0','0.01',''])
    ax[x].tick_params('both', length=2, width=2, which='major')
    ax[x].tick_params('both', length=0, width=2, which='minor')
        
#plt.text(.2,-.13,r'$Omega_M=0.30,\Omega_{\Lambda}=.70,w=-1.0$',fontdict={'fontsize':20}, color='black')
#plt.text(.2,.1,r'$\Omega_M=0.25,\Omega_{\Lambda}=.75,w=-1.0$',fontdict={'fontsize':20}, color='orange')
#plt.text(.2,.13,r'$\Omega_M=0.30,\Omega_{\Lambda}=.70,w=-1.1$',fontdict={'fontsize':20}, color='red')
#plt.text(.2,.16,r'$\Omega_M=0.30,\Omega_{\Lambda}=.70,w=-1.0, w_a=-0.1$',fontdict={'fontsize':20}, color='blue')

#ax[1,0].text(-0.3,0.05, 'd(m-M) [Mag]',fontdict={'fontsize':18}, color='black',rotation=90)

ax[4].set_ylabel(r'$\Delta \mu_{\rm Sys}  - \Delta \mu_{\rm Baseline} $'+' [mag]',labelpad=-1)

#plt.ylabel('d(m-M) [Mag]', size=24)

plt.show()
plt.savefig('sysgrid.png')
#line, = plt.plot(range(1,150)/100.0,5.0*np.log(c1/c2), lw=2,color='red')
#plt.show()
#plt.savefig('wdemo1.png')
