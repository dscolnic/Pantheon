import numpy as np
import matplotlib.pyplot as plt
import array
import math
from astropy import cosmology as cosmo
import wmom
import matplotlib
import plotsetup
from matplotlib import gridspec
import matplotlib.ticker as ticker
import linef
plotsetup.halfpaperfig()

#list1, idsurvey,z1, mass1,x11,c1,mu1, mu1e = np.loadtxt('wc0a.fitres', usecols=(0,3, 6,10,17,19,34,35), unpack=True, dtype='string', skiprows=12)
#VARNAMES: CID CIDint IDSURVEY TYPE FIELD CUTFLAG_SNANA zCMB zCMBERR zHD zHDERR VPEC VPEC_ERR HOST_LOGMASS HOST_LOGMASS_ERR SNRMAX1 SNRMAX2 SNRMAX3 PKMJD PKMJDERR x1 x1ERR c cERR mB mBERR x0 x0ERR \
#    COV_x1_c COV_x1_x0 COV_c_x0 NDOF FITCHI2 FITPROB RA DECL TGAPMAX MU MUMODEL MUERR MUERR_RAW MURES MUPULL ERRCODE biasCor_mu biasCorErr_mu biasCor_mB biasCor_x1 biasCor_c biasScale_muCOV IDSAM#PLE



name1='../DATA/SALT2mu/SALT2mu_fitoptg0.fitres'
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
idsurvey=data1['IDSURVEY'].astype(float)
NDOF1=data1['NDOF'].astype(float)
PKMJDE1=data1['PKMJDERR'].astype(float)
mb1e=data1['mBERR'].astype(float)
c1e=data1['cERR'].astype(float)
x11e=data1['x1ERR'].astype(float)
mures1=data1['MURES'].astype(float)
mu1=data1['MU'].astype(float)
mu1e=data1['MUERR'].astype(float)
mures=data1['MURES'].astype(float)
mass=data1['HOST_LOGMASS'].astype(float)
xx=np.where(idsurvey==15)

fsave=open('ps1_mass.txt','w')
list1=cid1[xx[0]]
z1=z1[xx[0]]
x11=x11[xx[0]]
c1=c1[xx[0]]
mb1=mb1[xx[0]]
mu1=mu1[xx[0]]
mu1e=mu1e[xx[0]]
mures=mures[xx[0]]
mass=mass[xx[0]]
x11e=x11e[xx[0]]
c1e=c1e[xx[0]]
print 'z',z1
print 'x11',x11
print 'c1', c1
xx1=np.where(mass.astype(float)>10)
xx2=np.where((mass.astype(float)<10) & (mass.astype(float)>0))
xx3=np.where(mass.astype(float)<0)
print list1[xx3[0]]
print len(xx1[0]), len(xx2[0]), len(xx1[0])+len(xx2[0]),len(mass)
fsave.write(str(len(xx1[0]))+' '+str(len(xx2[0]))+' '+str(len(xx1[0]))+' '+str(len(xx2[0]))+' '+str(len(mass))+'\n')
#stop
z1 = z1.astype(float)
x11 = x11.astype(float)
print x11[0]
print 'nothing yet'

xx=np.where(mass>1)
#list1=list1[xx[0]]
z2=z1[xx[0]]
x12=x11[xx[0]]
c2=c1[xx[0]]
mb2=mb1[xx[0]]
mu2=mu1[xx[0]]
muerr2=mu1e[xx[0]]
mures2=mures[xx[0]]
mass2=mass[xx[0]]

x12e=x11e[xx[0]]
c2e=c1e[xx[0]]

gamma1=0.053
gamma1e=0.009
xx=[mass<10]
mures2[xx]=mures[xx[0]]+gamma1
mures2=mures2-np.median(mures2)

print 'mass2', mass2
print 'mures2', mures2
#stop

print 'mass2 full', mass2
xx1=np.where(mass2 > 10)

