import numpy as np
import matplotlib.pyplot as plt
import array
import math
from astropy import cosmology as cosmo
import matplotlib
import matplotlib.ticker as ticker
import plotsetup
from matplotlib import gridspec
import matplotlib.ticker as ticker
import linef
plotsetup.halfpaperfig()

def fform(num):
   if (num>0): return r"$\bar{\mathrm{z}}=$"+"{:10.2f}".format(num)
   if (num<0): return r"$\bar{\mathrm{z}}=\textrm{--}$"+"{:10.2f}".format(np.absolute(num))

def fformc(num):
   if (num>0): return r"$\bar{\mathrm{c}}=$"+"{:10.2f}".format(num)
   #if (num<0): return r"$\bar{\mathrm{c}}=\textrm{--}$"+"{:10.2f}".format(np.absolute(num))
   if (num<0): return r"$\bar{\mathrm{c}}=\textrm{--}$"+"{:10.2f}".format(np.absolute(num))
      
def fformx(num):
   if (num>0): return r"$\bar{\mathrm{x_1}}=$"+"{:10.2f}".format(num)
   if (num<0): return r"$\bar{\mathrm{x_1}}=\textrm{--}$"+"{:10.2f}".format(np.absolute(num))
      

#candels_hubble_62a.fitres
#list1, idsurvey, z1,x11,c1,mu1, mu1e = np.loadtxt('candels_hubble_0a.fitres', delimiter=' ', usecols=(0, 2,5,16,18,31,33), unpack=True, dtype='string', skiprows=2) 
#list1, idsurvey, z1,x11,c1,mu1, mu1e = np.loadtxt('candels_hubble_0a.fitres', delimiter=' ', usecols=(0,3, 6,17,19,35,37), unpack=True, dtype='string', skiprows=2)
#list1, idsurvey, z1,x11,c1,mu1, mu1e = np.loadtxt('wc0a.fitres', delimiter=' ', usecols=(0,3, 6,17,19,31,33), unpack=True, dtype='string', skiprows=12)
list1, idsurvey, z1,mass,x11,c1,mb1,mu1, mu1e,mures = np.loadtxt('../DATA/SALT2mu/SALT2mu_fitoptg0.fitres', usecols=(1,3, 7,13,20,22,24,37,39,41), unpack=True, dtype='string', skiprows=15)

name1='../DATA/SALT2mu/SALT2mu_fitoptg0.fitres'
header1=linef.linef('../DATA/SALT2mu/SALT2mu_fitoptg0.fitres','zCMB')
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
mures=data1['MURES'].astype(float)
mu1=data1['MU'].astype(float)
mu1e=data1['MUERR'].astype(float)
#muerr=1.0/muerr**2

print idsurvey1


#list1,idsurvey,z1,SNRMAX11,x11,c1 ,NDOF1 ,TGAPMAX1 = np.loadtxt('PS1_Scolnic/NewDan100f/FITOPT000+SALT2mu.FITRES', delimiter=' ', usecols=(1,3,8,12,17,19,28,31), unpack=True, dtype='string', skiprows=16) 

print c1
#asdf
z1 = z1.astype(float)

c1 = c1.astype(float)
x11 = x11.astype(float)
#sdf

print 'z', z1

survey=1
tempsurv=[]
tempz=[]
tempmu=[]
tempmue=[]
uniqsurv=set(idsurvey1)
uniqsurv=['54', '50', '53', '1', '5', '4', '106','111','116','15']
uniqsurv=['54', '50', '53', '1', '5', '4', '15']

print uniqsurv

col=['b','g','r','c','m','y','r','g','m','b','g']

pos=[]

zmean=[]
gs1 = gridspec.GridSpec(3, 1)
gs1.update(bottom=0.1, top=0.95, hspace=0.45)
ax1= plt.subplot(gs1[0])
ax2= plt.subplot(gs1[1])
ax3= plt.subplot(gs1[2])
ax=[ax1,ax2,ax3]

co=0
bins = range(15, 25)
#ax[0].xticks(bins, ["2^%s" % i for i in bins])

