import os
import string
import numpy as np
import matplotlib.pyplot as plt
import array
import math
from astropy import cosmology as cosmo
import wmom
from scipy.interpolate import interp1d
import matplotlib.patches as patches
import matplotlib
import plotsetup
import linef
from matplotlib import gridspec

plotsetup.fullpaperfig()
#../SIMS/LOWZ_GRIDu_single/DS_ABCD_smearG10_LOW_GRID_single2
labels=['LOWZ','SDSS','SNLS','PS1','HST']
sing1=['../SIMS/LOWZ_GRIDu_single/DS_ABCD_smearG10_LOW_GRID_single','../SIMS/SDSS_GRIDu_single/DS_ABCD_smearG10_SDSS_GRID_single','../SIMS/PS1_SINGLEu2/DS_smearG10_PS1_GRIDu_single','../SIMS/SNLS_GRIDu_single/DS_ABCD_smearG10_SNLS_GRID_single','../SIMS/HST_GRIDu_single/DS_smearG10_HST_GRIDu_single']
sing2=['../SIMS/LOWZ_GRIDu_single/DS_ABCD_smearC11_LOW_GRID_single','../SIMS/SDSS_GRIDu_single/DS_ABCD_smearC11_SDSS_GRID_single','../SIMS/PS1_SINGLEu2/DS_smearC11_PS1_GRIDu_single','../SIMS/SNLS_GRIDu_single/DS_ABCD_smearC11_SNLS_GRID_single','../SIMS/HST_GRIDu_single/DS_smearC11_HST_GRIDu_single']
fig, ax = plt.subplots(2,2)
titles=['LOWZ','SDSS','PS1','SNLS','HST']
scat=['G10','C11']
colors=['black','red']
linestyles=['-', '--', '-.', ':','-']
colors=['blue','red','purple','green','orange']
zmin=[0,0.05,0.05,0.2,0.8]
zmax=[0.1,0.45,0.650,1.0,2.3]
heads=[6,5,5,5,6]
#ax1 = plt.subplot2grid((3,2), (0,0), rowspan=3)
#ax4 = plt.subplot2grid((3,2), (2,1),hspace=0)
#ax2 = plt.subplot2grid((3,2), (0,1),sharex=ax4,hspace=0)
#ax3 = plt.subplot2grid((3,2), (1,1),sharex=ax4,hspace=0)

#plt.figure(figsize = (3,3))
#gs1 = gridspec.GridSpec(3, 1)
#gs1.update(left=0.1, right=0.25, wspace=0.05)
#ax1= plt.subplot(gs1[0])
#ax2= plt.subplot(gs1[1])
#ax3= plt.subplot(gs1[2])

#gs2 = gridspec.GridSpec(3, 1)
#gs2.update(left=0.28, right=0.43, wspace=0.05)
#ax1= plt.subplot(gs1[0])
#ax2= plt.subplot(gs1[1])
#ax3= plt.subplot(gs1[2])

#gs3 = gridspec.GridSpec(3, 1)
#gs3.update(left=0.46, right=0.61, wspace=0.05)
#ax1= plt.subplot(gs1[0])
#ax2= plt.subplot(gs1[1])
#ax3= plt.subplot(gs1[2])

#gs4 = gridspec.GridSpec(3, 1)
#gs4.update(left=0.64, right=0.79, wspace=0.05)
#ax1= plt.subplot(gs1[0])
#ax2= plt.subplot(gs1[1])
#ax3= plt.subplot(gs1[2])

#gs5 = gridspec.GridSpec(3, 1)
#gs5.update(left=0.82, right=0.97, wspace=0.05)
#ax1= plt.subplot(gs1[0])
#ax2= plt.subplot(gs1[1])
#ax3= plt.subplot(gs1[2])



