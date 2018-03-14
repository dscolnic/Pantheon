import numpy as np
import matplotlib.pyplot as plt
import array
import math
from astropy.cosmology import FlatLambdaCDM
import matplotlib
import wmom
from numpy.polynomial import polynomial as P
import matplotlib
from scipy.interpolate import interp1d
import plotsetup
import string
import linef
plotsetup.halfpaperfig()



def func(x, a, b):
          return a * x + b

def grabfitres(file1, variable, num):
    g=open(file1,'r')
    co=0
    coall=0
    for line in g:
        if variable in line:
            x=string.split(line)
            return [(x[3]),x[5]]
        
def prec(x):
    return '('+"%.3f"%float(x[0])+'\pm'+"%.3f"%float(x[1])+')'
        
        
        
cosmo = FlatLambdaCDM(H0=70, Om0=0.3)
#SALT2mu/SALT2mu_fitoptgb0.fitres
#  -0.081421771     0.081707301     0.031227249     0.054284053
#    -0.081480861     0.076136832     0.025882917     0.045994964

#../DATA/SALT2mu/SALT2mu_fitoptgm0.fitres
#list1, idsurvey,z1, mass1,x11,c1,mu1, mu1e = np.loadtxt('../DATA/SALT2mu_fitopt.fitres', usecols=(0,3, 7,13,18,20,37,39), unpack=True, dtype='string', skiprows=12)
headn=linef.linef('../DATA/SALT2mu_SNLS+SDSS+LOWZ+PS1_Scolnic2+HST/DS17/SALT2mu_FITOPT000_MUOPT000.FITRES','zCMB')
data1=np.genfromtxt('../DATA/SALT2mu_SNLS+SDSS+LOWZ+PS1_Scolnic2+HST/DS17/SALT2mu_FITOPT000_MUOPT000.FITRES',skip_header=headn,names=True,comments='#')
list1=np.genfromtxt('../DATA/SALT2mu_SNLS+SDSS+LOWZ+PS1_Scolnic2+HST/DS17/SALT2mu_FITOPT000_MUOPT000.FITRES',skip_header=headn,usecols=(1),comments='#',dtype='str')[1:]
z1 = data1['zCMB'].astype(float)
SNRMAX11=data1['SNRMAX1'].astype(float)
x11 = data1['x1'].astype(float)
c1 = data1['c'].astype(float)
mu1 = data1['MU'].astype(float)
mu1e = data1['MUERR'].astype(float)
mass=data1['HOST_LOGMASS'].astype(float)
idsurvey=data1['IDSURVEY']
MWEBV=data1['MWEBV']

for x in np.unique(idsurvey):
          xx=[idsurvey==x]
          print x,np.median(MWEBV[xx])
print np.median(MWEBV[z1>1.2])
#stop
#.astype(float)

#list1, idsurvey,z1, mass1,x11,c1,mu1, mu1e = np.loadtxt('/project/rkessler/dscolnic/Tutor/DATA/DS16/MALL/_DS16/SALT2mu_FITOPT000_MUOPT005.FITRES', usecols=(0,3, 7,13,18,20,37,39), unpack=True, dtype='string', skiprows=12)
#list2, idsurvey2,z2, mass2,x12,c2,mu2, mu2e = np.loadtxt('../DATA/SALT2mu_fitopt_C11.fitres', usecols=(0,3, 7,13,18,20,37,39), unpack=True, dtype='string', skiprows=12)
headn=linef.linef('../DATA/SALT2mu_SNLS+SDSS+LOWZ+PS1_Scolnic2+HST/DS17/SALT2mu_FITOPT000_MUOPT001.FITRES','zCMB')

data1=np.genfromtxt('../DATA/SALT2mu_SNLS+SDSS+LOWZ+PS1_Scolnic2+HST/DS17/SALT2mu_FITOPT000_MUOPT001.FITRES',skip_header=headn,names=True,comments='#')
list1=np.genfromtxt('../DATA/SALT2mu_SNLS+SDSS+LOWZ+PS1_Scolnic2+HST/DS17/SALT2mu_FITOPT000_MUOPT000.FITRES',skip_header=headn,usecols=(1),comments='#',dtype='str')[1:]
z2 = data1['zCMB'].astype(float)
SNRMAX12=data1['SNRMAX1'].astype(float)
x12 = data1['x1'].astype(float)
c2 = data1['c'].astype(float)
mu2 = data1['MU'].astype(float)
mu2e = data1['MUERR'].astype(float)
mass2=data1['HOST_LOGMASS'].astype(float)
idsurvey2=data1['IDSURVEY']
#.astype(float)

