import os
import string
import numpy as np
import matplotlib.pyplot as plt
import array
import math
from astropy import cosmology as cosmo
import wmom
from scipy.interpolate import interp1d
import matplotlib
import plotsetup
import linef
from matplotlib import gridspec

plotsetup.halfpaperfig()

labels=['LOWZ mag','Low-z volume','LOWZ mag pop small','LOWZ vol pop small']
#sing1=['../SIMS/LOWZ_GRIDu_single/DS_ABCD_smearG10_LOW_GRID_single','../SIMS/SDSS_GRIDu_single/DS_ABCD_smearG10_SDSS_GRID_single','../SIMS/SNLS_GRIDu_single/DS_ABCD_smearG10_SNLS_GRID_single','../SIMS/PS1_SINGLEu2/DS_smearG10_PS1_GRIDu_single']
#sing2=['../SIMS/LOWZ_GRIDu_single/DS_ABCD_smearC11_LOW_GRID_single','../SIMS/SDSS_GRIDu_single/DS_ABCD_smearC11_SDSS_GRID_single','../SIMS/SNLS_GRIDu_single/DS_ABCD_smearC11_SNLS_GRID_single','../SIMS/PS1_SINGLEu2/DS_smearC11_PS1_GRIDu_single']

# LOWZ_GRIDu_single/DS_ABCD_smearG10_LOW_GRID_single/FITOPT000.FITRES
#  LOWZ_GRIDu_single/DS_ABCD_smearG10_LOW_GRID_singsys/FITOPT000.FITRES

sing1=['../SIMS/LOWZ_GRIDu_single/DS_ABCD_smearG10_LOW_GRID_single','../SIMS/LOWZ_GRIDu_sysing/DS_ABCD_smearG10_LOW_GRID_singsys','../SIMS/LOWZ_GRIDu_sysing/DS_ABCD_smearG10_LOW_GRID_singpop','../SIMS/LOWZ_GRIDu_sysing/DS_ABCD_smearG10_LOW_GRID_singpop2']
#../SIMS/LOWZ_GRIDu_single/DS_SIMGEN_LOWZ_VOLLIM_C11
sing2=['../SIMS/LOWZ_GRIDu_single/DS_ABCD_smearC11_LOW_GRID_single','../SIMS/LOWZ_GRIDu_sysing/DS_ABCD_smearG10_LOW_GRID_singsys','../SIMS/LOWZ_GRIDu_sysing/DS_ABCD_smearC11_LOW_GRID_singpop','../SIMS/LOWZ_GRIDu_sysing/DS_ABCD_smearC11_LOW_GRID_singpop2']

#../SIMS/LOWZ_GRIDu_single/DS_SIMGEN_LOWZ_VOLLIM_C11/FITOPT000.FITRES

#fig, ax = plt.subplots(2,2)
fig, ax = plt.subplots(1) 
scat=['G10','C11']
colors=['black','red']
linestyles=['-', '--', '-.', ':','-']
zmax=[0.1,0.1,0.1,0.1]
plt.xlim(0,0.08)
#a = plt.axes([0.0, -.03, .08, .03])