leftv=[0.1,0.28,0.46,0.64,0.82]
rightv=[0.25,0.43,0.61,0.79,0.97]
for ii in range(0,5):
    gs1 = gridspec.GridSpec(3, 1)
    gs1.update(left=leftv[ii], right=rightv[ii], hspace=0.0,bottom=0.13,top=0.92)
    ax3= plt.subplot(gs1[2])    
    ax2= plt.subplot(gs1[1])
    ax1= plt.subplot(gs1[0])
    for xl in range(0,2):
    
        betas=3.1
        #print '../SIMS//PS1_GRIDu_sys/DS_smear'+scat[xl]+'_PS1_GRIDs-0'+str(i)+'/FITOPT000.FITRES'
        if (xl>0):
            betas=3.8
        if (xl==0): singx=sing1
        if (xl==1): singx=sing2
        
        if (os.path.isfile(singx[ii]+'/FITOPT000.FITRES')==False): os.system('gunzip '+singx[ii]+'/FITOPT000.FITRES.gz')     
        #simalpha,simbeta,z,simx11,simc1,simmb,mb,x11,c1,simdlmag,pke,fitprob,mbe,x11e,c1e = np.loadtxt(sing1[ii]+'/FITOPT000.FITRES', usecols=(42,43,6,40,41,45,23,19,21,38,18,32,24,20,22), unpack=True, dtype='string', skiprows=12)


        #VARNAMES:  CID IDSURVEY TYPE FIELD CUTFLAG_SNANA zCMB zCMBERR zHD zHDERR VPEC VPEC_ERR HOST_LOGMASS HOST_LOGMASS_ERR SNRMAX1 SNRMAX2 SNRMAX3 PKMJD PKMJDERR x1 x1ERR c cERR mB mBER\R x0 x0ERR COV_x1_c COV_x1_x0 COV_c_x0 NDOF FITCHI2 FITPROB SIM_TYPE_INDEX SIM_NONIA_INDEX SIM_LIBID SIM_NGEN_LIBID SIM_ZCMB SIM_DLMAG SIM_PKMJD SIM_x1 SIM_c SIM_alpha SIM_beta SIM
        print singx[ii]+'/FITOPT000.FITRES'
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
        muerr=np.sqrt(mbe**2+(0.14**2)*(x11e**2)+(3.1**2)*(c1e**2)+.1**2)
        muerr=1.0/muerr**2
        xx=(muerr<1)
        #stop
        mudiff=(mb+0.14*x11-3.1*c1)-(simmb+0.14*simx11-betas*simc1)
        #print c1, simc1
        xx=(z>0.2)
        #print np.median(cdiff[xx])
        xx=(z<0.4)
        #print np.median(cdiff[xx])

        alpha=[0,0.07,0.14,0.21,0.28]
        bins=[0.01,0.02,0.04,0.08,0.16,0.25,0.36,0.48,0.62,0.85,1.1,1.4,1.8,2.3]
        bins=np.asarray(bins)
        xx=((z<zmax[ii])&(np.abs(x11) < 3.) & (np.abs(c1) < 0.3) & (pke < 2.0*(1.0+z)) & (fitprob>0.01))
        print 'ii', ii, xl, np.median(mudiff[xx])

        for j in range(2,3):
            #print simalpha
            #print simbeta
            xx=((z<zmax[ii])&(np.abs(x11) < 3.) & (np.abs(c1) < 0.3) & (pke < 2.0*(1.0+z)) & (fitprob>0.01))
                                                                       # (fr.FITPROB > 0.001) & )
            print 'lz',len(z[xx])
            print z[xx]
            print mudiff[xx]
            digitized = np.digitize(z[xx], bins)
            bin_means_z = [np.median(z[xx][digitized==i]) for i in range(0, len(bins))]
            
            bin_means_x1 = [np.median(0.14*x1diff[xx][digitized==i]) for i in range(0, len(bins))]
            bin_means_c = [np.median(cdiff[xx][digitized==i]) for i in range(0, len(bins))]
            bin_means_mb = [np.median(mbdiff[xx][digitized==i]) for i in range(0, len(bins))]
            bin_means_mu = [np.median(mudiff[xx][digitized==i]) for i in range(0, len(bins))]
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
            
            zz=(np.isfinite(bin_means_mu)&(np.isnan(bin_means_mu)==False))
            
            #print zz
            #print bins[zz], bin_means_mu[zz]
            #print bins[zz]
            #print bin_means_mu[zz]
            #print colors[xl]
            #print linestyles[ii]
            line, = ax1.plot(bin_means_z[zz],bin_means_mu[zz], lw=2,color=colors[ii],linestyle=linestyles[xl])
            #if (xl==0): line, = ax1.plot(bin_means_z[zz],bin_means_mu[zz], lw=2,color=colors[ii],linestyle=linestyles[xl],label=labels[ii])
            print bin_means_z[zz], bin_means_mu[zz]
            #line, = ax4.plot(bin_means_z[zz],bin_means_x1[zz], lw=2,color=colors[ii],linestyle=linestyles[xl])
            line, = ax2.plot(bin_means_z[zz],bin_means_mb[zz], lw=2,color=colors[ii],linestyle=linestyles[xl])
            line, = ax3.plot(bin_means_z[zz],bin_means_c[zz], lw=2,color=colors[ii],linestyle=linestyles[xl])
            if (xl>-1):
                print bin_means_z[zz],bin_means_mb[zz]
                print 'line', colors[ii], linestyles[xl]
            #ax1.axes.get_xaxis().set_visible(False)
            #ax2.axes.get_xaxis().set_visible(False)    
            bin_num=[len(x1diff[xx][digitized==i]) for i in range(0, len(alpha))]
            if (xl==0): ax1.set_title(titles[ii])
            ax1.set_ylim(-0.06,0.06)
            ax2.set_ylim(-0.06,0.06)
            ax3.set_ylim(-0.06,0.06)
            ax1.set_xlim(zmin[ii],zmax[ii])
            ax2.set_xlim(zmin[ii],zmax[ii])
                        
            ax3.set_xlim(zmin[ii],zmax[ii])
            ax3.set_xlabel('z')
            
            line, = ax1.plot([0,4],[0,0], lw=1,color='black',alpha=0.5)
            line, = ax2.plot([0,4],[0,0], lw=1,color='black',alpha=0.5)
            line, = ax3.plot([0,4],[0,0], lw=1,color='black',alpha=0.5)
            if (ii==0):
                ax1.set_ylabel('Sim. Distance \n Bias (mag)',fontsize=10)
                ax2.set_ylabel('Bias from \n '+r'$m_b$ ',fontsize=10)
                ax3.set_ylabel('Bias from \n '+r'$c$ ',fontsize=10)
                
            if (ii==0):
                ax1.set_xticks([0.02,0.06,0.1])
                ax2.set_xticks([0.02,0.06,0.1])
                ax3.set_xticks([0.02,0.06,0.1])  
                ax3.set_xticklabels(['0.02','0.06','0.10'])
                ax1.set_xticklabels(['','',''])
                ax2.set_xticklabels(['','',''])
                     
            if (ii==1):
                ax1.set_xticks([0.1,0.25,0.4])
                ax2.set_xticks([0.1,0.25,0.4])
                ax3.set_xticks([0.1,0.25,0.4])
                ax3.set_xticklabels(['0.1','0.25','0.4'])
                ax1.set_xticklabels(['','',''])
                ax2.set_xticklabels(['','',''])
            if (ii==2):
                ax1.set_xticks([0.1,0.3,0.5,0.7])
                ax2.set_xticks([0.1,0.3,0.5,0.7])
                ax3.set_xticks([0.1,0.3,0.5,0.7])
                ax1.set_xticklabels(['','','',''])
                ax2.set_xticklabels(['','','',''])
                ax3.set_xticklabels(['0.1','0.3','0.5','0.7'])
            if (ii==3):
                ax1.set_xticks([0.3,0.6,0.9])
                ax2.set_xticks([0.3,0.6,0.9])
                ax3.set_xticks([0.3,0.6,0.9])
                ax1.set_xticklabels(['','',''])
                ax2.set_xticklabels(['','',''])
                ax3.set_xticklabels(['0.3','0.6','0.9'])
            if (ii==4):
                ax1.set_xticks([1.0,1.5,2.0])
                ax2.set_xticks([1.0,1.5,2.0])
                ax3.set_xticks([1.0,1.5,2.0])
                ax1.set_xticklabels(['','',''])
                ax2.set_xticklabels(['','',''])
                ax3.set_xticklabels(['1.0','1.5','2.0'])
            if (ii==0):
                ax1.set_yticks([-0.06,-0.04,-0.02,0,0.02,0.04,0.06])
                ax1.set_yticklabels(['','-0.04','','0.0','','0.04',''])
                ax2.set_yticks([-0.06,-0.04,-0.02,0,0.02,0.04,0.06])
                ax2.set_yticklabels(['','-0.04','','0.0','','0.04',''])
                ax3.set_yticks([-0.06,-0.04,-0.02,0,0.02,0.04,0.06])
                ax3.set_yticklabels(['','-0.04','','0.0','','0.04',''])
            if (ii>0):
                ax1.set_yticks([-0.06,-0.04,-0.02,0,0.02,0.04,0.06])
                ax1.set_yticklabels(['','','','','','',''])
                ax2.set_yticks([-0.06,-0.04,-0.02,0,0.02,0.04,0.06])
                ax2.set_yticklabels(['','','','','','',''])
                ax3.set_yticks([-0.06,-0.04,-0.02,0,0.02,0.04,0.06])
                ax3.set_yticklabels(['','','','','','',''])
            if (ii==0):
                ax1.text(0.024,0.016,"C11 ",color='blue',rotation=-30)
                ax1.text(0.016,-0.042," G10 ", color='blue',rotation=-20)
                #ax3.set_xscale('log')
                
                

        #plt.xlim(0,0.3)
        #plt.ylim(-.2,0.4)
        #plt.xlabel('alpha')
        #plt.ylabel('x1-simx1')