gamma1=0.053
gamma1e=0.009
m=[0.08,-0.1]
print mu1



xx=[mass<10]
mu1[xx]=mu1[xx]+gamma1



z2 = z2.astype(float)
mu2 = mu2.astype(float)

mu2e = mu2e.astype(float)
mass2 = mass2.astype(float)
xx=[mass2<10]
mu2[xx]=mu2[xx]+gamma1

c2 = c2.astype(float)
x12=x12.astype(float)

x=cosmo.luminosity_distance(z1).value
mu_syn1=5.0*(np.log10(x))+25.0
mures=mu1-mu_syn1

x=cosmo.luminosity_distance(z2).value
mu_syn2=5.0*(np.log10(x))+25.0
mures2=mu2-mu_syn2
mures2=mures2-np.median(mures2)

bins=[0,.1,.2,.3,.4,.5,.6,.7,.8,1.0]
digitized = np.digitize(z1, bins)

#bin_means = [(np.median(temp[digitized == i])) for i in range(0, len(bins))]

#rmass rz rr1 

#stop
#mures=mures-np.median(mures)-f(c1)
mures=mures-np.median(mures)
print 'mass', mass
#stp
xx=np.where((mass<1)&(z1<.1))
xx=np.where((mass<1)&(z1>.1))
xx1=np.where((mass<1)&(idsurvey==15))
xx2=np.where((mass>1)&(idsurvey==15))

print len(xx[0]), len(mass)
print len(xx1[0]),len(xx2[0])


xx=np.where((mass>1))
xxad=np.where((mass>1)&(z1<.1))
print np.median(mass[xxad])
z1=z1[xx[0]]
x11=x11[xx[0]]
c1=c1[xx[0]]
mu1=mu1[xx[0]]
mures=mures[xx[0]]
mu1e=mu1e[xx[0]]
mass=mass[xx[0]]
idsurvey=idsurvey[xx[0]]
xx1=np.where(mass>10.0)
xx2=np.where(mass<10.0)


xx=np.where((mass2>1))
idsurvey2=idsurvey2[xx]
z2=z2[xx[0]]
x12=x12[xx[0]]
c2=c2[xx[0]]
mu2=mu2[xx[0]]
mures2=mures2[xx[0]]
mu2e=mu2e[xx[0]]
mass2=mass2[xx[0]]
yy1=np.where(mass2>10.0)
yy2=np.where(mass2<10.0)

yy1=np.where(mass2>10.0)
yy2=np.where((mass2<10.0)&(mass2>1))
#rmass rz rr1                                                                                                                                                                                                
v1=open('vari_ps1m.tex','w')

#mstep=np.median(mures2[xx1[0]])-np.median(mures2[xx2[0]])
wmean,werr = wmom.wmom(mures[xx1[0]], 1.0/mu1e[xx1[0]], calcerr=True)
wmean2,werr2 = wmom.wmom(mures[xx2[0]], 1.0/mu1e[xx2[0]], calcerr=True)
mstep=wmean2-wmean
mstepe=np.power(werr**2+werr2**2,.5)
print 'mstep',wmean2,wmean, mstep,mstepe, len(xx1[0])+len(xx2[0]), len(xx1[0]), len(xx2[0]), np.sum(mures**2/mu1e**2)
mstep="%.3f"%mstep
mstepe="%.3f"%mstepe
v1.write('\\newcommand{\\massallstepa}{\ensuremath{'+str(mstep)+'}}\n')
v1.write('\\newcommand{\\massallstepe}{\ensuremath{'+str(mstepe)+'}}\n')
v1.write('\\newcommand{\\massalllow}{\ensuremath{'+str(len(xx2[0]))+'}}\n')
v1.write('\\newcommand{\\massallhigh}{\ensuremath{'+str(len(xx1[0]))+'}}\n')


