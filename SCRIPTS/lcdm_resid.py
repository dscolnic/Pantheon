import numpy as np
import matplotlib.pyplot as plt
import array
import math
from astropy.cosmology import FlatLambdaCDM
cosmo = FlatLambdaCDM(H0=70, Om0=0.30)
import wmom
import string
import matplotlib
import linef

import matplotlib
import plotsetup
from matplotlib import gridspec
import matplotlib.ticker as ticker
plotsetup.halfpaperfig()


gs1 = gridspec.GridSpec(1,2)
gs1.update(bottom=0.5, top=0.95, hspace=0.0)
ax1= plt.subplot(gs1[0])
ax2= plt.subplot(gs1[1])

gs1 = gridspec.GridSpec(1,1)
gs1.update(bottom=0.1, top=0.36, hspace=0.0)
ax3= plt.subplot(gs1[0])



#list1, idsurvey, z1,x11,c1,mu1, mu1e = np.loadtxt('wc0a.fitres', delimiter=' ', usecols=(0,3, 6,17,19,35,37), unpack=True, dtype='string', skiprows=12)
#list1, idsurvey, z1,x11,c1,mu1, mu1e = np.loadtxt('wc0a.fitres', delimiter=' ', usecols=(0,3, 6,16,17,31,33), unpack=True, dtype='string', skiprows=12)                               
#list1, idsurvey, z1,x11,c1,mu1, mu1e = np.loadtxt('wc0a.fitres', usecols=(0,3, 7,17,19,34,35), unpack=True, dtype='string', skiprows=12)
#list1, idsurvey,z1, mass1,x11,c1,mu1, mu1e,mures1 = np.loadtxt('../DATA/SALT2mu_fitopt.fitres', usecols=(0,3, 7,13,20,22,37,39,41), unpack=True, dtype='string', skiprows=12)


name1='../DATA/SALT2mu/SALT2mu_fitoptg0.fitres'
name1='../DATA/SALT2mu_SNLS+SDSS+LOWZ+PS1_Scolnic2+HST/DS17/SALT2mu_FITOPT000_MUOPT000.FITRES'
headn=linef.linef(name1,'zCMB')
header1=headn
data1=np.genfromtxt(name1,skip_header=header1,names=True,comments='#')
cid1=np.genfromtxt(name1,skip_header=header1,usecols=(1),comments='#',dtype='str')[1:]
z1 = data1['zHD'].astype(float)
SNRMAX11=data1['SNRMAX1'].astype(float)
x11 = data1['x1'].astype(float)
c1 = data1['c'].astype(float)
mb1= data1['mB'].astype(float)
NDOF1=data1['NDOF'].astype(float)
#TGAPMAX2=data1['TGAPMAX'].astype(float)
FITPROB1=data1['FITPROB'].astype(float)
PKMJD1=data1['PKMJD'].astype(float)
#RA2=data1['RA'].astype(float)
#DEC2=data1['DECL'].astype(float)
idsurvey=data1['IDSURVEY'].astype(float)
NDOF1=data1['NDOF'].astype(float)
PKMJDE1=data1['PKMJDERR'].astype(float)
mb1E=data1['mBERR'].astype(float)
c1E=data1['cERR'].astype(float)
x11E=data1['x1ERR'].astype(float)
mures1=data1['MURES'].astype(float)
mu1=data1['MU'].astype(float)
mu1e=data1['MUERR'].astype(float)
mumodel1=data1['MUMODEL'].astype(float)

name2='../DATA/SALT2mu/SALT2mu_fitoptc0.fitres'
name2='../DATA/SALT2mu_SNLS+SDSS+LOWZ+PS1_Scolnic2+HST/DS17/SALT2mu_FITOPT000_MUOPT001.FITRES'

header1=1
headn=linef.linef(name2,'zHD')
data2=np.genfromtxt(name2,skip_header=headn,names=True,comments='#')
cid2=np.genfromtxt(name2,skip_header=headn,usecols=(1),comments='#',dtype='str')[1:]