xx=np.where(idsurvey1==15)
n, bins, patches = ax[0].hist(z1[xx[0]],  bins=np.logspace(-2, 0.28, 25,base=10),range=[0,2], facecolor='blue', alpha=0.85,color=col[co],linewidth=2, histtype='step')
zmean=np.append(zmean,np.median(z1[xx[0]]))
print 'log', np.logspace(0.01, 1.0, 20)
xx=np.where(idsurvey1==1)
n, bins, patches = ax[0].hist(z1[xx[0]],  bins=np.logspace(-2, 0.28, 25,base=10),range=[0,2], histtype='step', alpha=0.75,color='green',linewidth=2)
zmean=np.append(zmean,np.median(z1[xx[0]]))
xx=np.where(idsurvey1==4)
n, bins, patches = ax[0].hist(z1[xx[0]],  bins=np.logspace(-2, 0.28, 25,base=10),range=[0,2], histtype='step', alpha=0.75,color='red',linewidth=2)
zmean=np.append(zmean,np.median(z1[xx[0]]))
print np.median(z1[xx[0]])

xx=np.where((idsurvey1!=15) & (idsurvey1!=1) & (idsurvey1!=4)&(z1<0.1))
n, bins, patches = ax[0].hist(z1[xx[0]],  bins=np.logspace(-2, 0.28, 25),range=[0,2], histtype='step', alpha=0.75,color='black',linewidth=2)
zmean=np.append(zmean,np.median(z1[xx[0]]))

xx=np.where((idsurvey1!=15) & (idsurvey1!=1) & (idsurvey1!=4)&(z1>0.5))
n, bins, patches = ax[0].hist(z1[xx[0]],  bins=np.logspace(-2, 0.28, 25),range=[0,2], histtype='step', alpha=0.75,color='purple',linewidth=2)
zmean=np.append(zmean,np.median(z1[xx[0]]))


str2=['black','green','blue','red','purple']
proxy = [plt.Rectangle((0,0),.02,.02,fc = str2[pc]) for pc in range(0,5)]
ax[0].legend(proxy, ["Low-z  "+fform(zmean[3]).strip(), "SDSS  "+fform(zmean[1]).strip(),"PS1  "+fform(zmean[0]).strip(), "SNLS  "+fform(zmean[2]).strip(), "HST  "+fform(zmean[4]).strip()],loc='upper left',prop={'size':8},frameon=False,fontsize=8,ncol=2)
#,'weight':'bold'
ax[0].set_xlim(0.006,2)
ax[0].set_ylim(0.0,100)

#.xlim([0,0.7])
ax[0].set_xlabel('z',labelpad=-1)
ax[0].set_ylabel('\# of SNeIa')
#plt.text(1.0,80,"z",fontdict={'fontsize':20})
ax[0].set_xscale("log")

ax[0].set_xticklabels(['0.01','','0.01','0.10','1.00'])

ax[0].text(0.01,25,"Low-z",color=str2[0]) 
ax[0].text(0.06,40,"SDSS",color=str2[1])
ax[0].text(0.33,60,"PS1",color=str2[2])
ax[0].text(0.8,60,"SNLS",color=str2[3])
ax[0].text(1.0,20,"HST",color=str2[4])

co=0
zmean=[]
xx=np.where(idsurvey1==15)
n, bins, patches = ax[1].hist(c1[xx[0]], bins=20,range=[-.3,.3], facecolor='blue', alpha=0.85,color=col[co],linewidth=2, histtype='step')
zmean=np.append(zmean,np.median(c1[xx[0]]))

xx=np.where(idsurvey1==1)
n, bins, patches = ax[1].hist(c1[xx[0]], bins=20,range=[-.3,.3], histtype='step', alpha=0.75,color='green',linewidth=2)
zmean=np.append(zmean,np.median(c1[xx[0]]))

xx=np.where(idsurvey1==4)
n, bins, patches = ax[1].hist(c1[xx[0]], bins=20,range=[-.3,.3], histtype='step', alpha=0.75,color='red',linewidth=2)
zmean=np.append(zmean,np.median(c1[xx[0]]))
xx=np.where((idsurvey1!=15) & (idsurvey1!=1) & (idsurvey1!=4))
n, bins, patches = ax[1].hist(c1[xx[0]], bins=20,range=[-.3,.3], histtype='step', alpha=0.75,color='black',linewidth=2)
zmean=np.append(zmean,np.median(c1[xx[0]]))