wmean,werr = wmom.wmom(mures2[yy1[0]], 1.0/mu2e[yy1[0]], calcerr=True)
wmean2,werr2 = wmom.wmom(mures2[yy2[0]], 1.0/mu2e[yy2[0]], calcerr=True)
mstep=wmean2-wmean
mstepe=np.power(werr**2+werr2**2,.5)
mstep="%.3f"%mstep
mstepe="%.3f"%mstepe
print 'mstep color ', wmean2,wmean,mstep,mstepe, len(yy1[0])+len(yy2[0]), len(xx1[0]),len(xx2[0]), np.sum(mures2**2/mu2e**2)
v1.write('\\newcommand{\\masscallstepa}{\ensuremath{'+str(mstep)+'}}\n')
v1.write('\\newcommand{\\masscallstepe}{\ensuremath{'+str(mstepe)+'}}\n')
v1.write('\\newcommand{\\masscalllow}{\ensuremath{'+str(len(xx2[0]))+'}}\n')
v1.write('\\newcommand{\\masscallhigh}{\ensuremath{'+str(len(xx1[0]))+'}}\n')

#stop


survs=[15,1,4,0,100]
survi=['ps','sdss','snls','lowz','hst']
for i in range(0,len(survs)):
    x=survs[i]
    if (i<3):
              xx1=np.where((mass>10.0)&(idsurvey==x))
              xx2=np.where((mass<10.0)&(idsurvey==x))
              yy1=np.where((mass2>10.0)&(idsurvey2==x))
              yy2=np.where((mass2<10.0)&(mass2>1)&(idsurvey2==x))
              print idsurvey[xx1]
              print idsurvey
              #stop
    if (i==3):
              xx1=np.where((mass>10.0)&(idsurvey!=1)&(idsurvey!=4)&(idsurvey!=15)&(z1<0.1))
              xx2=np.where((mass<10.0)&(idsurvey!=1)&(idsurvey!=4)&(idsurvey!=15)&(z1<0.1))
              yy1=np.where((mass2>10.0)&(idsurvey2!=1)&(idsurvey2!=4)&(idsurvey2!=15)&(z2<0.1))
              yy2=np.where((mass2<10.0)&(mass2>1)&(idsurvey2!=1)&(idsurvey2!=4)&(idsurvey2!=15)&(z2<0.1))

    if (i==4):
              xx1=np.where((mass>10.0)&(idsurvey!=1)&(idsurvey!=4)&(idsurvey!=15)&(z1>0.1))
              xx2=np.where((mass<10.0)&(idsurvey!=1)&(idsurvey!=4)&(idsurvey!=15)&(z1>0.1))
              yy1=np.where((mass2>10.0)&(idsurvey2!=1)&(idsurvey2!=4)&(idsurvey2!=15)&(z2>0.1))
              yy2=np.where((mass2<10.0)&(mass2>1)&(idsurvey2!=1)&(idsurvey2!=4)&(idsurvey2!=15)&(z2>0.1))
              
    wmean,werr = wmom.wmom(mures[xx1[0]], 1.0/mu1e[xx1[0]], calcerr=True)
    wmean2,werr2 = wmom.wmom(mures[xx2[0]], 1.0/mu1e[xx2[0]], calcerr=True)
    mstep=wmean2-wmean
    mstepe=np.power(werr**2+werr2**2,.5)
    mstep="%.3f"%mstep
    mstepe="%.3f"%mstepe
    print 'survey ', x, 'mstep',wmean2,wmean, 'step',mstep,mstepe, len(xx1[0])+len(xx2[0]), len(xx1[0]), len(xx2[0]), np.sum(mures**2/mu1e**2)
    v1.write('\\newcommand{\\mass'+survi[i]+'stepa}{\ensuremath{'+str(mstep)+'}}\n')
    v1.write('\\newcommand{\\mass'+survi[i]+'stepe}{\ensuremath{'+str(mstepe)+'}}\n')
    v1.write('\\newcommand{\\mass'+survi[i]+'low}{\ensuremath{'+str(len(xx2[0]))+'}}\n')
    v1.write('\\newcommand{\\mass'+survi[i]+'high}{\ensuremath{'+str(len(xx1[0]))+'}}\n')
    

    wmean,werr = wmom.wmom(mures2[yy1[0]], 1.0/mu2e[yy1[0]], calcerr=True)
    wmean2,werr2 = wmom.wmom(mures2[yy2[0]], 1.0/mu2e[yy2[0]], calcerr=True)
    mstep=wmean2-wmean
    mstepe=np.power(werr**2+werr2**2,.5)
    mstep="%.3f"%mstep
    mstepe="%.3f"%mstepe
    print 'survey ', x,'mstep color ', wmean2,wmean,'step',mstep,mstepe, len(yy1[0])+len(yy2[0]), len(xx1[0]),len(xx2[0]), np.sum(mures2**2/mu2e**2)
    v1.write('\\newcommand{\\massc'+survi[i]+'stepa}{\ensuremath{'+str(mstep)+'}}\n')
    v1.write('\\newcommand{\\massc'+survi[i]+'stepe}{\ensuremath{'+str(mstepe)+'}}\n')
    v1.write('\\newcommand{\\massc'+survi[i]+'low}{\ensuremath{'+str(len(xx2[0]))+'}}\n')
    v1.write('\\newcommand{\\massc'+survi[i]+'high}{\ensuremath{'+str(len(xx1[0]))+'}}\n')
                  

