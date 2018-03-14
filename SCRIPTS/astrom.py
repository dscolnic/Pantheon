import numpy as np
import string
import matplotlib.pyplot as plt
from scipy import ndimage
from sklearn.gaussian_process import GaussianProcess
import matplotlib.cm as cm
import os
import matplotlib
import plotsetup
plotsetup.halfpaperfig()



val1,val2,val3,val4,val5,fil = np.loadtxt('wcs_all.txt', usecols=(0,1,2,3,4,5), unpack=True, dtype='string', skiprows=16)
val1=val1.astype(float)
val2=val2.astype(float)
val3=val3.astype(float)
val4=val4.astype(float)
val5=val5.astype(float)
fil=fil.astype(float)

val1=val1*3600.0*4.0*np.cos(val4*3.14/180.0)
val2=val2*3600.0*4.0

plt.figure(1)
f, ax = plt.subplots(2)

#f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
#ax1.set_title('Sharing x per column, y per row')
#      16.1788997999999999      -0.0624315568115250 g  02  016
strf=['g','r','i','z']
for j in range(0,1):
  
  #val2=(val2-val1)
 
  #print range(16,23,.25)
  #stop
  aval1=0.0
  aval2=0.0
  weights=0.0
  for k in range(0,3):
    aval1x,avalbx,aval2x = np.loadtxt('/project/rkessler/dscolnic/PS1_analysis/astro2_'+repr(k)+'.txt', usecols=(0,1,2), unpack=True, dtype='string', skiprows=16)                   
    aval1x=aval1x.astype(float)
    aval2x=aval2x.astype(float)
    weights=val2*0+1.0
    aval1=np.append(aval1,aval1x)
    aval2=np.append(aval2,aval2x)
  means1=[]
  means1x=[]
  means2=[]
  means2x=[]
  b1=[0,1,2,3,4,5,6,7,8,9,10,11]
  bins=np.power(1.5,b1)*.01
  #bins=[0,0.01,0.0150.02,0.04,0.08,0.16,0.32,0.64]
  for x in range(0,len(bins)-1):
        xx=np.where((val5>bins[x])&(val5<(bins[x+1])))
        print 'xx', xx[0]
        if len(xx[0])>2:
          print x,1.48*np.median(np.absolute(val2[xx[0]]))
          #weights[xx[0]]=1.0/len(xx[0])
          r=1
          means1=np.append(means1,1.48*np.median(np.absolute(val2[xx[0]])))
          means1x=np.append(means1x,np.median(val5[xx[0]]))
  for x in range(0,len(bins)-1):
        xx=np.where((aval1>bins[x])&(aval1<(bins[x+1])))
        print 'xx', xx[0]
        if len(xx[0])>2:
          print 'and',x,1.48*np.median(np.absolute(aval2[xx[0]]))
          #weights[xx[0]]=1.0/len(xx[0])                                                                                                                                
          means2=np.append(means2,1.48*np.median(np.absolute(aval2[xx[0]])))
          means2x=np.append(means2x,np.median(aval1[xx[0]]))
          r=1
  pos=[]



  for i in range(0,299):
    pos.append(i/300.0)
  pos2=[]
  pos3=[]
  for i in range(0,299):
    pos2.append(0.2**2+float(i)/300.0*1.5**2)
    pos3.append(0.1**2+float(i)/300.0*1.5**2)
  x=np.arange(0,2,.1)  
  print 'means1', means1
  print 'means2', means2
  print 'pos2', pos, pos2
  line, = ax[0].plot(x, .1**2+(.75**2)*x,lw=2,color='green')
  line, = ax[0].plot(x, .2**2+(1.5**2)*x,lw=2,color='black')

  #p1=ax[0].errorbar(means1x, means1, yerr=(means1*0)+.01, fmt='ko', ecolor='blue', color='blue',label='Stars')
  p2=ax[0].errorbar(means2x, means2**2, yerr=(means2x**2)*.1, fmt='ko', ecolor='r', color='r',label='Binned SNe')
  ax[0].set_ylim(0,.4)
  ax[0].set_xlim(0,.35)
  ax[0].set_xlabel(r'(FWHM/SNR)$^2$')
  ax[0].set_ylabel('Astr. Pixel \n Variance '+r'$\sigma^2_{\Delta y}$')
  ax[0].legend(loc='upper left',numpoints=1,fontsize=12)
  ax[0].text(0.15,0.51**2+.05,"R14", color='black',rotation=25)
  ax[0].text(0.2,0.3**2+.02,"This Work", color='green',rotation=12)
  ax[0].set_yticks([0,0.2,0.4,0.6,])
  #ax[0].set_yticklabels(['','','','','','',''])


 
z=[]
err=[]
err2=[]
cntr=[]
offset=[]
offsetp=[]
cntrlines=open('allcntr.dat','r').readlines()
for x in cntrlines:
  cntr=np.append(cntr,x[68:74])
  offset=np.append(offset,float(x[131:137]))
file1='../DATA/DS17_PS1_Scolnic2/PS1_Spec_DS17/FITOPT000.FITRES'
if (os.path.isfile(file1)==False): os.system('gunzip '+file1+'.gz')
#name1,z1,SNRMAX11,x11,c1 ,NDOF1 ,TGAPMAX1 = np.loadtxt('../DATA/DS16_PS1_Scolnic2/NewDan101f_DS16/FITOPT000.FITRES', usecols=(1,7,12,17,19,28,33), unpack=True, dtype='string', skiprows=16)
import linef
headn=linef.linef(file1,'zCMB')
data1=np.genfromtxt(file1,skip_header=headn,names=True,comments='#')
name1=np.genfromtxt(file1,skip_header=headn,usecols=(1),comments='#',dtype='str')[1:]
z1 = data1['zCMB'].astype(float)
z=[]
err2=[]
print 'cntr', cntr


for i in range(0,len(name1)):
   xxc=(name1[i]==cntr)
   print 'xxc', xxc   
   if (len(cntr[xxc])>0):
              z=np.append(z,float(z1[i]))
              offsetp=np.append(offsetp,float(offset[xxc][0]))
print 'z', len(z)
print 'err2', len(err2)
print offsetp
p1=ax[1].errorbar(z,offsetp*.5, yerr=(offsetp*0), fmt='ko', ecolor='blue', color='blue',label='Stars')
ax[1].set_xlim(0,.7)

line, = ax[1].plot(pos, np.multiply(pos,.002)*.5,lw=2,color='orange')  
ax[1].set_xlabel('z')
ax[1].set_ylabel('Phot. Bias Due to \n Astr. Uncertainty (mag)')
ax[1].set_ylim(0,.015*.5)
ax[1].set_yticks([0,0.002,0.004,0.006])
plt.tight_layout()
plt.show()
plt.savefig('astrom.png')