z2 = data2['zHD'].astype(float)
SNRMAX12=data2['SNRMAX1'].astype(float)
x12 = data2['x1'].astype(float)
c2 = data2['c'].astype(float)
mb2= data2['mB'].astype(float)
NDOF2=data2['NDOF'].astype(float)
#TGAPMAX2=data2['TGAPMAX'].astype(float)
FITPROB2=data2['FITPROB'].astype(float)
PKMJD2=data2['PKMJD'].astype(float)
#RA2=data2['RA'].astype(float)
#DEC2=data2['DECL'].astype(float)
idsurvey2=data2['IDSURVEY'].astype(float)
NDOF2=data2['NDOF'].astype(float)
PKMJDE2=data2['PKMJDERR'].astype(float)
mb2E=data2['mBERR'].astype(float)
c2E=data2['cERR'].astype(float)
x12E=data2['x1ERR'].astype(float)
mures2=data2['MURES'].astype(float)
mu2=data2['MU'].astype(float)
mu2e=data2['MUERR'].astype(float)
mumodel2=data2['MUMODEL'].astype(float)



uniqsurv=['54', '50', '53', '1', '5', '4', '106','100','106','15']
col=['b','g','r','c','m','y','r','g','m','b','g']
co2=0
pos2=[]
pos=[]
for i in range(1,299):
    pos2.append(i/10.0-5)
    pos.append(0/1.0)


                #6F
x=cosmo.luminosity_distance(z1).value
mu_syn1=5.0*(np.log10(x))+25.0
#mu_syn1=mumodel1
yy=mumodel1-mu_syn1
co=0
for x in yy:
    print z1[co], x
    co=co+1
#stop
x=cosmo.luminosity_distance(z2).value
mu_syn2=5.0*(np.log10(x))+25.0
#mu_syn2=mumodel2

uniqsurv=[100,4,15,1,0]
labels=['HST','SNLS','PS1','SDSS','LOW-Z']

#1,4,15,64,62,63,65,100,61,106
xx=(z1>0)
tempz=z1[xx]
tempmu=mu1[xx]-mu_syn1[xx]
tempmue=mu1e[xx]
print 'tempmu', tempmu, tempmue
wmean0,werr = wmom.wmom(tempmu, 1.0/np.power(tempmue,2), inputmean=None, calcerr=True, sdev=False)                                                                        
wmean0t,werrt = wmom.wmom(tempmu[z1<0.05], 1.0/np.power(tempmue[z1<0.05],2), inputmean=None, calcerr=True, sdev=False)
wmean0t2,werrt = wmom.wmom(tempmu[z1>0.05], 1.0/np.power(tempmue[z1>0.05],2), inputmean=None, calcerr=True, sdev=False)

print 'ww and lcdm', wmean0, wmean0t, wmean0t2        
#stop

xx=(z2>0)
tempz=z2[xx]
tempmu=mu2[xx]-mu_syn2[xx]
tempmue=mu2e[xx]
print 'tempmu', tempmu, tempmue
wmean1,werr = wmom.wmom(tempmu, 1.0/np.power(tempmue,2), inputmean=None, calcerr=True, sdev=False)
wmean1t,werrt = wmom.wmom(tempmu[z2<0.05], 1.0/np.power(tempmue[z2<0.05],2), inputmean=None, calcerr=True, sdev=False)

wmean1x,werrx = wmom.wmom(tempmu[z2>0.05], 1.0/np.power(tempmue[z2>0.05],2), inputmean=None, calcerr=True, sdev=False)

print 'ww and lcdm', wmean1, wmean1t, wmean1x
#stop
print 'wmean00', wmean0, wmean1


