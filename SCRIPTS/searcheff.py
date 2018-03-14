import numpy as np
import matplotlib.pyplot as plt
import array
import math
from astropy import cosmology as cosmo
import wmom
from scipy.interpolate import interp1d
from matplotlib import pyplot as pl
import weighted_moving_average as wma
import matplotlib
import plotsetup
from matplotlib import gridspec
import matplotlib.ticker as ticker
import linef
plotsetup.halfpaperfig()

#gs1 = gridspec.GridSpec(2, 1)
#gs1.update(bottom=0.15, top=0.95, hspace=0.05)
#ax1= plt.subplot(gs1[0])
#ax2= plt.subplot(gs1[1])



#malmquist_tree12z.txt
#Restetal.fitres
#SALT2mu_PS1.M0DIF
#SALT2mu_PS1_conv.M0DIF
#SALT2mu_Rest_pre.M0DIF

rmag,eff = np.loadtxt('../SIMS/spec_dave_r_e6.txt', usecols=(1,2), unpack=True, dtype='string', skiprows=2)
rmag = rmag.astype(float)
eff = eff.astype(float)






#fig, ax = plt.subplots(2,1)
fig, ax = plt.subplots(2,1, gridspec_kw = {'height_ratios':[2, 5]})
plt.subplots_adjust(hspace=0.26)

lx=np.arange(0,3,.3)
efferr1=np.append([1],eff[0:-1])
efferr2=np.append(eff[1:],[0])

line, = ax[0].plot(rmag,eff, lw=2,color='black')
#line, = ax[0].plot(rmag,efferr1, lw=2,color='green',alpha=0.5)
#line, = ax[0].plot(rmag,efferr2, lw=2,color='green',alpha=0.5)

ax[0].fill_between(rmag, efferr2, efferr1, alpha=0.2, edgecolor='#1B2ACC', facecolor='gray', linewidth=0, antialiased=True)


#ax[0].errorbar(rmag,eff, yerr=efferr, fmt='ko', ecolor='black', color='black',label='D16 Malm')
ax[0].set_xlim(17,24)
ax[0].set_ylim(0,1.15)

ax[0].set_xlabel('peak r mag',labelpad=-1)
ax[0].set_ylabel('Spec. Sel. Eff.')
#ax1.set_xticklabels(['','','','','','','',''])


#ax[0].text(21,0.8,"Nominal Selection",fontdict={'fontsize':20}, color='black')
#ax[0].text(21,0.55,r'$\pm 1\sigma$',fontdict={'fontsize':20}, color='green')


for i in range(0,4):
    if (i==0): name1='../SIMS/PS1_SINGLEu2/DS_smearG10_PS1_GRIDu_single/FITOPT000.FITRES'; betas=3.1
    if (i==1): name1='../SIMS/PS1_SINGLEu2/DS_smearC11_PS1_GRIDu_single/FITOPT000.FITRES'; betas=3.8
    if (i==2): name1='../SIMS/PS1_SINGLEu2/DS_smearG10_PS1_GRIDu_sysing/FITOPT000.FITRES'; betas=3.1
    if (i==3): name1='../SIMS/PS1_SINGLEu2/DS_smearC11_PS1_GRIDu_sysing/FITOPT000.FITRES'; betas=3.8

    
    header1=5
    header1=linef.linef(name1,'zCMB')
    data1=np.genfromtxt(name1,skip_header=header1,names=True,comments='#')
    cid1=np.genfromtxt(name1,skip_header=header1,usecols=(1),comments='#',dtype='str')[1:]
    z1 = data1['zCMB'].astype(float)
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
    idsurvey1=data1['IDSURVEY'].astype(float)
    NDOF1=data1['NDOF'].astype(float)
    PKMJDE1=data1['PKMJDERR'].astype(float)
    mb1E=data1['mBERR'].astype(float)
    c1E=data1['cERR'].astype(float)
    x11E=data1['x1ERR'].astype(float)
    simx11 = data1['SIM_x1'].astype(float)
    simc1 = data1['SIM_c'].astype(float)
    simmb1=data1['SIM_mB'].astype(float)
    mudiff=(mb1+0.14*x11-3.1*c1)-(simmb1+0.14*simx11-betas*simc1)
    muerr=np.sqrt(mb1E**2+(0.14**2)*(x11E**2)+(3.1**2)*(c1E**2)+.1**2)
    #muerr=1.0/muerr**2
    xx=((np.absolute(c1)<0.3)&(np.absolute(x11)<3)&(FITPROB1>0.001))
    z1=z1[xx]
    mudiff=mudiff[xx]
    muerr=muerr[xx]        

    if (i==0): bins1,model1 = wma.weighted_moving_average(z1,mudiff,step_size=0.0025,window_size=0.05,width=muerr)
    if (i==1): bins2,model2 = wma.weighted_moving_average(z1,mudiff,step_size=0.0025,window_size=0.05,width=muerr)
    if (i==2): bins1b,model1b = wma.weighted_moving_average(z1,mudiff,step_size=0.0025,window_size=0.05,width=muerr)
    if (i==3): bins2b,model2b = wma.weighted_moving_average(z1,mudiff,step_size=0.0025,window_size=0.05,width=muerr)