print len(xx1[0])
print 'med high mass mu', np.median(mures2[xx1[0]])
xx2=np.where((mass2>3) & (mass2 < 10))
print len(xx2[0])
print 'med low mass mu', np.median(mures2[xx2[0]])
print 'Full Med', np.median(mures), np.median(mures2)
print 'mures', mures
mstep=np.median(mures2[xx1[0]])-np.median(mures2[xx2[0]])
wmean,werr = wmom.wmom(mures2[xx1[0]], 1.0/muerr2[xx1[0]], calcerr=True)
wmean2,werr2 = wmom.wmom(mures2[xx2[0]], 1.0/muerr2[xx2[0]], calcerr=True)
mstep=wmean2-wmean
mstepe=np.power(werr**2+werr2**2,.5)
mstep=0.022
mstepe=0.018
#0.022  0.018
print 'MASS FROM FITS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
#ax[2].text(7.1,-.18,"Hubble Step=",fontdict={'fontsize':15})
#ax[2].text(7.1,-.31,("{:10.3f}".format(mstep)+'+-'+"{:10.3f}".format(mstepe)).strip(),fontdict={'fontsize':15})


#stop
col=['b','g','r','c','m','y','r','g','m','b','g']

pos=[]



for i in range(1,299):
    pos.append(i/10.0-5)
pos2=[]

for i in range(1,299):
    pos2.append(0.0/100.0+0)

gs1 = gridspec.GridSpec(3, 1)
gs1.update(bottom=0.15, top=0.95, hspace=0.03)
ax1= plt.subplot(gs1[0])
ax2= plt.subplot(gs1[1])
ax3= plt.subplot(gs1[2])
ax=[ax1,ax2,ax3]



bins=[8,8.5,9,9.5,10,10.5,11,11.5,12,12.5]
line, = ax[0].plot(pos, pos2, lw=2,color='black')
line, = ax[1].plot(pos, pos2, lw=2,color='black')
line, = ax[2].plot(pos, pos2, lw=2,color='black')

line, = ax[0].plot([10,10], [-10,10], lw=2,color='black',linestyle='--',alpha=.5)
line, = ax[1].plot([10,10], [-10,10], lw=2,color='black',linestyle='--',alpha=.5)
line, = ax[2].plot([10,10], [-10,10], lw=2,color='black',linestyle='--',alpha=.5)

mstep=-0.210
mstepe=0.041
ax[0].text(8.1,-2.3,r"$x_1$"+" Step=")
ax[0].text(8.1,-3.1,("{:10.3f}".format(mstep)+'+-'+"{:10.3f}".format(mstepe)).replace(" ",""))

mstep=+0.012
mstepe=0.004
ax[1].text(8.1,-.23,"c Step=")
ax[1].text(8.1,-.31,("{:10.3f}".format(mstep)+'+-'+"{:10.3f}".format(mstepe)).replace(" ",""))


mstep=0.039
mstepe=0.016
ax[2].text(8.1,-.23,"HR Step=")
ax[2].text(8.1,-.31,("{:10.3f}".format(mstep)+'+-'+"{:10.3f}".format(mstepe)).replace(" ",""))



print 'mass2', mass2
digitized = np.digitize(mass2, bins)
bin_means = [(np.median(mures2[digitized == i])) for i in range(0, len(bins))]
bin_z = [mass2[digitized == i].mean() for i in range(0, len(bins))]
bin_std = [np.std(mass2[digitized == i])/np.sqrt(len(mass2[digitized == i])) for i in range(0, len(bins))]
ax[2].errorbar(mass2, mures2, yerr=np.zeros(len(mures2)), fmt='go', ecolor='g', alpha=.15)

ax[2].errorbar(bin_z, bin_means, yerr=bin_std, fmt='ko', ecolor='k')
ax[2].set_xlim(8,12.0)
ax[2].set_ylim(-.38,.35)
ax[2].set_ylabel('Hubble Res. (mag)')
ax[2].set_xlabel(r'${\rm log}_{10}(M_{\rm Stellar}/{M}_{\odot})$')

fsave.write("{:10.3f}".format(mstep)+' '+"{:10.3f}".format(mstepe))
#ax[0].set_xlabel('Mass')

digitized = np.digitize(mass2, bins)
bin_means = [(np.mean(c2[digitized == i])) for i in range(0, len(bins))]
bin_z = [mass2[digitized == i].mean() for i in range(0, len(bins))]
bin_std = [np.std(c2[digitized == i])/np.sqrt(len(mass2[digitized == i])) for i in range(0, len(bins))]
ax[1].errorbar(mass2, c2, yerr=np.zeros(len(c2)), fmt='go', ecolor='g', alpha=.15)

