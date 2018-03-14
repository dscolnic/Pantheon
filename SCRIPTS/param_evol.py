import numpy as np
import matplotlib.pyplot as plt
import array
import math
from astropy.cosmology import FlatLambdaCDM
import matplotlib
import wmom
import string
from numpy.polynomial import polynomial as P
from scipy.interpolate import interp1d
from scipy.optimize import curve_fit
import matplotlib
import plotsetup
import matplotlib.ticker as ticker
from scipy.stats import pearsonr
from matplotlib import gridspec
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
            if ((('g10.fitres' in file1)|('g12.fitres' in file1)) and (variable=='beta0')):
                  x[3]=str(float(x[3])-0.06)
            if ((('g10.fitres' in file1)|('g12.fitres' in file1)) and (variable=='beta1')):
                  x[3]=str(float(x[3])+.35)
            if ((('c10.fitres' in file1)|('c12.fitres' in file1)) and (variable=='beta0')):
                x[3]=str(float(x[3])-0.15)
            if ((('c10.fitres' in file1)|('c12.fitres' in file1)) and (variable=='beta1')):
                x[3]=str(float(x[3])+.7)
            return ([x[3],x[5]])
def prec(x):
      return '('+"%.3f"%float(x[0])+'\pm'+"%.3f"%float(x[1])+')'

      
beta=[]
alpha=[]
gamma=[]
intscat=[]

betaerr=[]
alphaerr=[]
gammaerr=[]
intscaterr=[]
red=[]
red2=[0.010,0.060,0.115,0.177,0.247,0.328,0.420,0.528,0.656,.810]
red2=[0.01,
      0.037,
      0.067,
      0.103,
      0.145,
      0.198,
      0.265,
      .356,
      0.494,
      0.753,
      2.2]
alphanum=0.14
betanum=3.1
gammanum=0.04
intscatnum=0.1

alphanum=float(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg0.fitres','alpha0',3)[0])
betanum=float(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg0.fitres','beta0',3)[0])
gammanum=float(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg0.fitres','gamma0',3)[0])
intscatnum=float(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg0.fitres','iterat',3)[0])

alphanum0=float(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg11.fitres','alpha0',3)[0])
betanum0=float(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg11.fitres','beta0',3)[0])
gammanum0=float(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg11.fitres','gamma0',3)[0])

alphanum1=float(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg10.fitres','alpha0',3)[0])
betanum1=float(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg10.fitres','beta0',3)[0])
gammanum1=float(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg10.fitres','gamma0',3)[0])


alphanum2=float(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg9.fitres','alpha0',3)[0])
betanum2=float(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg9.fitres','beta0',3)[0])
gammanum2=float(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg9.fitres','gamma0',3)[0])

alphanumz=float(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg11.fitres','alpha1',3)[0])
betanumz=float(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg10.fitres','beta1',3)[0])
gammanumz=float(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg9.fitres','gamma1',3)[0])

alphanumxa=float(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg12.fitres','alpha0',3)[0])
betanumxa=float(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg12.fitres','beta0',3)[0])
gammanumxa=float(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg12.fitres','gamma0',3)[0])


alphanumxb=float(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg12.fitres','alpha1',3)[0])
betanumxb=float(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg12.fitres','beta1',3)[0])
gammanumxb=float(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg12.fitres','gamma1',3)[0])


#betanum
#betanumz+betanum1
print betanum, betanumz,betanum2


v1=open('vari_evol.tex','w')

v1.write('\\newcommand{\\alphanumn}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg0.fitres','alpha0',3))+'}}\n')
v1.write('\\newcommand{\\betanumn}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg0.fitres','beta0',3))+'}}\n')
v1.write('\\newcommand{\\gammanumn}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg0.fitres','gamma0',3))+'}}\n')

v1.write('\\newcommand{\\alphanuma}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg11.fitres','alpha0',3))+'}}\n')
v1.write('\\newcommand{\\betanuma}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg11.fitres','beta0',3))+'}}\n')
v1.write('\\newcommand{\\gammanuma}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg11.fitres','gamma0',3))+'}}\n')
v1.write('\\newcommand{\\alphanumza}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg11.fitres','alpha1',3))+'}}\n')

v1.write('\\newcommand{\\alphanumb}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg10.fitres','alpha0',3))+'}}\n')
v1.write('\\newcommand{\\betanumb}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg10.fitres','beta0',3))+'}}\n')
v1.write('\\newcommand{\\gammanumb}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg10.fitres','gamma0',3))+'}}\n')
v1.write('\\newcommand{\\betanumzb}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg10.fitres','beta1',3))+'}}\n')

v1.write('\\newcommand{\\alphanumc}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg9.fitres','alpha0',3))+'}}\n')
v1.write('\\newcommand{\\betanumc}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg9.fitres','beta0',3))+'}}\n')
v1.write('\\newcommand{\\gammanumc}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg9.fitres','gamma0',3))+'}}\n')
v1.write('\\newcommand{\\gammanumzc}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg9.fitres','gamma1',3))+'}}\n')