for xl in range(0,2):
    singx=sing1
    for ii in range(0,2):
        betas=3.1
        #print '../SIMS//PS1_GRIDu_sys/DS_smear'+scat[xl]+'_PS1_GRIDs-0'+str(i)+'/FITOPT000.FITRES'
        if (xl>0):
            sing1=sing2
            betas=3.8
            singx=sing2
            #a = plt.axes([0.0, -.03, .08, .03])
            
        #simalpha,simbeta,z,simx11,simc1,simmb,mb,x11,c1,simdlmag,pke,fitprob,mbe,x11e,c1e = np.loadtxt(sing1[ii]+'/FITOPT000.FITRES', usecols=(42,43,6,40,41,45,23,19,21,38,18,32,24,20,22), unpack=True, dtype='string', skiprows=12)
        
        if (os.path.isfile(singx[ii]+'/FITOPT000.FITRES')==False): os.system('gunzip '+singx[ii]+'/FITOPT000.FITRES.gz')
        headn=linef.linef(singx[ii]+'/FITOPT000.FITRES','zCMB')
        data1=np.genfromtxt(singx[ii]+'/FITOPT000.FITRES',skip_header=headn,names=True,comments='#')
        cid=np.genfromtxt(singx[ii]+'/FITOPT000.FITRES',skip_header=headn,usecols=(1),comments='#',dtype='str')[1:]
        z = data1['zCMB'].astype(float)
        SNRMAX11=data1['SNRMAX1'].astype(float)
        x11 = data1['x1'].astype(float)
        c1 = data1['c'].astype(float)
        NDOF1=data1['NDOF'].astype(float)
        fitprob=data1['FITPROB'].astype(float)
        PKMJD1=data1['PKMJD'].astype(float)
        idsurvey=data1['IDSURVEY'].astype(float)
        NDOF1=data1['NDOF'].astype(float)
        c1e=data1['cERR'].astype(float)
        x11e=data1['x1ERR'].astype(float)
        mbe=data1['mBERR'].astype(float)
        mb=data1['mB'].astype(float)
        simx11 = data1['SIM_x1'].astype(float)
        simc1 = data1['SIM_c'].astype(float)
        simmb=data1['SIM_mB'].astype(float)
        pke=data1['PKMJDERR'].astype(float)
        simdlmag=data1['SIM_DLMAG'].astype(float)
        cdiff=-(3.1*c1-betas*simc1)
        x1diff=x11-simx11
        mbdiff=mb-simmb
        muerr=np.sqrt(mbe**2+(0.157**2)*(x11e**2)+(3.1**2)*(c1e**2)+.1**2)
        muerr=1.0/muerr**2
        xx=(muerr<1)
        mudiff=(mb+0.157*x11-3.1*c1)-(simmb+0.157*simx11-betas*simc1)
        
        alpha=[0,0.07,0.14,0.21,0.28]
        bins=[0,0.01,.015,0.022,.03,0.036,0.042,0.060,0.08]
        #bins=np.asarray(bins)-.005
        xx=((z<zmax[ii])&(np.abs(x11) < 3.) & (np.abs(c1) < 0.3) & (pke < 2.0*(1.0+z)) & (fitprob>0.01))
        print 'ii', ii, xl, np.median(mudiff[xx])

        for j in range(2,3):
            #print simalpha
            #print simbeta
            xx=((z<zmax[ii])&(np.abs(x11) < 3.) & (np.abs(c1) < 0.3) & (pke < 2.0*(1.0+z)) & (fitprob>0.01))
                                                                       # (fr.FITPROB > 0.001) & )
            #print 'lz',len(z[xx])
            
            #digitized = np.digitize(z[xx], bins)
            bin_means_z = [np.median(z[xx][(z[xx]>bins[i])&(z[xx]<bins[i+1])]) for i in range(0, len(bins)-1)]
            print bin_means_z
            #stop
            bin_means_x1 = [np.median(0.157*x1diff[xx][(z[xx]>bins[i])&(z[xx]<bins[i+1])]) for i in range(0, len(bins)-1)]
            bin_means_c = [np.median(cdiff[xx][(z[xx]>bins[i])&(z[xx]<bins[i+1])]) for i in range(0, len(bins)-1)]
            bin_means_mb = [np.median(mbdiff[xx][(z[xx]>bins[i])&(z[xx]<bins[i+1])]) for i in range(0, len(bins)-1)]
            bin_means_mu = [np.median(mudiff[xx][(z[xx]>bins[i])&(z[xx]<bins[i+1])]) for i in range(0, len(bins)-1)]
            #bin_len = [len(mudiff[xx]) for i in range(0, len(bins))]
            #bin_means_mu=[wmom.wmom(mudiff[xx][digitized==i], muerr[xx][digitized==i],calcerr=False)[0]  for i in range(0, len(bins))]
            #print len(bins), len(bin_means_x1)
            #wmom.wmom(mures[xx1[0]], 1.0/mu1e[xx1[0]], calcerr=True)
            #print bins
            #print bin_means_x1
            bin_means_x1=np.asarray(bin_means_x1)
            bin_means_c=np.asarray(bin_means_c)
            bin_means_mb=np.asarray(bin_means_mb)
            bin_means_mu=np.asarray(bin_means_mu)
            bin_means_z=np.asarray(bin_means_z)
            #print 'bin_len', bin_len
            zz=(np.isfinite(bin_means_mu)&(np.isnan(bin_means_mu)==False))
            
            #print zz
            #print bins[zz], bin_means_mu[zz]
            #print bins[zz]
            #print bin_means_mu[zz]
            #print colors[xl]
            #print linestyles[ii]
            #line, = ax[0,0].plot(bin_means_z[zz],bin_means_mu[zz], lw=2,color=colors[xl],linestyle=linestyles[ii])
            if ((xl==0)&(ii==0)):line1, = plt.plot(bin_means_z[zz],bin_means_mu[zz], lw=4,color=colors[xl],linestyle=linestyles[ii],label=scat[xl]+' '+labels[ii])
            if ((xl==0)&(ii==1)):line2, = plt.plot(bin_means_z[zz],bin_means_mu[zz], lw=4,color=colors[xl],linestyle=linestyles[ii],label=scat[xl]+' '+labels[ii])
            if ((xl==1)&(ii==0)):line3, = plt.plot(bin_means_z[zz],bin_means_mu[zz], lw=4,color=colors[xl],linestyle=linestyles[ii],label=scat[xl]+' '+labels[ii])
            if ((xl==1)&(ii==1)):line4, = plt.plot(bin_means_z[zz],bin_means_mu[zz], lw=4,color=colors[xl],linestyle=linestyles[ii],label=scat[xl]+' '+labels[ii])
                                    
            #line, = ax[0,0].plot(bin_means_z[zz],bin_means_mu[zz], lw=2,color=colors[xl],linestyle=linestyles[ii])
            
            #print bin_means_z[zz], bin_means_mu[zz]
            #line, = ax[1,0].plot(bin_means_z[zz],bin_means_x1[zz], lw=2,color=colors[xl],linestyle=linestyles[ii],label=scat[xl]+' '+labels[ii])
            #line, = ax[1,1].plot(bin_means_z[zz],bin_means_c[zz], lw=2,color=colors[xl],linestyle=linestyles[ii])
            #line, = ax[0,1].plot(bin_means_z[zz],bin_means_mb[zz], lw=2,color=colors[xl],linestyle=linestyles[ii])
                
            bin_num=[len(x1diff[xx][(z[xx]>bins[i])&(z[xx]<bins[i+1])]) for i in range(0, len(bins)-1)]
    
            print bin_num

        #plt.xlim(0,0.3)
        #plt.ylim(-.2,0.4)
        #plt.xlabel('alpha')
        #plt.ylabel('x1-simx1')
