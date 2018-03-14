import numpy as np
import matplotlib.pyplot as plt
import array
import math
from astropy import cosmology as cosmo
import matplotlib
import matplotlib.ticker as ticker
import linef
import plotsetup
from matplotlib import gridspec

plotsetup.halfpaperfig()

named=['../DATA/SALT2mu/SALT2mu_fitoptn0.fitres','../DATA/SALT2mu/SALT2mu_fitoptg0.fitres']
#named=['../DATA/SALT2mu_fitopt.fitres','../DATA/SALT2mu_fitopt.fitres']
surv=[15,99,1,4,106,5,61,62,63,64,65,66]
survname=['PS1','Low-z','SDSS','SNLS']

names1=['../SIMS/PS1_SINGLEu2/DS_smearG10_PS1_GRIDu_single/FITOPT000.FITRES','../SIMS/LOWZ_GRIDu_single/DS_ABCD_smearG10_LOW_GRID_single/FITOPT000.FITRES','../SIMS/SDSS_GRIDu_single/DS_ABCD_smearG10_SDSS_GRID_single/FITOPT000.FITRES','../SIMS/SNLS_GRIDu_single/DS_ABCD_smearG10_SNLS_GRID_single/FITOPT000.FITRES','../SIMS/HST_GRIDu_single/DS_smearG10_HST_GRIDu_single/FITOPT000.FITRES']
names2=['../SIMS/PS1_SINGLEu2/DS_smearC11_PS1_GRIDu_single/FITOPT000.FITRES','../SIMS/LOWZ_GRIDu_single/DS_ABCD_smearC11_LOW_GRID_single/FITOPT000.FITRES','../SIMS/SDSS_GRIDu_single/DS_ABCD_smearC11_SDSS_GRID_single/FITOPT000.FITRES','../SIMS/SNLS_GRIDu_single/DS_ABCD_smearC11_SNLS_GRID_single/FITOPT000.FITRES','../SIMS/HST_GRIDu_single/DS_smearC11_HST_GRIDu_single/FITOPT000.FITRES']
#names1[1]='/project/rkessler/djones/NN_forDan/empiricalsim/biascor/SIMGEN_LOWZ/SIMGEN_LOWZ/SIMGEN_LOWZ_G10/FITOPT000.FITRES'
#/project/rkessler/djones/NN_forDan/empiricalsim/biascor/SIMGEN_LOWZ/SIMGEN_LOWZ/SIMGEN_LOWZ_G10/FITOPT000.FITRES
files=['ps1','lowz','sdss','snls','hst','csp','cfa1','cfa2','cfa3','cfa3k','cfa41','cfa42']
header1d=[1,1,1,1,1,1,1,1,1,1,1,1]
header1s=[5,6,5,5,6,6,6,6,6,6,6,6]
zm1=[0,0,0.05,0.1,0.8,0,0,0,0,0,0,0]
zm2=[0.69,0.065,0.49,0.99,2.29,0.09,0.09,0.09,0.09,0.09,0.09,0.09]
zt=[0.2,0.02,0.1,0.3,0.5,0.02,0.02,0.02,0.02,0.02,0.02,0.02]
for ii in range(0,2):
    print named[0]
    if (ii!=40):
        headn=linef.linef(named[0],'zCMB')
        print headn
        #stop
        data1=np.genfromtxt(named[0],skip_header=headn,names=True,comments='#')
        cid=np.genfromtxt(named[0],skip_header=headn,usecols=(1),comments='#',dtype='str')[1:]
    #if (ii==4):
    #    print 'ok'
    #    data1=np.genfromtxt('/project/rkessler/dscolnic/HST_analysis/CANDELS/CANDELs/FITOPT000.FITRES',skip_header=10,names=True,comments='#')
    #    cid=np.genfromtxt('/project/rkessler/dscolnic/HST_analysis/CANDELS/CANDELs/FITOPT000.FITRES',skip_header=10,usecols=(1),comments='#',dtype='str')[1:]
    #    print 'ok2'
        
    z1 = data1['zCMB'].astype(float)
    SNRMAX11=data1['SNRMAX1'].astype(float)
    x11 = data1['x1'].astype(float)
    c1 = data1['c'].astype(float)
    NDOF1=data1['NDOF'].astype(float)
    #TGAPMAX1=data1['TGAPMAX'].astype(float)
    FITPROB1=data1['FITPROB'].astype(float)
    PKMJD1=data1['PKMJD'].astype(float)
    #RA1=data1['RA'].astype(float)
    #DEC1=data1['DECL'].astype(float)
    idsurvey=data1['IDSURVEY'].astype(float)
    NDOF1=data1['NDOF'].astype(float)
    MB1E=data1['cERR'].astype(float)
    PKMJDE1=data1['PKMJDERR'].astype(float)
    x11err = data1['x1ERR'].astype(float)
    c1err = data1['cERR'].astype(float)
    
    iii=ii
    if (ii>4): iii=1
    headn=linef.linef(names1[iii],'zCMB')
    data1=np.genfromtxt(names1[iii],skip_header=headn,names=True,comments='#')
    cid2=np.genfromtxt(names1[iii],skip_header=headn,usecols=(1),comments='#',dtype='str')[1:]
    
    z2 = data1['zCMB'].astype(float)
    SNRMAX12=data1['SNRMAX1'].astype(float)
    x12 = data1['x1'].astype(float)
    c2 = data1['c'].astype(float)
    NDOF2=data1['NDOF'].astype(float)
    #TGAPMAX2=data1['TGAPMAX'].astype(float)
    FITPROB2=data1['FITPROB'].astype(float)
    PKMJD2=data1['PKMJD'].astype(float)
    #RA2=data1['RA'].astype(float)
    #DEC2=data1['DECL'].astype(float)
    idsurvey2=data1['IDSURVEY'].astype(float)
    NDOF2=data1['NDOF'].astype(float)
    MB2E=data1['cERR'].astype(float)
    PKMJDE2=data1['PKMJDERR'].astype(float)
    x12err = data1['x1ERR'].astype(float)
    c2err = data1['cERR'].astype(float)

    
    headn=linef.linef(names2[iii],'zCMB')    
    data1=np.genfromtxt(names2[iii],skip_header=headn,names=True,comments='#')
    cid3=np.genfromtxt(names2[iii],skip_header=headn,usecols=(1),comments='#',dtype='str')[1:]
    z3 = data1['zCMB'].astype(float)
    SNRMAX13=data1['SNRMAX1'].astype(float)
    x13 = data1['x1'].astype(float)
    x13err = data1['x1ERR'].astype(float)
    c3 = data1['c'].astype(float)
    c3err = data1['cERR'].astype(float)
    
    NDOF3=data1['NDOF'].astype(float)
    #TGAPMAX3=data1['TGAPMAX'].astype(float)
    FITPROB3=data1['FITPROB'].astype(float)
    PKMJD3=data1['PKMJD'].astype(float)
    #RA3=data1['RA'].astype(float)
    #DEC3=data1['DECL'].astype(float)
    idsurvey3=data1['IDSURVEY'].astype(float)
    NDOF3=data1['NDOF'].astype(float)
    MB3E=data1['cERR'].astype(float)
    PKMJDE3=data1['PKMJDERR'].astype(float)

    print np.unique(idsurvey)
    print np.unique(idsurvey2)
    print np.unique(idsurvey3)

    if (surv[ii]!=99): xx=((np.absolute(c1)<0.3)&(np.absolute(x11)<3)&(FITPROB1>0.001)&(idsurvey==surv[ii]))
    if (surv[ii]==99): xx=((np.absolute(c1)<0.3)&(np.absolute(x11)<3)&(FITPROB1>0.001)&(idsurvey!=15)&(idsurvey!=1)&(idsurvey!=4)&(z1<0.1))
    if (surv[ii]>100): xx=((np.absolute(c1)<0.3)&(np.absolute(x11)<3)&(FITPROB1>0.001)&(idsurvey!=15)&(idsurvey!=1)&(idsurvey!=4)&(z1>0.5))
        
    #if (ii=4): xx=(
    z1=z1[xx]
    SNRMAX11=SNRMAX11[xx]
    x11=x11[xx]
    c1=c1[xx]
    NDOF1=NDOF1[xx]
    #TGAPMAX1=TGAPMAX1[xx]
    #RA1=RA1[xx]
    PKMJDE1=PKMJDE1[xx]
    MB1E=MB1E[xx]
    c1err=c1err[xx]
    x11err=x11err[xx]
        
    PKMJD2 = PKMJD2.astype(float)
    PKMJDE2 = PKMJDE2.astype(float)
    
    z2 = z2.astype(float)
    SNRMAX12=SNRMAX12.astype(float)
    x12 = x12.astype(float)
    c2 = c2.astype(float)
    NDOF2=NDOF2.astype(float)
    FITPROB2=FITPROB2.astype(float)
    MB2E=MB2E.astype(float)
        
    if (surv[ii]!=99): xx=((np.absolute(c2)<0.3)&(np.absolute(x12)<3)&(FITPROB2>0.001)&(idsurvey2==surv[ii]))
    if (surv[ii]==99): xx=((np.absolute(c2)<0.3)&(np.absolute(x12)<3)&(FITPROB2>0.001)&(idsurvey2!=15)&(idsurvey2!=1)&(idsurvey2!=4)&(z2<0.1))
    if (surv[ii]>99): xx=((np.absolute(c2)<0.3)&(np.absolute(x12)<3)&(FITPROB2>0.001)&(idsurvey2!=15)&(idsurvey2!=1)&(idsurvey2!=4)&(z2>0.5))
        
    z2=z2[xx]
    SNRMAX12=SNRMAX12[xx]
    x12=x12[xx]
    c2=c2[xx]
    NDOF2=NDOF2[xx]
    FITPROB2=FITPROB2[xx]
    PKMJD2=PKMJD2[xx]
    PKMJDE2=PKMJDE2[xx]
    MB2E=MB2E[xx]
    c2err=c2err[xx]
    x12err=x12err[xx]
    
    z3 = z3.astype(float)
    SNRMAX13=SNRMAX13.astype(float)
    PKMJDE3 = PKMJDE3.astype(float)
    x13 = x13.astype(float)
    c3 = c3.astype(float)
    NDOF3=NDOF3.astype(float)
    FITPROB3=FITPROB3.astype(float)
    PKMJD3=PKMJD3.astype(float)
    
    MB3E=MB3E.astype(float)

    #xx=((np.absolute(c3)<0.3)&(np.absolute(x13)<3)&(FITPROB3>0.001)&(idsurvey3==surv[ii]))
    if (surv[ii]!=99): xx=((np.absolute(c3)<0.3)&(np.absolute(x13)<3)&(FITPROB3>0.001)&(idsurvey3==surv[ii]))
    if (surv[ii]==99): xx=((np.absolute(c3)<0.3)&(np.absolute(x13)<3)&(FITPROB3>0.001)&(idsurvey3!=15)&(idsurvey3!=1)&(idsurvey3!=4)&(z3<0.1))
    if (surv[ii]>99): xx=((np.absolute(c3)<0.3)&(np.absolute(x13)<3)&(FITPROB3>0.001)&(idsurvey3!=15)&(idsurvey3!=1)&(idsurvey3!=4)&(z3>0.4))
    
    z3=z3[xx]
    SNRMAX13=SNRMAX13[xx]
    x13=x13[xx]
    c3=c3[xx]
    NDOF3=NDOF3[xx]
    PKMJD3=PKMJD3[xx]
    PKMJDE3=PKMJDE3[xx]
    MB3E=MB3E[xx]
    c3err=c3err[xx]
    x13err=x13err[xx]
    
    if (surv[ii]==99):
        print len(idsurvey[idsurvey==5]), len(idsurvey[idsurvey==61]),len(idsurvey[idsurvey==62]),len(idsurvey[idsurvey==63]),len(idsurvey[idsurvey==64]),len(idsurvey[idsurvey==65]),len(idsurvey[idsurvey==66])
        print len(idsurvey2[idsurvey2==5]), len(idsurvey2[idsurvey2==61]),len(idsurvey2[idsurvey2==62]),len(idsurvey2[idsurvey2==63]),len(idsurvey2[idsurvey2==64]),len(idsurvey2[idsurvey2==65]),len(idsurvey2[idsurvey2==66])
        print len(idsurvey3[idsurvey3==5]), len(idsurvey3[idsurvey3==61]),len(idsurvey3[idsurvey3==62]),len(idsurvey3[idsurvey3==63]),len(idsurvey3[idsurvey3==64]),len(idsurvey3[idsurvey3==65]),len(idsurvey3[idsurvey3==66])
    print np.mean(c3), np.mean(c2), np.mean(c1), names1[ii]
    #stop   
    col=['b','g','r','c','m','y','r','g','m','b','g']

    pos=[]



    for i in range(1,299):
        pos.append(i/10.0-5)
    pos2=[]

    for i in range(1,299):
        pos2.append(0.0/100.0+.11)

    plt.figure(1)



    fig, ax = plt.subplots(4,2)
    gs1 = gridspec.GridSpec(1, 2)
    gs2 = gridspec.GridSpec(1, 2)
    gs3 = gridspec.GridSpec(1, 2)
    gs4 = gridspec.GridSpec(1, 2)
            
    gs1.update(bottom=0.83, top=0.97,wspace=0)
    ax1= plt.subplot(gs1[0])
    ax2= plt.subplot(gs1[1],sharey=ax1)

    gs2.update(bottom=0.59, top=0.73,wspace=0)
    ax3= plt.subplot(gs2[0])
    ax4= plt.subplot(gs2[1],sharey=ax3)

    gs3.update(bottom=0.35, top=0.49,wspace=0)
    ax5= plt.subplot(gs3[0])
    ax6= plt.subplot(gs3[1],sharey=ax5)

    gs4.update(bottom=0.11, top=0.25,wspace=0.38)
    ax7= plt.subplot(gs4[0])
    ax8= plt.subplot(gs4[1])
    print z1
    print zm1[ii],zm2[ii]
    n, bins, patches = ax1.hist(z1, bins=10,range=[zm1[ii],zm2[ii]], color='white', alpha=0.25,linewidth=0)
    ax1.set_xlabel('z',labelpad=-2)
    ax1.set_ylabel(" \# ")
    ax1.errorbar((bins[:-1]+bins[1:])/2.0, n, yerr=np.sqrt(n), fmt='ko', ecolor='k',label='Data')
    ax1.set_xlim(zm1[ii],zm2[ii])
    weights=z2*0.0+float(len(z1))/float(len(z2))
    weights3=z3*0.0+float(len(z1))/float(len(z3))

    print 'weights', weights
    n2, bins2, patches2 = ax1.hist(z2, weights=weights,bins=10,range=[zm1[ii],zm2[ii]], histtype='step', alpha=0.85, color='r',linewidth=2,label='G10 Sim')
    n3, bins3, patches3 = ax1.hist(z3, weights=weights3,bins=10,range=[zm1[ii],zm2[ii]], histtype='step', alpha=0.85, color='g',linewidth=2,label='C11 Sim')
    print np.sum(n), np.sum(n2), np.sum(n3)
    print n
    print n2
    print n3
    #stop
    hrange=100
    #if ((files[ii]=='lowz')|(ii>4)):
    #    hrange=200
    #if ((files[ii]!='lowz')&(ii<4)):
    #    hrange=90
    n, bins, patches = ax2.hist(SNRMAX11, bins=13,range=[0,hrange], color='white', alpha=0.25,linewidth=0)
    ax2.errorbar((bins[:-1]+bins[1:])/2.0, n, yerr=np.sqrt(n), fmt='ko', ecolor='k')
    #ax2.set_ylabel(" \# ")
    ax2.set_xlabel('Peak SNR',labelpad=-2)
    n2, bins2, patches2 = ax2.hist(SNRMAX12, weights=weights, color='r',bins=13,range=[0,hrange], histtype='step', alpha=0.85,linewidth=2)
    n3, bins2, patches2 = ax2.hist(SNRMAX13, weights=weights3, color='green',bins=13,range=[0,hrange], histtype='step', alpha=0.85,linewidth=2)
    #ax2.set_yticklabels([])
    plt.setp(ax2.get_yticklabels(), visible=False)
    ax2.set_xlim(1,hrange)
    #ax2.set_ylim(0,np.amax(bins)*1.1)
    
    n, bins, patches = ax3.hist(PKMJDE1, bins=12,range=[0,3], color='white', alpha=0.25,linewidth=0)
    ax3.errorbar((bins[:-1]+bins[1:])/2.0, n, yerr=np.sqrt(n), fmt='ko', ecolor='k',label='Data')
    ax3.set_xlabel(r"$\sigma_{pkMJD}$",labelpad=-2)
    ax3.set_ylabel(" \# ")
    n2, bins2, patches2 = ax3.hist(PKMJDE2,weights=weights, bins=12,range=[0,3], histtype='step', alpha=0.85,color='r',linewidth=2,label='G10 Sim')
    n2, bins2, patches2 = ax3.hist(PKMJDE3,weights=weights3, bins=12,range=[0,3], histtype='step', alpha=0.85,color='g',linewidth=2,label='C11 Sim')

    ax3.legend(loc='upper right',prop={'size':8})
    ax3.set_ylim(1,np.amax(n)*1.1)
        

    
    n, bins, patches = ax4.hist(MB1E, bins=10,range=[0,0.1], color='white', alpha=0.25,linewidth=0)
    ax4.errorbar((bins[:-1]+bins[1:])/2.0, n, yerr=np.sqrt(n), fmt='ko', ecolor='k')

    ax4.set_xlabel(r"$\sigma_c$",labelpad=-2)
    #ax4.set_ylabel(" \# ")
    n2, bins2, patches2 = ax4.hist(MB2E,weights=weights,color='r', bins=10,range=[0,.10], histtype='step', alpha=0.85,linewidth=2)
    n2, bins2, patches2 = ax4.hist(MB3E,weights=weights3,color='g', bins=10,range=[0,.10], histtype='step', alpha=0.85,linewidth=2)
    ax4.set_ylim(0,np.amax(n2)*1.2)
    plt.setp(ax4.get_yticklabels(), visible=False)
    ax4.set_xlim(0.005,0.1)
    


    n, bins, patches = ax5.hist(c1, bins=15,range=[-.4,.4], facecolor='white', alpha=0.25,linewidth=0)
    ax5.errorbar((bins[:-1]+bins[1:])/2.0, n, yerr=np.sqrt(n), fmt='ko', ecolor='k')
    n2, bins2, patches2 = ax5.hist(c2,weights=weights,color='r', bins=15,range=[-.4,.4], histtype='step', alpha=0.85,linewidth=2)
    
    n3, bins3, patches3 = ax5.hist(c3,weights=weights3,color='g', bins=15,range=[-.4,.4], histtype='step', alpha=0.85,linewidth=2)
    
    print np.sum(n), np.sum(n2), np.sum(n3)
    print np.sum(n), np.sum(n2), np.sum(n3)
    print n
    print n2
    print n3
    #stop               
    ax5.set_xlabel('c',labelpad=-2)
    ax5.set_ylabel(" \# ")
    ax5.set_xlim(-.3,.3)
    print 'lenc', np.sum(n), len(c1)
    n, bins, patches = ax6.hist(x11, bins=15,range=[-4,4], color='white', alpha=0.25,linewidth=0)
    ax6.errorbar((bins[:-1]+bins[1:])/2.0, n, yerr=np.sqrt(n), fmt='ko', ecolor='k')
    
    #ax[2,1].xlabel='z'
    #ax[2,1].ylabel=" \# "
    n2, bins2, patches2 = ax6.hist(x12, weights=weights,color='r',bins=15,range=[-4,4], histtype='step', alpha=0.85,linewidth=2)
    n3, bins3, patches3 = ax6.hist(x13, weights=weights3,color='green',bins=15,range=[-4,4], histtype='step', alpha=0.85,linewidth=2)
    
    ax6.set_xlabel(r'$x_1$',labelpad=-2)
    #ax6.set_ylabel(" \# ")
    ax6.set_xlim(-3,3)
    plt.setp(ax6.get_yticklabels(), visible=False)
    print 'lenc', np.sum(n), len(x11)
    
    bins = np.linspace(zm1[ii], zm2[ii], 11)
    #l1=plt.legend([p1],['D15 Data'],loc='lower left',prop={'size':16})
    digitized = np.digitize(z2, bins)
    bin_means = [np.median(c2[digitized == i]) for i in range(0, len(bins))]
    bin_z = [np.median(z2[digitized == i]) for i in range(0, len(bins))]
    bin_std = [np.median(c2err[digitized == i])/np.sqrt(len(c2[digitized == i])) for i in range(0, len(bins))]
    #ax[3,0].errorbar(bin_z, bin_means, yerr=bin_std, fmt='ko', ecolor='g', color='g',label='D15 Sim')
    line, = ax7.plot(bin_z,bin_means, lw=4,color='red',alpha=.85)
    
    digitized = np.digitize(z3, bins)
    bin_means = [np.median(c3[digitized == i]) for i in range(0, len(bins))]
    bin_z = [np.median(z3[digitized == i]) for i in range(0, len(bins))]
    bin_std = [np.median(c3err[digitized == i])/np.sqrt(len(c3[digitized == i])) for i in range(0, len(bins))]
    #bin_std=[]
    #for i in range(0, len(bins)):
    #    if len(
    #    bin_std=n
    #ax[3,0].errorbar(bin_z, bin_means, yerr=bin_std, fmt='ko', ecolor='g', color='g',label='D15 Sim')                                                                                                      
    line, = ax7.plot(bin_z,bin_means, lw=4,color='green',alpha=.85, label='Sim')

    bins = np.linspace(zm1[ii], zm2[ii], 11)
    
    digitized = np.digitize(z1, bins)
    bin_means = [np.median(c1[digitized == i]) for i in range(0, len(bins))]
    bin_z = [np.median(z1[digitized == i]) for i in range(0, len(bins))]
    bin_std = [np.median(c1err[digitized == i])/np.sqrt(len(c1[digitized == i])) for i in range(0, len(bins))]
    ax7.errorbar(bin_z, bin_means, yerr=bin_std, fmt='ko', ecolor='black', color='black',label='Data')
    
    
    #ax1.legend(loc='upper right',prop={'size':8})
    ax7.set_ylabel('c',labelpad=0.2)
    ax7.set_xlabel('z',labelpad=-1)
    ax7.set_xlim(zm1[ii],zm2[ii])
    #ax[3,0].xaxis.set_ticks(np.arange(-.15, 0.05, 0.03))
    #ax[3,0].xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
    ax7.yaxis.set_major_locator(ticker.MultipleLocator(0.04))
    #l1=plt.legend([p1],['D15 Data'],loc='lower left',prop={'size':16})                                                                                     
    digitized = np.digitize(z2, bins)
    bin_means = [np.median(x12[digitized == i]) for i in range(0, len(bins))]
    bin_z = [np.median(z2[digitized == i]) for i in range(0, len(bins))]
    bin_std = [np.median(x12err[digitized == i])/np.sqrt(len(x12[digitized == i])) for i in range(0, len(bins))]
    #ax[3,1].errorbar(bin_z, bin_means, yerr=bin_std, fmt='ko', ecolor='g', color='g',label='D15 Sim')
    line, = ax8.plot(bin_z,bin_means, lw=4,color='red',alpha=.85)
    
    digitized = np.digitize(z3, bins)
    bin_means = [np.median(x13[digitized == i]) for i in range(0, len(bins))]
    bin_z = [np.median(z3[digitized == i]) for i in range(0, len(bins))]
    bin_std = [np.std(x13err[digitized == i])/np.sqrt(len(x13[digitized == i])) for i in range(0, len(bins))]
    #ax[3,1].errorbar(bin_z, bin_means, yerr=bin_std, fmt='ko', ecolor='g', color='g',label='D15 Sim')                                                                                         
    
    line, = ax8.plot(bin_z,bin_means, lw=4,color='green',alpha=.85)
    
    digitized = np.digitize(z1, bins)
    bin_means = [np.median(x11[digitized == i]) for i in range(0, len(bins))]
    bin_z = [np.median(z1[digitized == i]) for i in range(0, len(bins))]
    bin_std = [np.median(x11err[digitized == i])/np.sqrt(len(x11err[digitized == i])) for i in range(0, len(bins))]
    ax8.errorbar(bin_z, bin_means, yerr=bin_std, fmt='ko', ecolor='black', color='black',label='D15 Data')


    #ax[3,1].legend(loc='upper right',prop={'size':5})
    ax8.set_ylabel(r'$x_1$',labelpad=-1.5)
    ax8.set_xlabel('z',labelpad=-2)
    ax8.set_xlim(zm1[ii],zm2[ii])
    ax8.yaxis.set_major_locator(ticker.MultipleLocator(0.4))
    if (1<0):
        ax1.text(.7,50,"(a)",fontdict={'fontsize':12})
        ax2.text(70,60,"(b)",fontdict={'fontsize':12})
        ax3.text(3.5,90,"(c)",fontdict={'fontsize':12})
        ax4.text(.12,100,"(d)",fontdict={'fontsize':12})
        ax5.text(.3,90,"(e)",fontdict={'fontsize':12})
        ax6.text(3,70,"(f)",fontdict={'fontsize':12})
        ax7.text(.7,.05,"(g)",fontdict={'fontsize':12})
        ax8.text(.7,1.5,"(h)",fontdict={'fontsize':12})

    ax1.yaxis.set_major_locator(ticker.MultipleLocator(30))
    ax3.yaxis.set_major_locator(ticker.MultipleLocator(30))
    ax5.yaxis.set_major_locator(ticker.MultipleLocator(30))
    ax7.yaxis.set_major_locator(ticker.MultipleLocator(0.04))
        
    ax8.yaxis.set_major_locator(ticker.MultipleLocator(0.6))
    
    #ax1.yaxis.set_major_locator(ticker.MultipleLocator(30))
    ax1.xaxis.set_major_locator(ticker.MultipleLocator(zt[ii]))
    
    ax2.xaxis.set_major_locator(ticker.MultipleLocator(30))    
    ax3.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax4.xaxis.set_major_locator(ticker.MultipleLocator(.04))
    ax5.xaxis.set_major_locator(ticker.MultipleLocator(0.2))
    ax6.xaxis.set_major_locator(ticker.MultipleLocator(2))
    ax7.xaxis.set_major_locator(ticker.MultipleLocator(zt[ii]))
    ax8.xaxis.set_major_locator(ticker.MultipleLocator(zt[ii]))
                         
    
    #plt.tight_layout()
    plt.show()


    plt.savefig('snana_hist_'+files[ii]+'.png')
    plt.cla()