#legend = ax[0,0].legend(loc='upper right', shadow=True,frameon = False)
#for text in legend.get_texts():
#            text.set_color("blue")
# example additional legends
#l1 = plt.legend(handles=[rec1], loc='lower right',
#                bbox_to_anchor=(1.0, 0.5))

#plt.tight_layout()

plt.show()
plt.savefig('oned_bias.png')
plt.cla()
stop

ax1.set_xlabel('z')
ax4.set_xlabel('z')



#ax2.set_ylabel(r'$-\beta_{R} c_{R} + \beta_{T} c_{T}$',fontsize=10)
#ax3.set_ylabel(r'$m_{B_R}-m_{B_T}$',fontsize=10)
#ax4.set_ylabel(r'$\alpha_{R} x1_{R} - \alpha_{T} x1_{T}$',fontsize=10)

#ax[0,0].text(0.67,-0.065,"G10 Scatter",color='black',fontsize=10,bbox=dict(facecolor='none', edgecolor='black'))
#ax[0,0].text(0.67,-0.052,"C11 Scatter", color='red',fontsize=10,bbox=dict(facecolor='none', edgecolor='black'))

ax1.text(0.02,0.055,"- G10 Scatter",color='black')
ax1.text(0.02,0.042," - - C11 Scatter", color='black')