#legend = ax[1,0].legend(loc='lower left', shadow=True,fontsize=6.5
first_legend = plt.legend(handles=[line1,line2], loc=3,fontsize=12.0,)
axn = plt.gca().add_artist(first_legend)
plt.legend(handles=[line3,line4], loc=1,fontsize=12.0,)


#                legend = ax.legend(loc='lower left', shadow=True,fontsize=12.0,frameon=False)
#            if (xl>0): legend = ax.legend(loc='upper right', shadow=True,fontsize=12.0,frameon=False)
                        
line, = ax.plot([0,2],[0,0], lw=.5,color='blue')
plt.xlim(0,0.08)

ax.set_xlabel('z')
ax.set_ylabel('Distance Bias (mag)')
#ax[0,0].set_ylabel('mu bias')
#ax[1,1].set_ylabel('b*c diff')
#ax[0,1].set_ylabel('mb diff')
#ax[1,0].set_ylabel('a*x1 diff')



#ax[1,0].set_xlabel('z')
#ax[1,1].set_xlabel('z')
#ax[0,0].set_ylabel('mu bias')
#ax[1,1].set_ylabel('b*c diff')
#ax[0,1].set_ylabel('mb diff')
#ax[1,0].set_ylabel('a*x1 diff')

#ax[0,0].text(0.06,-0.07,"Luminosity Scatter Model",color='black',fontsize=5)
#ax[0,0].text(0.06,-0.1,"Color Scatter Model", color='red',fontsize=5)

plt.tight_layout()

plt.show()
plt.savefig('lowz_bias.png')
plt.cla()