v1.write('\\newcommand{\\alphanumd}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg12.fitres','alpha0',3))+'}}\n')
v1.write('\\newcommand{\\betanumd}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg12.fitres','beta0',3))+'}}\n')
v1.write('\\newcommand{\\gammanumd}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg12.fitres','gamma0',3))+'}}\n')

v1.write('\\newcommand{\\alphanumzd}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg12.fitres','alpha1',3))+'}}\n')
v1.write('\\newcommand{\\betanumzd}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg12.fitres','beta1',3))+'}}\n')
v1.write('\\newcommand{\\gammanumzd}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg12.fitres','gamma1',3))+'}}\n')

v1.write('\\newcommand{\\nalphanumd}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptn12.fitres','alpha0',3))+'}}\n')
v1.write('\\newcommand{\\nbetanumd}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptn12.fitres','beta0',3))+'}}\n')
v1.write('\\newcommand{\\ngammanumd}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptn12.fitres','gamma0',3))+'}}\n')

v1.write('\\newcommand{\\nalphanumzd}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptn12.fitres','alpha1',3))+'}}\n')
v1.write('\\newcommand{\\nbetanumzd}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptn12.fitres','beta1',3))+'}}\n')
v1.write('\\newcommand{\\ngammanumzd}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptn12.fitres','gamma1',3))+'}}\n')



v1.close()

v1=open('param_evol.table','w')
v1.write('Nominal & \\alphanumn  & \\betanumn  & \\gammanumn '+r'\\'+'\n')
v1.write(r'$\alpha$ evol. & $\alphanuma + \alphanumza \times z$ & \betanuma & \gammanuma '+r'\\'+'\n')
v1.write(r'$\beta$ evol. & \alphanumb & $\betanumb + \betanumzb \times z$ & \gammanumb '+r'\\'+'\n')
v1.write(r'$\gamma$ evol. & \alphanumc & \betanumc & $\gammanumc + \gammanumzc \times z$ '+r'\\'+'\n')
v1.write(r'$\alpha,\beta,\gamma$ evol. & $\alphanumd + \alphanumzd \times z$ & $\betanumd + \betanumzd \times z$ &  $\gammanumd + \gammanumzd \times z$  '+r'\\'+'\n')
v1.close()



temp=grabfitres('../DATA/SALT2mu/SALT2mu_fitoptg10.fitres','beta0',3)

rede1=[]
rede2=[]
for num in range(0,len(red2)-1):
    red=np.append(red,(red2[num]+red2[num+1])/2.0)
    rede1=np.append(rede1,np.absolute((red2[num]+red2[num+1])/2.0-red2[num]))
    rede2=np.append(rede2,np.absolute((red2[num]+red2[num+1])/2.0-red2[num+1]))
#xerr=[rede1,rede2]
print len(rede1)
print rede1
print rede2
print red
#stop
num=linef.linef('../DATA/SALT2mu/SALT2mu_fitoptg0bin.M0DIF','VARNAME')
z1,mures, murese = np.loadtxt('../DATA/SALT2mu/SALT2mu_fitoptg0bin.M0DIF', usecols=(4,5,6), unpack=True, dtype='string', skiprows=num+1)

z1=z1.astype(float)
mures=mures.astype(float)
murese=murese.astype(float)
muresebin=murese
print z1, red
#stop
red=z1

for x in range(0,10):
    temp=grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgb'+str(x)+'.fitres','beta0',3)                       
    print float(temp[0])
    beta=np.append(beta,float(temp[0]))
    betaerr=np.append(betaerr,float(temp[1]))

    temp=grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgb'+str(x)+'.fitres','alpha0',3)
    alpha=np.append(alpha,float(temp[0]))
    alphaerr=np.append(alphaerr,float(temp[1]))
         
    print '../DATA/SALT2mu/SALT2mu_fitoptgb'+str(x)+'.fitres'
    temp=grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgb'+str(x)+'.fitres','gamma0',3)
    gamma=np.append(gamma,float(temp[0]))
    gammaerr=np.append(gammaerr,float(temp[1]))
     
    temp=grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgb'+str(x)+'.fitres','iteration',3)
    intscat=np.append(intscat,float(temp[0]))
    intscaterr=np.append(intscaterr,0)


print len(alpha)
#stop
#fig, ax = plt.subplots(3,1,sharex=True)
#print len(alpha),len(red)
xn=np.arange(0,15,.1)+.01
gs1 = gridspec.GridSpec(4, 1)
gs1.update(hspace=0.04,bottom=0.13,top=0.92)
ax4= plt.subplot(gs1[3])
ax3= plt.subplot(gs1[2])
ax2= plt.subplot(gs1[1])
ax1= plt.subplot(gs1[0])
ax=[ax1,ax2,ax3,ax4]
print alpha.shape, alphaerr.shape, red.shape
#stop
print red
print alpha
rede1=rede1*0
rede2=rede2*0
print red
#stop
ax[0].errorbar(red, alpha, xerr=[rede1,rede2],yerr=alphaerr, fmt='go', ecolor='g', alpha=.75)
print 'pearson alpha',pearsonr(red,alpha)