#stop
for i in range(0,len(uniqsurv)):

    uniqsu=uniqsurv[i]
    if (uniqsu != 0) & (uniqsu != 100): xx=np.where(idsurvey==uniqsu)
    if uniqsu == 0: xx=np.where((idsurvey!=4) & (idsurvey!=15) & (idsurvey!=1)&(z1<0.1))
    if uniqsu == 100: xx=np.where((idsurvey!=4) & (idsurvey!=15) & (idsurvey!=1)&(z1>0.1))
    tempz=z1[xx[0]]
    tempmu=mu1[xx[0]]-mu_syn1[xx[0]]
    tempmue=mu1e[xx[0]]
    wmean,werr = wmom.wmom(tempmu, 1.0/np.power(tempmue,2), inputmean=None, calcerr=True, sdev=False)
    
    if (uniqsu != 0) & (uniqsu != 100): xx=np.where(idsurvey==uniqsu)
    if uniqsu == 0: xx=np.where((idsurvey2!=4) & (idsurvey2!=15) & (idsurvey2!=1)&(z2<0.1))
    if uniqsu == 100: xx=np.where((idsurvey2!=4) & (idsurvey2!=15) & (idsurvey2!=1)&(z2>0.1))
    tempz=z2[xx[0]]
    tempmu=mu2[xx[0]]-mu_syn2[xx[0]]
    tempmue=mu2e[xx[0]]
    wmean2,werr = wmom.wmom(tempmu, 1.0/np.power(tempmue,2), inputmean=None, calcerr=True, sdev=False)
    
    print 'ok',uniqsu, wmean, wmean2, wmean-wmean0+wmean2-wmean1
    ax1.errorbar((wmean-wmean0+wmean2-wmean1)/2.0,co2, xerr=werr, fmt=col[co2]+'o', ecolor=col[co2],label=labels[i])
    
    ax1.text((wmean-wmean0+wmean2-wmean1)/2.0,co2,labels[i],fontdict={'fontsize':10},color=col[co2])
    co2=co2+1
    print i, 'wmean', wmean, co2, werr

#stop
ax1.set_xticklabels(['','-0.04','','0.0','','0.04'])

#plt.legend(loc='lower left',prop={'size':8})
#plt.errorbar(z, mu-mu_syn, yerr=mue, fmt='o')
line, = ax1.plot(pos, pos2, lw=2, color='black')

ax1.set_xlim(-.05,.05)
ax1.set_ylim(-1,5.5)
#ax1.set_ylabel('Samples')
#ax1.set_xlabel('Mean Residuals '+r'$\Delta \mu$'+' (mag)',labelpad=-.75)
ax1.set_xlabel(r'$\Delta \mu$'+' (mag)',labelpad=-.75)

plt.gca().yaxis.set_major_locator(plt.NullLocator())

#candels_lcparams
#candels_hubble_0a.fitres.cospar
vec=['a','b','c','d','e','f','g','h','i','j','k','l','m']

#onek_colormass_none_sup_omw [0, '-1.0106786E+00', '3.0069144E-02', '3.0956975E-01', '9.8917210E-03', '0', '0', '1.1163266E+03']
#labels=['SNLS','PS1','SDSS','CSP','CFA4','CFA3','CFA1-2','LOWZ','HST']

survs=['onek_colormass_sup_omw','onek_colormass_sup_u_SNLS_omw','onek_colormass_sup_u_PS_omw','onek_colormass_sup_u_SDSS_omw','onek_colormass_sup_u_CSP_omw','onek_colormass_sup_u_CFA4_omw','onek_colormass_sup_u_CFA3_omw','onek_colormass_sup_u_CFA12_omw','onek_colormass_sup_u_lowz_omw','onek_colormass_sup_u_hst_omw']

survs2=['onek_colormass_sup_stat_omw','onek_colormass_sup_u_SNLS_stat_omw','onek_colormass_sup_u_PS_stat_omw','onek_colormass_sup_u_SDSS_stat_omw','onek_colormass_sup_u_CSP_stat_omw','onek_colormass_sup_u_CFA4_stat_omw','onek_colormass_sup_u_CFA3_stat_omw','onek_colormass_sup_u_CFA12_stat_omw','onek_colormass_sup_u_lowz_stat_omw','onek_colormass_sup_u_hst_stat_omw']

