import djs_angle_match
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import plotsetup
from matplotlib import gridspec

plotsetup.fullpaperfig()
co=0
xlabel=['g mag','MJD/100','Airmass','Ang. Dist. (Deg)']
fil2=['g','r','i','z']
fields=['053','054','055','057','058','059']
fields=['0','053','054','056','057','058','059']
fbin=[0,0.1,0.2,0.3,0.5,0.7,1.0,1.3,2.0]
        
if (1>0):

    co=0
    l1=0
    jj=0
    gs1 = gridspec.GridSpec(1, 4)
    gs1.update(bottom=0.17, top=0.95, wspace=0.0)
    ax1= plt.subplot(gs1[0])
    ax2= plt.subplot(gs1[1])
    ax3= plt.subplot(gs1[2])
    ax4= plt.subplot(gs1[3])
    ax=[ax1,ax2,ax3,ax4]    
    for k1 in range(0,2):
        for k2 in range(0,2):
        
            if (co==0):fil,mag,color,off1,off1e,num = np.loadtxt('/project/rkessler/dscolnic/DougComp/ps1star/ncomp_'+fil2[l1]+'_'+fields[jj]+'_1_mag.txt', usecols=(0,1,2,3,4,5), unpack=True, dtype='string')
            print 'ps1star/comp_'+fil2[l1]+'_'+fields[jj]+'_1_mag.txt'

            if (co==1):fil,mag,color,off1,off1e,num = np.loadtxt('/project/rkessler/dscolnic/PS1_analysis/ps1star/comp_'+fil2[l1]+'_'+fields[jj]+'_1_mjd.txt', usecols=(0,1,2,3,4,5), unpack=True, dtype='string')
            if (co==2):fil,mag,color,off1,off1e,num = np.loadtxt('/project/rkessler/dscolnic/PS1_analysis/ps1star/comp_'+fil2[l1]+'_'+fields[jj]+'_1_air.txt', usecols=(0,1,2,3,4,5), unpack=True, dtype='string')
            if (co==3):fil,mag,color,off1,off1e,num = np.loadtxt('/project/rkessler/dscolnic/PS1_analysis/ps1star/comp_'+fil2[l1]+'_'+fields[jj]+'_1_foc.txt', usecols=(0,1,2,3,4,5), unpack=True, dtype='string')
            mag=mag.astype(float)            
            if (co==3):
             for mm in range(0,len(mag)):
              mag[mm]=fbin[mag[mm].astype(int)]
            if (co==1):
             mag=mag/100.0
             mag=mag.astype(int)
             print mag
             
            num=num.astype(float)
            mag=mag.astype(float)
            color=color.astype(float)
            off1=off1.astype(float)
            off1e=off1e.astype(float)
            num=num.astype(float)
            colnames=['red','blue','green','black']
            labels2=[r"$0.0<g-i<0.5$",r"$0.5<g-i<1.0$",r"$1.0<g-i<1.5$",r"$1.5<g-i<2.0$"]
            labels2=[r"$-1.0<g-i<0.6$",r"$0.6<g-i<1.3$",r"$1.3<g-i<1.8$",r"$1.8<g-i<3.0$"]
                        
            marker=['o','s','D','o']
            colv=[-1,0.6,1.3,1.8]
            #colv=[0,0.5,1,1.5]
            for i in range(0,4):
                line, = ax[co].plot(np.arange(-10,800000,200000), np.arange(-10,800000,200000)*0.0, linestyle='-',lw=0.5,color='gray',alpha=0.5) 
                if (i==0): xx=((color==colv[i])&(num>1000)&(np.isfinite(off1)))
                if (i>0):xx=((color==colv[i])&(num>100)&(np.isfinite(off1)))
                #if (i==0): xx=((color==colv[i])&(num>1000)&(np.isfinite(off1)))
                
                print 'xx', xx
                if (len(off1[xx])>1):
                    #line, = ax[k1,k2].plot(mag[xx], off1[xx], linestyle='--',lw=2,color=colnames[i])
                    
                    if (co==0): ax[co].errorbar(mag[xx]+.4, off1[xx], yerr=off1e[xx], color=colnames[i],ecolor=colnames[i],fmt=marker[i],label=labels2[i])
                    if (co>0): ax[co].errorbar(mag[xx]+0, off1[xx], yerr=off1e[xx], color=colnames[i],ecolor=colnames[i],fmt=marker[i],label=labels2[i])
                                        
                    print mag[xx], off1[xx]


                        
            ax[co].set_xlabel(xlabel[co])
            if (co==0): ax[co].set_ylabel('g S17-Ubercal (mmag)')
            ax[co].set_ylim((-0.005,0.005))
            if (co==0):
             ax[0].set_xlim((17.2,21.2))
             ax[co].set_xticklabels(['','17.5','','18.5','','19.5','','20.5',''])
             #ax[0].text(17,0.026,marker[0]+" -1.0<g-i<0.6",fontdict={'fontsize':12},color=colnames[0])
             #ax[0,0].text(17,0.022,marker[1]+"0.6<g-i<1.3",fontdict={'fontsize':12},color=colnames[1])
             #ax[0,0].text(17,0.018,marker[2]+"1.3<g-i<1.8",fontdict={'fontsize':12},color=colnames[2])
             #ax[0,0].text(17,0.014,marker[3]+"1.8<g-i",fontdict={'fontsize':12},color=colnames[3])
             ax[0].legend(loc='upper left',fontsize=8)             
                         
                           
            if (co==1):
                ax[co].set_xlim((552,569))
                ax[co].set_xticklabels(['','554','','558','','562','','566'])
            if (co==2):
                ax[co].set_xlim((0.95,1.7))
                ax[co].set_xticklabels(['1.0','','1.2','','1.4','','1.6',''])
            if (co==3):ax[co].set_xlim((-.1,1.7))
            if (co==3):
             ax[co].arrow(0.1, 0.0025, 0.0, 0.0015, head_width=0.05, head_length=0.0015, fc='k', ec='k')
             ax[co].arrow(0.2, 0.0025, 0.0, 0.0015, head_width=0.05, head_length=0.0015, fc='k', ec='k')
             ax[co].text(0.27,0.0025,"R14")                                                                                                      
              
            #stop
            co=co+1
    ax1.set_yticklabels(['','-4','-2','0','2','4',''])
        
    ax2.set_yticklabels(['','','','','','',''])
    ax3.set_yticklabels(['','','','','','',''])
    ax4.set_yticklabels(['','','','','','',''])
            
    #plt.show()
    print 'ps1star_'+fil2[l1]+'_'+fields[jj]+'_mag.png'
    #plt.savefig('ps1star_'+fil2[l1]+'_'+fields[jj]+'_mag.png')
    #ax[0,0].set_title('ps1star_'+fil2[l1]+'_'+fields[jj])
    #plt.tight_layout()
    line, = ax[0].plot(np.arange(16,23,1), (np.arange(16,23,1)-19.0)*.0006-.0002, linestyle='--',lw=0.5,color='purple')
                    
    plt.subplots_adjust(wspace=0,hspace=0.1)
    #plt.tight_layout(w_pad=0.0, h_pad=0.2,pad=0)
    
    plt.show()
    plt.savefig('ps1star_plot.png') 
    #pdf.savefig()  # saves the current figure into a pdf page
    plt.close()
                                           