ax1.text(0.03,-0.05,"Low-z",color='blue')
ax1.text(0.13,0.02,"SDSS",color='red')
ax1.text(0.16,-0.04,"PS1",color='green')
ax1.text(0.86,-0.015,"SNLS",color='purple')
ax1.text(1.0,0.01,"HST",color='orange')

#colors=['blue','red','purple','green']


ax1.set_xlim(0.01,2)
ax1.set_xscale('log')
ax2.set_xlim(0.01,2)
ax2.set_xscale('log')
ax3.set_xlim(0.01,2)
ax3.set_xscale('log')
ax4.set_xlim(0.01,2)
ax4.set_xscale('log')

ax1.set_ylim(-0.075,0.075)
ax2.set_ylim(-0.075,0.075)
ax3.set_ylim(-0.075,0.075)
ax4.set_ylim(-0.075,0.075)

line, = ax1.plot([0,2],[0,0], lw=1,color='blue',alpha=0.5)
line, = ax2.plot([0,2],[0,0], lw=1,color='blue',alpha=0.5)
line, = ax3.plot([0,2],[0,0], lw=1,color='blue',alpha=0.5)
line, = ax4.plot([0,2],[0,0], lw=1,color='blue',alpha=0.5)

ax1.set_xticks([0.01,0.1,1.0])
ax1.set_xticklabels(['0.01','0.10','1.0'])
ax4.set_xticks([0.01,0.1,1.0])
ax4.set_xticklabels(['0.01','0.10','1.0'])


#ax2.yticks([-.05,0,.05],['-0.05','0.0','0.05'])
#ax3.yticks([-.05,0,.05],['-0.05','0.0','0.05'])
#ax4.yticks([-.05,0,.05],['-0.05','0.0','0.05'])

#plt.tight_layout()

plt.show()
plt.savefig('oned_bias.png')
plt.cla()