survs2=['DS17_ALL', 'DS17_MHST','DS17_MSNLS', 'DS17_MPS1', 'DS17_MSDSS', 'DS17_MLOWZ']
survs=['DS17_ALL_sys','DS17_MHST_sys', 'DS17_MSNLS_sys', 'DS17_MPS1_sys', 'DS17_MSDSS_sys', 'DS17_MLOWZ_sys']

#survs=['Tutor','Tutor_MLOWZ','Tutor_MSDSS','Tutor_MSNLS','Tutor_MPS1']
#labels=['SNLS','PS1','SDSS','LOW-Z']



#tutor_chains.results
survvar,wvar,wverr = np.loadtxt('/project/rkessler/dscolnic/cosmomc_s16/survcomb.txt', usecols=(0,2,3), unpack=True, dtype='string')
xx=(survvar==survs[0])
w1=wvar[xx]
w1e=wverr[xx]
w1=w1[0][1:-2]
w1e=w1e[0][1:-2]
w1x = float(w1)
w1ex = float(w1e)

xx=(survvar==survs2[0])
w2=wvar[xx]
w2e=wverr[xx]
w2=w2[0][1:-2]
w2e=w2e[0][1:-2]
w2x = float(w2)
w2ex = float(w2e)
print w2ex
co2=0
erref1=[]
erref2=[w1ex]
erref3=[]
erref1w=[]
erref2w=[w2ex]
erref3w=[]
for i in range(1,len(uniqsurv)+1):
   xx=(survvar==survs[i])
   w1=wvar[xx]
   w1e=wverr[xx]
   w1=w1[0][1:-2]
   w1e=w1e[0][1:-2]
   w1=float(w1)
   w1e=float(w1e)
   eb1=ax2.errorbar(w1-w1x,co2*1.5, xerr=w1e, fmt=col[co2]+'o', ecolor=col[co2],label=labels[i-1])
   eb1[-1][0].set_linestyle('--') #eb1[-1][0] is the LineCollection objects of the errorbar lines
   
   ax2.text(w1-w1x,co2*1.5+.3,labels[i-1],fontdict={'fontsize':10},color=col[co2])

   xx=(survvar==survs2[i])
   w2=wvar[xx]
   w2e=wverr[xx]
   w2=w2[0][1:-2]
   w2e=w2e[0][1:-2]
   w2=float(w2)
   w2e=float(w2e)
   #w2e 0.042621879 0.03925187
   ax2.errorbar(w2-w2x,co2*1.5+0.2, xerr=w1e, fmt=col[co2]+'o', ecolor=col[co2],label=labels[i-1],ls='-.')
   #plt.set_linestyle('--')
   #plt.text(w2-w2x,co2,labels[i-1],fontdict={'fontsize':10},color=col[co2])
                           
   
   erref1=np.append(erref1,co2)
   if w1e>w1ex: erref2=np.append(erref2,np.sqrt(w1e**2))
   if w1e<=w1ex: erref2=np.append(erref2,w1ex)
   erref3=np.append(erref3,labels[i-1])

   erref1w=np.append(erref1w,co2)
   if w2e>w2ex: erref2w=np.append(erref2w,np.sqrt(w2e**2))
   if w2e<=w2ex: erref2w=np.append(erref2w,w2ex)
   erref3w=np.append(erref3w,labels[i-1])
   print 'w2e ', w2ex, w2e
   print erref2w
   print 'survey', survs[i], np.sqrt(w1e**2-w1ex**2), np.sqrt(w2e**2-w2ex**2), w1e, w1ex, w2e, w2ex
   #w2e 0.042621879 0.03925187
   
   co2=co2+1

#plt.legend(loc='lower left',prop={'size':8})
line, = ax2.plot(pos, pos2, lw=2, color='black')

line,= ax2.plot([-0.132,-.115],[6.5,6.5],color='black',linewidth=2)
line,= ax2.plot([-0.132,-.115],[7.1,7.1],color='black',linestyle='--',linewidth=2)