v1.close()






print 'xx1', np.median(mures[xx2[0]])-np.median(mures[xx1[0]])
print (np.power(np.std(mures[xx2[0]])/np.sqrt(len(xx2[0])),2)+np.power(np.std(mures[xx2[0]])/np.sqrt(len(xx2[0])),2))**.5

for x2 in range(0,10):
    x=x2/10.0
    xx1=np.where((z1>(x)) & (z1<(x+.1)) & (mass>10.0))
    xx2=np.where((z1>(x)) & (z1<(x+.1)) & (mass<10.0))

    #print np.median(mures[xx1[0]]), len(xx1[0])
    #print np.median(mures[xx2[0]]), len(xx2[0])
    print np.median(mures[xx1[0]])-np.median(mures[xx2[0]]), len(xx1[0]), len(xx2[0])
    #print name1[xx1[0]]
    #print name1[xx2[0]]

    xx1=np.where((z1>(x)) & (z1<(x+.1)) & (mass>10.0) & (c1>-0.1) & (x11<1))
    xx2=np.where((z1>(x)) & (z1<(x+.1)) & (mass<10.0) & (c1>-0.1) & (x11<1))
    print 'color split', np.median(mures[xx1[0]])-np.median(mures[xx2[0]]), len(xx1[0]), len(xx2[0])

#stop
fig, ax = plt.subplots(2,1)

pos=[]



for i in range(1,299):
    pos.append(i/10.0-5)
pos2=[]

for i in range(1,299):
    pos2.append(0.0/100.0+0)


bins=[8,8.5,9,9.5,10,10.5,11,11.5,12,12.5]
line, = ax[0].plot(pos, pos2, lw=2)
line, = ax[0].plot([10,10], [-5,5], lw=1, linestyle='--')

#-0.094143366      0.14642234     0.030800737     0.080101205
digitized = np.digitize(mass, bins)
bin_means = [(np.median(mures[digitized == i])) for i in range(0, len(bins))]
bin_z = [mass[digitized == i].mean() for i in range(0, len(bins))]
bin_std = [np.std(mures[digitized == i])/np.sqrt(len(mass[digitized == i])) for i in range(0, len(bins))]



ax[0].errorbar(mass, mures, yerr=np.zeros(len(mures)), fmt='go', ecolor='g', alpha=.15)
ax[0].errorbar(bin_z, bin_means, yerr=bin_std, fmt='ko', ecolor='k')
ax[0].set_xlim(7,12.3)
ax[0].set_ylim(-.35,.35)
ax[0].set_ylabel('Hubble Residual (mag)')
ax[0].set_xlabel(r'$\textrm{log}_{10}(M_{Stellar}/M_{\odot})$')

ax[0].text(7.15,-.28,"Hubble Step\n"+("{:10.3f}".format(gamma1)+r'$\pm$'+"{:10.3f}".format(gamma1e)).replace(" ","")+'\n [mag]',fontdict={'fontsize':8})                                                                                                                           
#ax[0].text(11.4,-.27,("{:10.3f}".format(gamma1)+r'$\pm$'+"{:10.3f}".format(gamma1e)).replace(" ","")+' mag',fontdict={'fontsize':12})                                                                        

print 'means', bin_means
bins=[0,.1,.2,.3,.4,.5,.6,.7,.8,1.0]
bins=[0.01,
      0.06,
      0.115,
      0.177,
      0.247,
      0.328,
      0.42,
      0.528,
      .656,
      0.81,
      1.0]