ax[1].errorbar(bin_z, bin_means, yerr=bin_std, fmt='ko', ecolor='k')
ax[1].set_xlim(8,12.0)
ax[1].set_ylim(-.35,.35)
ax[1].set_ylabel('c ')
#ax[1].set_xlabel('Mass')
print bin_means

digitized = np.digitize(mass2, bins)
bin_means = [(np.mean(x12[digitized == i])) for i in range(0, len(bins))]
bin_z = [mass2[digitized == i].mean() for i in range(0, len(bins))]
bin_std = [np.std(x12[digitized == i])/np.sqrt(len(mass2[digitized == i])) for i in range(0, len(bins))]
ax[0].errorbar(mass2, x12, yerr=np.zeros(len(x12)), fmt='go', ecolor='g', alpha=.15)

ax[0].errorbar(bin_z, bin_means, yerr=bin_std, fmt='ko', ecolor='k')
ax[0].set_xlim(8,12.0)
ax[0].set_ylim(-3.5,3.5)
ax[0].set_ylabel('x1 ')


ax2.set_xticklabels(['','','','','','','',''])
ax1.set_xticklabels(['','','','','','','',''])

fsave.close()
plt.show()


plt.savefig('ps1_mass.png')
xx=(mass2<10)
print np.median(x12[xx]),np.median(x12e[xx])/np.sqrt(len(x12e[xx]))
xx=(mass2>10)
print np.median(x12[xx]),np.median(x12e[xx])/np.sqrt(len(x12e[xx]))

xx=(mass2<10)
print np.median(c2[xx]),np.median(c2e[xx])/np.sqrt(len(c2e[xx]))
xx=(mass2>10)
print np.median(c2[xx]),np.median(c2e[xx])/np.sqrt(len(c2e[xx]))


#stop

def wmom(arrin, weightsin, inputmean=None, calcerr=False, sdev=False):
    """
    NAME:
      wmom()
      
    PURPOSE:
      Calculate the weighted mean, error, and optionally standard deviation
      of an input array.

    CALLING SEQUENCE:
     wmean,werr = wmom(arr, weights, inputmean=None, calcerr=False, sdev=False)
    
    INPUTS:
      arr: A numpy array or a sequence that can be converted.
      weights: A set of weights for each elements in array.
    OPTIONAL INPUTS:
      inputmean: An input mean value, around which them mean is calculated.
      calcerr=False: Calculate the weighted error.  By default the error
        is calculated as 1/sqrt( weights.sum() ).  In this case it is
        calculated as sqrt( (w**2 * (arr-mean)**2).sum() )/weights.sum()
      sdev=False: If True, also return the weighted standard deviation 
        as a third element in the tuple.

    OUTPUTS:
      wmean, werr: A tuple of the weighted mean and error. If sdev=True the
         tuple will also contain sdev: wmean,werr,wsdev

    REVISION HISTORY:
      Converted from IDL: 2006-10-23. Erin Sheldon, NYU

   """
    from np import float64
    
    # no copy made if they are already arrays
    arr = np.array(arrin, ndmin=1, copy=False)
    weights = np.array(weightsin, ndmin=1, copy=False)
    
    # Weights is forced to be type double. All resulting calculations
    # will also be double
    if weights.dtype != float64:
        weights = np.array(weights, dtype=float64)
  
    wtot = weights.sum()
        
    # user has input a mean value
    if inputmean is None:
        wmean = ( weights*arr ).sum()/wtot
    else:
        wmean=float(inputmean)

    # how should error be calculated?
    if calcerr:
        werr2 = ( weights**2 * (arr-wmean)**2 ).sum()
        werr = np.sqrt( werr2 )/wtot
    else:
        werr = 1.0/np.sqrt(wtot)

    # should output include the weighted standard deviation?
    if sdev:
        wvar = ( weights*(arr-wmean)**2 ).sum()/wtot
        wsdev = np.sqrt(wvar)
        return wmean,werr,wsdev
    else:
        return wmean,werr

asdf
