import os
import string
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import plotsetup
import linef
from matplotlib import gridspec
import matplotlib.ticker as ticker

plotsetup.halfpaperfig()

xcid, xred, xtype, xfield,xmjd = np.loadtxt('PS1_Noah2.txt', delimiter=' ', usecols=(0, 1,2,3,4), unpack=True, dtype='string', skiprows=2) 
print 'mjd', xred
#stop
#xred=xred[0]
xmjd = xmjd.astype(int)
xred = xred.astype(float)
print 'xr', xred
#stop
#list1, idsurvey, z1,x11,c1,mb1,mu1, mu1e = np.loadtxt('PS1_Scolnic/NewDan100f/FITOPT000+SALT2mu.FITRES', usecols=(1, 2,6,17,19,21,36,37), unpack=True, dtype='string', skiprows=15)
headn=linef.linef("../DATA/sntable_dump_SNANA.fitres",'z')
data1=np.genfromtxt("../DATA/sntable_dump_SNANA.fitres",skip_header=headn,names=True,comments='#')
cid=np.genfromtxt("../DATA/sntable_dump_SNANA.fitres",skip_header=headn,usecols=(1),comments='#',dtype='str')[1:]
z1 = data1['z'].astype(float)
#SNRMAX11=data1['SNRMAX1'].astype(float)
#x11 = data1['x1'].astype(float)
#c1 = data1['c'].astype(float)
#NDOF1=data1['NDOF'].astype(float)
#TGAPMAX1=data1['TGAPMAX'].astype(float)
#FITPROB=data1['FITPROB'].astype(float)
PKMJD=data1['PKMJDINI'].astype(float)
RA=data1['RA'].astype(float)
DECL=data1['DECL'].astype(float)
idsurvey=data1['IDSURVEY'].astype(float)
headn=linef.linef("../DATA/SALT2mu/SALT2mu_fitoptg0.fitres",'zCMB')
data1=np.genfromtxt("../DATA/SALT2mu/SALT2mu_fitoptg0.fitres",skip_header=headn,names=True,comments='#')
cid2=np.genfromtxt("../DATA/SALT2mu/SALT2mu_fitoptg0.fitres",skip_header=headn,usecols=(1),comments='#',dtype='str')[1:]

z2 = data1['zCMB'].astype(float)
SNRMAX12=data1['SNRMAX1'].astype(float)
x12 = data1['x1'].astype(float)
c2 = data1['c'].astype(float)
NDOF2=data1['NDOF'].astype(float)
TGAPMAX2=data1['TGAPMAX'].astype(float)
FITPROB2=data1['FITPROB'].astype(float)
PKMJD2=data1['PKMJD'].astype(float)
RA2=data1['RA'].astype(float)
DECL2=data1['DECL'].astype(float)
idsurvey2=(data1['IDSURVEY']).astype(float)


xx=np.where(idsurvey2==15)

z2=z2[xx]
SNRMAX12=SNRMAX12[xx]
x12=x12[xx]
c2=c2[xx]
NDOF2=NDOF2[xx]
TGAPMAX2=TGAPMAX2[xx]
FITPROB2=FITPROB2[xx]
PKMJD2=PKMJD2[xx]
RA2=RA2[xx]
DECL2=DECL2[xx]
cid2=cid2[xx]
for y in range(0,len(cid2)):
  xx=(cid2[y]==cid)
  print cid2[y]
  print 'xx', xx
  PKMJD2[y]=PKMJD[xx][0]
yy=np.where(xtype=='SNIa')
print yy[0]
print xred[yy[0]]
#stop
g=open('Table1.txt','w')

#plt.figure(1)
gs1 = gridspec.GridSpec(3, 1)
gs1.update(hspace=0.8,bottom=0.13,top=0.92)
ax3= plt.subplot(gs1[2])
ax2= plt.subplot(gs1[1])
ax1= plt.subplot(gs1[0])
ax=[ax1,ax2,ax3]


n, bins, patches = ax[0].hist(z1, bins=14,range=[0,.7], facecolor='g', alpha=0.35,label='Full PS1 Set')
n2, bins2, patches2 = ax[0].hist(z2, bins=14,range=[0,.7], histtype='step', alpha=0.65,linewidth=2,label='Cosmo PS1 Set',color='black')
ax[0].legend(loc='upper right',prop={'size':8})

ax[0].set_ylabel('\# of SNeIa')
ax[0].set_xlabel('z',labelpad=-2)
ax[0].yaxis.set_major_locator(ticker.MultipleLocator(20))

#ax[0].text(0.55,30,"z",fontdict={'fontsize':20})

field1,field2 = np.loadtxt('field.txt', delimiter=' ', usecols=(0, 1), unpack=True, dtype='string')
field1 = field1.astype(float)
field2=field2.astype(float)