#line, = ax[1].plot(pos, pos2, lw=2)
line, = ax[1].plot([-10,10], [0,0], linestyle='--',lw=2,color='black')
ax[1].text(0.05,-0.04,r'$\gamma_0=0$',fontdict={'fontsize':10},color='black')
    
red2=bins

gamma=[]
gammaerr=[]
red=[]
gammab=[]
gammaerrb=[]
redb=[]
for num in range(0,len(red2)-1):
        red=np.append(red,(red2[num]+red2[num+1])/2.0)

for x in range(0,10):
     temp=grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgb'+str(x)+'.fitres','gamma0',3)
     gamma=np.append(gamma,float(temp[0]))
     gammaerr=np.append(gammaerr,float(temp[1]))
for x in range(0,10):
    temp=grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgb'+str(x)+'.fitres','gamma0',3)
    gammab=np.append(gammab,float(temp[0]))
    gammaerrb=np.append(gammaerrb,float(temp[1]))

lx=np.array([0, .75, 1.5], dtype='f')
print m

line, = ax[1].plot(lx,lx*m[1]+m[0], lw=2)
line, = ax[1].plot(lx,lx*0+gamma1, lw=2,linestyle='--')
ax[1].text(0.7,0.06,r'$\gamma_0=0.050$',fontdict={'fontsize':10},color='green')
ax[1].text(0.6,-0.04,r'$\gamma_(z)=0.07-0.07z$',fontdict={'fontsize':10},color='blue',rotation=-8)

print m[0]/np.power(7,.5)
print red.shape, gamma.shape

ax[1].errorbar(red,gamma,yerr=gammaerr, fmt='ko', ecolor='k')
ax[1].errorbar(red,gammab,yerr=gammaerrb, fmt='ko', ecolor='k')


#lx=np.array([0, .5, 1], dtype='f')
#print lx*.146-.09

#line, = ax[1].plot(lx,lx*.146-.094, lw=2)


chiz,chia,chih = np.loadtxt('childress.dat', usecols=(0,1,2), unpack=True, dtype='string')
chiz=chiz.astype(float)
chia=chia.astype(float)
chih=chih.astype(float)
line, = ax[1].plot(chiz,-chih, lw=3, color='orange',label='Childress Curve')

ax[1].text(0.31,0.08,'Childress 14',fontdict={'fontsize':10},color='orange',rotation=-5)

from scipy.interpolate import interp1d
ff=interp1d(chiz,chih)



ax[1].set_xlim(0,1)
ax[1].set_ylim(-.15,.15)
ax[1].set_ylabel('Hubble step (mag)')
ax[1].set_xlabel('z')
print bin_means

chip1=[]
chip2=[]

for x2 in range(0,10):
    x=x2/10.0
    xx1=np.where((z1>bins[x2]) & (z1<bins[x2+1]) & (mass>10.0))
    xx2=np.where((z1>bins[x2]) & (z1<bins[x2+1]) & (mass<10.0))
    #ax[1].bar(x+.04, len(xx1[0])/2000.0, width=.03, color='g', alpha=.45)
    #ax[1].bar(x+.07, len(xx2[0])/2000.0, width=.03, color='r', alpha=.45)
    rect=plt.Rectangle((x+.04, -.15), .015*(1+bins[x2]), len(xx1[0])/1600.0, facecolor='blue', edgecolor='black',alpha=.75)
    ax[1].add_patch(rect)
    rect2=plt.Rectangle((x+.06, -.15), .015*(1+bins[x2]), len(xx2[0])/1600.0, facecolor='red', edgecolor='black', alpha=.75)
    ax[1].add_patch(rect2)

    print float(len(xx1[0]))/float(len(xx1[0])+len(xx2[0]))
    chip1=np.append(chip1,np.median(np.append(z1[xx1[0]],z1[xx2[0]])))
    chip2=np.append(chip2,0.6*ff(np.median(np.append(z1[xx1[0]],z1[xx2[0]])))/float(len(xx1[0]))*float(len(xx1[0])+len(xx2[0])))
#line, = ax[1].plot(chip1,chip2, lw=3, color='purple')

#legend = ax[1].legend(loc='upper right', shadow=True,fontsize=8,frameon = False,labelspacing=0.01)

plt.tight_layout()
plt.show()
plt.savefig('mass_global.png')