xx=((bins1>0.05)&(bins1<0.65)); bins1=bins1[xx]; model1=model1[xx];
xx=((bins2>0.05)&(bins2<0.65));bins2=bins2[xx]; model2=model2[xx];
xx=((bins1b>0.05)&(bins1b<0.65));bins1b=bins1b[xx]; model1b=model1b[xx];
xx=((bins2b>0.05)&(bins2b<0.65));bins2b=bins2b[xx]; model2b=model2b[xx];

print bins2,bins2b

print len(model1), len(model1b)
print len(model2), len(model2b)

#stop
line, = ax[1].plot(np.arange(0,1,.1),np.arange(0,1,.1)*0,lw=1,color='black',linestyle='--',alpha=.5)

line, = ax[1].plot(bins1,model1,lw=2,color='blue',label='G10 Bias')
line, = ax[1].plot(bins2,model2,lw=2,color='red',label='C11 Bias')
line, = ax[1].plot(bins1,(model1+model2)/2.0,lw=2,color='black',label='Average Bias')

ax[1].fill_between(bins1, model1+(model1-model1b), model1-(model1-model1b), alpha=0.2, edgecolor='#1B2ACC', facecolor='#089FFF', linewidth=0, linestyle='dashdot', antialiased=True)
ax[1].fill_between(bins2, model2+(model2-model2b), model2-(model2-model2b), alpha=0.2, edgecolor='purple', facecolor='red', linewidth=0, linestyle='dashdot', antialiased=True)
ax[1].set_xlabel('z',labelpad=-1)
ax[1].set_ylabel('Distance Bias (mag)',labelpad=-.5)
ax[1].legend(loc='lower left',fontsize=12)
ax[1].set_xlim(0,0.7)
ax[1].set_ylim(-0.15,0.1)
    
plt.show()
plt.savefig('searcheff.png')

#ax[0].errorbar(rmag,eff, yerr=efferr, fmt='ko', ecolor='black', color='black',label='D16 Malm')



#print np.mean(mudiff[z1 > 0.6])
#print bins, model
#import pdb; pdb.set_trace()
stop

name2='PS1_SINGLEu2_sys'
#print model
stop
#colors=['blue','blue','blue','red','red','red','black']
#markers=['o','D','s','o','D','s','o']
#files=['SALT2mu_fitoptgsu_ps1.M0DIF','SALT2mu_fitoptgsusys_ps1.M0DIF','SALT2mu_fitoptgfsu_ps1.M0DIF','SALT2mu_fitoptcsu_ps1.M0DIF','SALT2mu_fitoptcsusys_ps1.M0DIF','SALT2mu_fitoptcfsu_ps1.M0DIF','SALT#2mu_fitoptgosu_ps1.M0DIF']
#alphas=[0.4,0.4,0.4,0.4,0.4,0.4,1]
colors=['blue','blue','red','red','black']
markers=['o','D','o','D','s']
files=['SALT2mu_fitoptgsu_ps1.M0DIF','SALT2mu_fitoptgsusys_ps1.M0DIF','SALT2mu_fitoptcsu_ps1.M0DIF','SALT2mu_fitoptcsusys_ps1.M0DIF','SALT2mu_fitoptgosu_ps1.M0DIF']
alphas=[0.9,0.4,0.9,0.4,1]   
for num in range(0,5):
    headn=linef.linef(files[num],'VARN')
    z1,muerr1,mures1 = np.loadtxt('../DATA/SALT2mu/'+files[num], usecols=(4,6,5), unpack=True, dtype='string', skiprows=8)
    z1 = z1.astype(float)
    mures1=mures1.astype(float)
    muerr1=muerr1.astype(float)
    
    ax[1].errorbar(z1, mures1, yerr=muerr1, fmt='ko', ecolor=colors[num], color=colors[num],label='R14 Malm',marker=markers[num],alpha=alphas[num])
line, = ax[0].plot(lx,lx*0, lw=2)
line, = ax[1].plot(lx,lx*0, lw=2)
ax[1].set_xlim(0.04,.6)
ax[1].set_ylim(-.1,.15)

#plt.gca().add_artist(l1)


plt.xlabel('z',size=14)
ax[0].set_ylabel('Efficiency',size=24)
ax[1].set_ylabel(r'$\mu-\mu_{nom}$ (mag)',size=24)

#ax[0].text(0.05,0.3,"R14", color='red')
#ax[0].text(0.05,0.235,"S16",fontdict={'fontsize':20}, color='black')


plt.show()


plt.savefig('searcheff.png')

asdf