stop
plt.figure(1)
bins = np.linspace(18,24,12)
digitized = np.digitize(mb3, bins)
bin_means = [np.median(SNRMAX13[digitized == i]) for i in range(0, len(bins))]
bin_z = [np.median(mb3[digitized == i]) for i in range(0, len(bins))]
bin_std = [np.std(SNRMAX13[digitized == i])/np.sqrt(len(SNRMAX13[digitized == i])) for i in range(0, len(bins))]
#ax[3,1].errorbar(bin_z, bin_means, yerr=bin_std, fmt='ko', ecolor='g', color='g',label='D15 Sim')                                                                               

line, = plt.plot(bin_z,bin_means, lw=4,color='green',alpha=.85)

print mb1
print SNRMAX11

digitized = np.digitize(mb1, bins)
bin_means = [np.median(SNRMAX11[digitized == i]) for i in range(0, len(bins))]
bin_z = [np.median(mb1[digitized == i]) for i in range(0, len(bins))]
bin_std = [np.std(SNRMAX11[digitized == i])/np.sqrt(len(SNRMAX11[digitized == i])) for i in range(0, len(bins))]
plt.errorbar(bin_z, bin_means, yerr=bin_std, fmt='ko', ecolor='b', color='b',label='D15 Data',alpha=.5)
print bin_z
print bin_means

plt.xlim(16,24)
plt.ylim(0,200)
plt.xlabel('mb')
plt.ylabel('SNRMAX1')
plt.tight_layout()
plt.show()


plt.savefig('snana_hist_check.png')

asdf