vecx=[]
vecx2=[]
vecx3=[]

vecxb=[]
vecx2b=[]
vecx3b=[]
print 'xcid', xcid
print len(xcid)
#stop
for k in range(0,len(cid)):
  gg=np.where(xcid == cid[k])
  if (len(gg[0])>0):
    if (k<20):
      print cid[k], xmjd[gg[0]]-PKMJD2[k]
    x=xmjd[gg[0]]
    vecx3=np.append(vecx3,xmjd[gg[0]]-PKMJD[k])
    print field1, field2
    print 'k', k
    ee=np.power((field1-RA[k])*np.cos(np.absolute(3.14/180.0*(DECL[k]))),2)+np.power((field2-DECL[k]),2)
    print '3', 3.14/180.0*(DECL[k])
    print np.cos(3.14/180.0*(DECL[k]))
    #print np.power((field1-RA[k])/(np.arccos(3.14/180.0*(field2-DECL[k]))),2)
    print np.power((field2-DECL[k]),2)
    print 'ee', ee
    xx=np.isfinite(ee)
    if len(ee[xx])<10:
      stop
    zz1=np.amin(ee)
    zz2=np.where(ee==zz1)
    vecx=np.append(vecx,zz2[0])
    if (zz1<0): stop
    print 'np.sqrt(zz1)', np.sqrt(zz1)
    vecx2=np.append(vecx2,np.sqrt(zz1))

print len(cid), len(cid2)
print len(vecx), len(vecx2)
print vecx2
#stop
for k in range(0,len(cid2)):
  gg=np.where(xcid == cid2[k])
  if (len(gg)>0):
    x=xmjd[gg[0]]
    if (k<20):
      print cid2[k], xmjd[gg[0]]-PKMJD2[k]
    vecx3b=np.append(vecx3b,xmjd[gg[0]]-PKMJD2[k])
    ee=np.power((field1-RA2[k])*np.absolute((np.cos(3.14/180.0*(DECL2[k])))),2)+np.power((field2-DECL2[k]),2)
    
    zz1=np.amin(ee)
    zz2=np.where(ee==zz1)
    vecxb=np.append(vecxb,zz2[0])
    vecx2b=np.append(vecx2b,np.sqrt(zz1))
    if np.sqrt(zz1)>2.0:
      print cid2[k]
      print RA2[k], DECL2[k]
      print 'field', field1, field2
      
n, bins, patches = ax[1].hist(vecx2, bins=11,range=[-.5,1.6], facecolor='b', alpha=0.35)
print np.sum(n)
#stop
vecx2 = vecx2.astype(float)
xy=np.where(vecx2b>0.0)
print 'xy', xy
#xy=np.greater(vecx2,vecx2*0+.3 )
print 'vecx2', vecx2
print 'xy', xy
n2, bins2, patches2 = ax[1].hist(vecx2b[xy[0]], bins=11,range=[-.5,1.6], histtype='step', alpha=0.65,linewidth=2,color='black')
ax[1].yaxis.set_major_locator(ticker.MultipleLocator(20))
#ax[1].set_xlabel('Dist to Center (Deg)')
#ax[1].set_ylabel('#')
#ax[1].text(2.0,35,"Dist to Center",fontdict={'fontsize':20})
#ax[1].text(2.4,24,"(Deg)",fontdict={'fontsize':20})
ax[1].set_ylabel('\# of SNeIa')
ax[1].set_xlabel('Distance to MDF Center in Degrees',labelpad=-1)
ax[1].set_xlim(0,1.6)

print 'vecx3', vecx3
#stop
n, bins, patches = ax[2].hist(vecx3, bins=16,range=[-20,20], facecolor='r', alpha=0.35)

n2, bins2, patches2 = ax[2].hist(vecx3b, bins=16,range=[-20,20], histtype='step', alpha=0.65,linewidth=2,color='black')


#ax[2].set_xlabel('Disc before Peak (Days)')
#ax[2].set_ylabel('#')
#ax[2].text(4.7,35,"Disc before Peak",fontdict={'fontsize':20})
#ax[2].text(12,25,"(Days)",fontdict={'fontsize':20})
ax[2].set_ylabel('\# of SNeIa')
ax[2].set_xlabel('Rest-frame Discovery Phase in Days',labelpad=0)
plt.show()
plt.savefig('makeplot.png')
print 'vecx', vecx

str=['01','02','03','04','05','06','07','08','09','10']
print 'vecx', vecx
#stop
for l  in range(0,10):
    zz=np.where(xfield==('md'+str[l]))
    print 'l', l
    g.write(repr(field1[l])+' '+repr(field2[l])+' '+repr(len(zz[0]))+' '+repr(len(np.where(vecx==l)))+'\n')

g.close()