ax2.text(-0.107,6.4,' Stat',fontdict={'fontsize':10},color='black')
ax2.text(-0.107,7.0,' Stat+Sys',fontdict={'fontsize':10},color='black')
ax2.set_xticklabels(['','-0.1','','0.0','','0.1'])    
ax2.set_xlim(-.145,.145)
ax2.set_ylim(-1,8)
plt.gca().yaxis.set_major_locator(plt.NullLocator())
#ax2.set_ylabel('Samples')
#ax2.set_xlabel(r'$\Delta w$'+' after removing sample',labelpad=-.75)
ax2.set_xlabel(r'$\Delta w$'+' w/o sample',labelpad=-.75)

#erref2
#erref2w

line, =ax3.plot([0,0.1],[.1,.1],color='black',linewidth=2)
line, =ax3.plot([0,.1],[.2,.2],color='black',linestyle='--',linewidth=2)


co2=0
print erref2
print erref2w
#stop
ax3.text(0.0243,0.09,'Stat+Sys',fontdict={'fontsize':10},color='black',rotation=0)
ax3.text(0.0268,0.18,'Stat',fontdict={'fontsize':10},color='black',rotation=0)
print erref3
#check=['HST' 'SNLS' 'PS1' 'SDSS' 'LOW-Z']
erref3=np.append('NOCUT',erref3)
cv=[-.001,-.0005,0,0,.0005,0.0002]
cv2=[-.001,-.000,0,-.001,.000,0.000]
col=['black','b','g','r','c','m','y','r','g','m','b','g']

print erref2w
erref2w[0]=erref2w[0]-.0002
#stop
textsize=[6,10,10,10,10,8]
for i in range(1,len(uniqsurv)+2):
   ax3.text(erref2[i-1]+cv2[i-1],0.03,erref3[i-1],fontdict={'fontsize':textsize[i-1]},color=col[co2],rotation=90)
   ax3.text(erref2w[i-1]+cv[i-1],0.32,erref3[i-1],fontdict={'fontsize':textsize[i-1]},color=col[co2],rotation=90)
   line, = ax3.plot([erref2[i-1],erref2[i-1]],[0.08,0.12], lw=2, color=col[co2])
   line, = ax3.plot([erref2w[i-1],erref2w[i-1]],[0.18,0.22], lw=2, color=col[co2])
   
   co2=co2+1

print 'erref1', erref1
print 'erref2', erref2

#ax3.barh(erref1+.3,erref2, align='center',height=0.2,color=col,edgecolor='none')
#ax3.barh(erref1w,erref2w, align='center',height=0.2,edgecolor=col,hatch='/',color='w')

#eb2[-1][0].set_linestyle('--') #eb1[-1][0] is the LineCollection objects of the errorbar lines

print 'erref',erref1w, erref2w

#plt.set_yticks(erref1, ('Tom', 'Dick', 'Harry', 'Slim', 'Jim'))
#plt.axvline(0,color='k',lw=3)   # poor man's zero level

#line, ax3.plot([0.0375,0.04],[-0.2,-0.2],color='black',linewidth=2)
#line, plt.plot([0.031,0.035],[1.8,1.8],color='black',linestyle='/',linewidth=2)

#ax3.text(0.038,0.5,'/ / / / Stat',fontdict={'fontsize':10},color='black')
#ax3.text(0.041,-0.3,' Stat+Sys',fontdict={'fontsize':10},color='black')
#ax3.text(0.031,0.5,' Stat Only',fontdict={'fontsize':10},color='black')


ax3.set_xlim(0.029,.055)
ax3.set_ylim(-.12,0.38)
#ax3.set_ylabel('Samples')
ax3.yaxis.set_major_locator(plt.NullLocator())
ax2.yaxis.set_major_locator(plt.NullLocator())
ax1.yaxis.set_major_locator(plt.NullLocator())

#ax3.set_xlabel('Quadrature difference in '+r'$\sigma_w$'+' w/o a sample',labelpad=-.25)
ax3.set_xlabel(r'$\sigma_w$',labelpad=-.25)

ax3.xaxis.set_major_locator(ticker.MultipleLocator(0.01))
#ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.01))

plt.show()


plt.savefig('lcdm_resid.png')