xx=np.where((idsurvey1!=15) & (idsurvey1!=1) & (idsurvey1!=4)&(z1>0.5))
n, bins, patches = ax[1].hist(c1[xx[0]], bins=20,range=[-.3,.3], histtype='step', alpha=0.75,color='purple',linewidth=2)
zmean=np.append(zmean,np.median(c1[xx[0]]))


str2=['black','green','blue','red','purple']
proxy = [plt.Rectangle((0,0),.02,.02,fc = str2[pc]) for pc in range(0,5)]
ax[1].legend(proxy, ["Low-z  "+fformc(zmean[3]).strip(), "SDSS  "+fformc(zmean[1]).strip(),"PS1  "+fformc(zmean[0]).strip(), "SNLS  "+fformc(zmean[2]).strip(), "HST  "+fformc(zmean[4]).strip()],loc='upper left',prop={'size':8},frameon=False,fontsize=8,ncol=2)


ax[1].set_xlabel('c',labelpad=-1)
ax[1].set_ylabel('\# of SNeIa')
ax[1].set_xlim(-.30,.30)
ax[1].set_ylim(0,100)

#plt.text(.2,60,"c",fontdict={'fontsize':20})


zmean=[]
co=0
xx=np.where(idsurvey1==15)
n, bins, patches = ax[2].hist(x11[xx[0]], bins=15,range=[-3,3], facecolor='blue', alpha=0.85,color=col[co],linewidth=2, histtype='step')
zmean=np.append(zmean,np.median(x11[xx[0]]))

xx=np.where(idsurvey1==1)
n, bins, patches = ax[2].hist(x11[xx[0]], bins=15,range=[-3,3], histtype='step', alpha=0.75,color='green',linewidth=2)
zmean=np.append(zmean,np.median(x11[xx[0]]))
xx=np.where(idsurvey1==4)
n, bins, patches = ax[2].hist(x11[xx[0]], bins=15,range=[-3,3], histtype='step', alpha=0.75,color='red',linewidth=2)
zmean=np.append(zmean,np.median(x11[xx[0]]))
xx=np.where((idsurvey1!=15) & (idsurvey1!=1) & (idsurvey1!=4))
n, bins, patches = ax[2].hist(x11[xx[0]], bins=15,range=[-3,3], histtype='step', alpha=0.75,color='black',linewidth=2)
zmean=np.append(zmean,np.median(x11[xx[0]]))

xx=np.where((idsurvey1!=15) & (idsurvey1!=1) & (idsurvey1!=4)&(z1>0.5))
n, bins, patches = ax[2].hist(x11[xx[0]], bins=15,range=[-.3,.3], histtype='step', alpha=0.75,color='purple',linewidth=2)
zmean=np.append(zmean,np.median(x11[xx[0]]))


str2=['black','green','blue','red','purple']
proxy = [plt.Rectangle((0,0),.02,.02,fc = str2[pc]) for pc in range(0,5)]
ax[2].legend(proxy, ["Low-z  "+fformx(zmean[3]).strip(), "SDSS  "+fformx(zmean[1]).strip(),"PS1  "+fformx(zmean[0]).strip(), "SNLS  "+fformx(zmean[2]).strip(), "HST  "+fformx(zmean[4]).strip()],loc='upper left',prop={'size':8},frameon=False,fontsize=8,ncol=2)

#plt.text(2.1,45,"x1",fontdict={'fontsize':20})

ax[2].set_xlabel(r'$x_1$',labelpad=-1)
ax[2].set_ylabel('\# of SNeIa')
ax[2].set_ylim(0.0,100)
ax[2].set_xlim(-3.0,3.0)

ax[0].yaxis.set_major_locator(ticker.MultipleLocator(20))
ax[1].yaxis.set_major_locator(ticker.MultipleLocator(20))
ax[2].yaxis.set_major_locator(ticker.MultipleLocator(20))

plt.show()

plt.savefig('csz_hist.png')

asdf