ax[0].set_xlim(0.01,1.3)
ax[0].set_ylim(0.08,0.22)
ax[0].set_ylabel(r'$\alpha$')
line, = ax[0].plot(xn,xn*0+alphanum, lw=2,color='black')
line, = ax[0].plot(xn,alphanum0+xn*alphanumz, lw=2)

ax[1].errorbar(red, beta-(.06-.3*red), xerr=[rede1,rede2],yerr=betaerr, fmt='go', ecolor='g', alpha=.75)
print red
print beta

ax[1].set_xlim(0.01,1.3)
ax[1].set_ylim(1.4,3.9)
ax[1].set_ylabel(r'$\beta$')
line, = ax[1].plot(xn,xn*0+betanum, lw=2,color='black')
line, = ax[1].plot(xn,betanum1+xn*betanumz-(.06-.3*xn)*0, lw=2)
print betanum1, betanumz
#stop
print 'pearson beta', pearsonr(red,beta)
print betanum1, betanumz
#y8ip
#stop
#ax[2].errorbar(red, gamma, gammaerr, fmt='go', ecolor='g', alpha=.75)
#ax[2].set_xlim(0,.8)
#ax[2].set_ylim(-0.12,0.12)
#ax[2].set_ylabel('HR Mass Step')
#line, = ax[2].plot(np.arange(0,15),np.arange(0,15)*0+gammanum, lw=2,color='black')
#line, = ax[2].plot(np.arange(0,15),np.arange(0,15)*gammanumz+gammanum2, lw=2)


ax[2].errorbar(red, intscat, xerr=[rede1,rede2],yerr=intscaterr, fmt='go', ecolor='g', alpha=.75)
ax[2].set_xlim(0.01,1.3)
ax[2].set_ylim(0.05,0.17)
ax[2].set_ylabel(r'$\sigma_{int}$')
ax[2].set_xlabel(r'$z$')

line, = ax[2].plot(np.arange(0,15),np.arange(0,15)*0+intscatnum, lw=2,color='black')

ax[0].yaxis.set_major_locator(ticker.MultipleLocator(0.04))
ax[1].yaxis.set_major_locator(ticker.MultipleLocator(0.4))
ax[2].yaxis.set_major_locator(ticker.MultipleLocator(0.03))
ax[3].yaxis.set_major_locator(ticker.MultipleLocator(0.03))

ax[0].text(0.62,0.105,r"$\alpha$ evol.",color='blue',rotation=0)
ax[0].text(0.02,.13,"No evol.", color='black')
ax[1].text(0.4,2.3,r"$\beta$ evol.",color='blue',rotation=-9)
ax[0].set_xticklabels(['','','','','','','',''])
ax[1].set_xticklabels(['','','','','','','',''])
ax[2].set_xticklabels(['','','','','','','',''])
num=linef.linef('../DATA/SALT2mu/SALT2mu_fitoptg0bin.M0DIF','VARNAME')
#SALT2mu/SALT2mu_fitoptg0bin
#SALT2mu/SALT2mu_fitoptc0bin

z1,mures, murese = np.loadtxt('../DATA/SALT2mu/SALT2mu_fitoptg0bin.M0DIF', usecols=(4,5,6), unpack=True, dtype='string', skiprows=num+1)
z1=z1.astype(float)
mures=mures.astype(float)
murese=murese.astype(float)

z2,mures2, murese2 = np.loadtxt('../DATA/SALT2mu/SALT2mu_fitoptc0bin.M0DIF', usecols=(4,5,6), unpack=True, dtype='string', skiprows=num+1)
z1=z1.astype(float)
mures2=mures2.astype(float)
murese2=murese2.astype(float)
mures=(mures+mures2)/2.0

print z1, mures, murese
#stop
print len(red), len(intscat), len(rede1)
ax[2].errorbar(red, intscat, xerr=[rede1,rede2],yerr=muresebin, fmt='go', ecolor='g', alpha=.75)

ax[3].errorbar(z1,mures,yerr=murese, fmt='go', ecolor='g', alpha=.75)
ax[3].set_xlim(0.01,1.3)
ax[3].set_ylim(-.07,0.07)
ax[3].set_ylabel(r'$\Delta \mu$ (mag)',labelpad=-0.4)
ax[3].set_xlabel(r'$z$')
line, = ax[3].plot(np.arange(0,15),np.arange(0,15)*0, lw=2,color='black')


ax1.set_xscale('log')
ax2.set_xscale('log')
ax3.set_xscale('log')
ax4.set_xscale('log')
ax1.axes.get_xaxis().set_visible(False)
ax2.axes.get_xaxis().set_visible(False)
ax3.axes.get_xaxis().set_visible(False)
ax[3].set_xticklabels(['','0.01','0.1','1.0'])

plt.show()
#plt.tight_layout()
plt.savefig('param_evol.png')

print 'Finished successfully'
