import numpy as np
import string
import matplotlib.pyplot as plt
import matplotlib
import plotsetup
from matplotlib import gridspec
from scipy.stats import pearsonr
from pylab import polyfit
plotsetup.fullpaperfig()

#matplotlib.rcParams.update({'font.size': 14})
val1=[]
val2=[]
fil=[]
a=open('smp_comp.txt', 'r')
for line in a:
    x=string.split(line)
    val1=np.append(val1,x[0])
    val2=np.append(val2,x[1])
    fil=np.append(fil,x[2])

#list1, idsurvey,z1, mass1,x11,c1,sb,mu1, mu1e = np.loadtxt('PS1_Scolnic_test/NewDan101f/FITOPT000+SALT2mu.FITRES', usecols=(1,3, 6,10,17,19,31,34,35), unpack=True, dtype='string', skiprows=12)
list1,z1,sb,mass1,PKMJD,x11,c1 ,NDOF1 ,FITPROB,RA,DECL,TGAPMAX1 = np.loadtxt('../DATA/DS17_PS1_Scolnic2/PS1_Spec_DS17/FITOPT000.FITRES', usecols=(1,7,12,13,18,20,22,31,33,34,35,36), unpack=True, dtype='string', skiprows=16)
print mass1
print sb

sb=[]
listb, filb,massb,surf = np.loadtxt('sbb.txt', usecols=(0,1,2,3), unpack=True, dtype='string')
yy=np.where(massb=='nan')
massb[yy[0]]='25'
for i in range(0,len(list1)):
    yy=np.where((('PSc'+list1[i])==listb)&(filb=='r'))
    print 'len', list1[i], len(yy[0])
    if len(yy[0])>0: sb=np.append(sb,massb[yy[0]][0])
    if len(yy[0])==0: sb=np.append(sb,-9)
#mass=mass[xx[0]]                                                                                                                                                 
#print len(mass), len(z1)
#print 'mass', mass

val1,val1e,val2,val2e,mjd,nam,fil = np.loadtxt('smp_comp.txt', usecols=(0,1,2,3,4,5,6), unpack=True, dtype='string')
for i in range(0,len(fil)):
    nam[i]=nam[i].replace("PSc","")
#sys_ps1.py:list1, idsurvey1, z1,x11,c1,mb1,mu1, mu1e = np.loadtxt('PS1_Scolnic/NewDan101f/FITOPT000+SALT2mu.FITRES', usecols=(1, 2,6,17,19,21,36,37), unpack=True, dtype='string', skiprows=15)
print 'sb', sb

sbm=[]
massm=[]
for i in range(0,len(fil)):
  xx=np.where(nam[i]==(list1))
  #print 'xx', xx[0]
  temp=sb[xx[0]]
  jemp=mass1[xx[0]]
  print 'temp', temp
  print nam[i], len(xx[0])
  #print 'sb', sb[xx[0]], sbm[i]
  if len(xx[0])>0:
      sbm.append(temp[0])
      massm.append(jemp[0])
  if len(xx[0])==0:
      sbm.append('-9')
      massm.append('-9')
  #print 'sbm', sbm[i]
print 'sbm', sbm

mjd=mjd.astype(float)
val1=val1.astype(float)
val2=val2.astype(float)
xx=np.where(val1>6000.0)
#print val1[xx[0]]
#print nam[xx[0]]

val1e=val1e.astype(float)
val2e=val2e.astype(float)
#val2=(val2-val1)
weights=val2*0+1.0


xx=np.where(np.absolute(val2)>300)

y1=nam[xx[0]]
y2=fil[xx[0]]
#for i in range(0,len(y1)):
#    print y1[i], y2[i]

#stop
weights2=weights*0

bins = np.linspace(18,25,13)
sbm=np.array(sbm)
sbm=sbm.astype(float)
massm=np.array(massm)
massm=massm.astype(float)

for i in range(0,len(nam)):
    if (('50221' in nam[i])|('110460' in nam[i])|('80735' in nam[i])|(mjd[i]<(-20))|(mjd[i]>(60))): weights2[i]=1
#xx=np.where((weights2!=1)&(fil=='g'))
#xx=np.where((weights2!=1)&(val1/val1e>7)&(val2/val2e>7)&(fil=='z'))
xx=np.where((weights2!=1))  
xx2=np.where((weights2!=1))  
#print xx[0]
#stop
#xx=np.where(weights2!=1)
val2=val2[xx[0]]
val1=val1[xx[0]]

#val1=val1


weights=weights[xx[0]]
val1e=val1e[xx[0]]
val2e=val2e[xx[0]]
mjd=mjd[xx[0]]
sbm=sbm[xx[0]]
print 'sbm', np.median(sbm)
mjd=mjd.astype(float)
massm=massm[xx[0]]
mval1=27.5-2.5*np.log10(val1)
mval2=27.5-2.5*np.log10(val2)


plt.figure(1)
gs1 = gridspec.GridSpec(1, 2)
gs1.update(left=0.1, right=0.48,wspace=0,bottom=0.15,top=0.95)
ax1= plt.subplot(gs1[0])
ax2= plt.subplot(gs1[1])

gs2 = gridspec.GridSpec(1, 2)
gs2.update(left=0.60, right=0.98,wspace=0,bottom=0.15,top=0.95)
ax3= plt.subplot(gs2[0])
ax4= plt.subplot(gs2[1])

xx=np.where((sbm<21.5)&(sbm>0))
mval2=(val1[xx[0]]-val2[xx[0]])/val1e[xx[0]]-0.15

ax1.set_xlabel("SN "+r'$r_{PS1}$'+" mag")
ax1.set_ylabel('(SMP-DIFF)/(Unc.)')
ax1.set_ylim(-3.5,3.5)
ax1.set_xlim(18,24.9)
ax1.plot(mval1[xx[0]],mval2,'.r',alpha=0.25)
print 'sigma bias!!!', np.median((val1[xx[0]]-val2[xx[0]])/val1e[xx[0]]),  np.median((val1[xx[0]]-val2[xx[0]])), np.median((val1[xx[0]]-val2[xx[0]]-1.0)/val1e[xx[0]])


#ax[0,0].plot(mval1[xx[0]],(val1[xx[0]]-val2[xx[0]])/val1[xx[0]],'.r')

#val2=mval2[xx[0]]-mval1[xx[0]]
#mval2=(val1[xx[0]]-val2[xx[0]])/val1[xx[0]]

mval1x=mval1[xx[0]]
print 'mval1x', mval1x
bins = np.linspace(18,25,13)

digitized = np.digitize(mval1[xx[0]], bins)
bins = np.linspace(18,25,13)
print 'bins', bins

bin_means = [np.median(mval2[digitized == i]) for i in range(0, len(bins))]
bin_z = [np.median(mval1x[digitized == i]) for i in range(0, len(bins))]
bin_std = [np.std(mval2[digitized == i])/np.sqrt(len(mval2[digitized == i])) for i in range(0, len(bins))]
ax1.errorbar(bin_z, bin_means, yerr=bin_std, fmt='ko', ecolor='b', color='b',label='Binned Data')
ax1.legend(loc='upper left',prop={'size':10})
ax3.text(22,9,"High") 
ax3.text(22,6,"Surface")
ax3.text(22,3,"Brightness")

ax4.text(22,9,"Low")
ax4.text(22,6,"Surface")
ax4.text(22,3,"Brightness")


ax1.text(19.8,-2.3,"High")
ax1.text(19.8,-2.7,"Surface")
ax1.text(19.8,-3.1,"Brightness")

ax2.text(19.8,-2.3,"Low")
ax2.text(19.8,-2.7,"Surface")
ax2.text(19.8,-3.1,"Brightness")




xx=np.where(sbm>10)
xx=np.where((sbm>21.5)&(sbm>0))
mval2=(val1[xx[0]]-val2[xx[0]])/val1e[xx[0]]-0.15

print 'sxx', xx[0]
ax2.set_xlabel("SN "+r'$r_{PS1}$'+" mag")
#ax[0,1].set_ylabel('Delta Mag')
ax2.set_ylim(-3.5,3.5)
ax2.set_xlim(18,24.9)
ax2.plot(mval1[xx[0]],mval2,'.r',alpha=0.25)
print 'sigma bias!!!', np.median((val1[xx[0]]-val2[xx[0]])/val1e[xx[0]]), np.median((val1[xx[0]]-val2[xx[0]])), np.median((val1[xx[0]]-val2[xx[0]]-1.0)/val1e[xx[0]])

#ax[0,1].plot(mval1[xx[0]],(val1[xx[0]]-val2[xx[0]])/val1[xx[0]],'.r')

#val2=mval2[xx[0]]-mval1[xx[0]]
#mval2=(val1[xx[0]]-val2[xx[0]])/val1[xx[0]]


mval1x=mval1[xx[0]]
bins = np.linspace(18,25, 13)
digitized = np.digitize(mval1[xx[0]], bins)
bin_means = [np.median(mval2[digitized == i]) for i in range(0, len(bins))]
bin_z = [np.median(mval1x[digitized == i]) for i in range(0, len(bins))]
bin_std = [np.std(mval2[digitized == i])/np.sqrt(len(mval2[digitized == i])) for i in range(0, len(bins))]
ax2.errorbar(bin_z, bin_means, yerr=bin_std, fmt='ko', ecolor='b', color='b',label='D15 Sim')
line, = ax1.plot(range(1,59999), np.zeros(59998), lw=2,color='black')



xx=np.where((sbm<21.5)&(sbm>0))
ax3.set_xlabel('SMP Phot. Unc.')
ax3.set_ylabel('DIFF Phot. Unc.')
ax4.set_xlabel('SMP Phot. Unc.')

ax3.set_ylim(0,60)
ax3.set_xlim(0,59.5)
ax3.plot(val1e[xx[0]],val2e[xx[0]],'.r',alpha=0.25)
#zz3=(val1e[xx[0]]<40)

val2=val2e[xx[0]]
mval1x=val1e[xx[0]]
print 'mval1x', mval1x
bins = np.linspace(0,70,10)
digitized = np.digitize(val1e[xx[0]], bins)
bins = np.linspace(18,25,13)
print 'bins', bins
bin_means = [np.median(val2[digitized == i]) for i in range(0, len(bins))]
bin_z = [np.median(mval1x[digitized == i]) for i in range(0, len(bins))]
bin_std = [np.std(val2[digitized == i])/np.sqrt(len(val2[digitized == i])) for i in range(0, len(bins))]
ax3.errorbar(bin_z, bin_means, yerr=bin_std, fmt='ko', ecolor='b', color='b',label='D15 Sim')
#line, = ax3.plot(range(1,59999), np.zeros(59998), lw=2,color='black',linestyle='--')

print bin
#zz=np.isfinite(bin_z)
#print bin_z[zz],bin_means[zz]
print bin_z, bin_means

print 'pearson alpha',pearsonr(bin_z[1:6],bin_means[1:6])
from scipy.stats import linregress
m, b, r_value, p_value, std_err = linregress(bin_z[1:6],bin_means[1:6])
print m,b,r_value,p_value,std_err




pos=[]
for i in range(1,299):
    pos.append(i/100.0)


line, = ax3.plot(range(1,299), range(1,299), lw=2,color='black')
#line, = ax3.plot(np.arange(1,299,1)*.9, range(1,299), lw=2,color='black',linestyle='--')



xx=np.where((sbm>21.5))
#ax[1,1].set_xlabel('Mag')
#ax[1,1].set_ylabel('Delta Mag')
ax4.set_ylim(0,60)
ax4.set_xlim(0,59.5)
ax4.plot(val1e[xx[0]],val2e[xx[0]],'.r',alpha=0.25)

print 'pearson alpha',pearsonr(val1e[xx[0]],val2e[xx[0]])
m,b = polyfit(val1e[xx[0]],val2e[xx[0]], 1)
print m,b


val2=val2e[xx[0]]
mval1x=val1e[xx[0]]
print 'mval1x', mval1x
bins = np.linspace(0,70,10)
digitized = np.digitize(val1e[xx[0]], bins)
bins = np.linspace(18,25,13)
print 'bins', bins
bin_means = [np.median(val2[digitized == i]) for i in range(0, len(bins))]
bin_z = [np.median(mval1x[digitized == i]) for i in range(0, len(bins))]
bin_std = [np.std(val2[digitized == i])/np.sqrt(len(val2[digitized == i])) for i in range(0, len(bins))]
ax4.errorbar(bin_z, bin_means, yerr=bin_std, fmt='ko', ecolor='b', color='b',label='D15 Sim')
line, = ax4.plot(range(1,59999), range(1,59999), lw=2,color='black')
#line, = ax4.plot(np.arange(1,299)*.9, range(1,299), lw=2,color='black',linestyle='--')

line, = ax1.plot(range(1,59999), np.zeros(59998), lw=2,color='black')
line, = ax2.plot(range(1,59999), np.zeros(59998), lw=2,color='black')


pos=[]
for i in range(1,299):
    pos.append(i/100.0)


ax1.set_yticks([-3,-2,-1,0,1,2,3])
ax1.set_yticklabels(['-3','-2','-1','0','1','2','3'])
ax2.set_yticks([-3,-2,-1,0,1,2,3])
ax2.set_yticklabels(['','-','-','','','',''])


ax3.set_yticks([0,20,40,60])
ax3.set_yticklabels(['0','20','40','60'])
ax4.set_yticks([0,20,40,60])
ax4.set_yticklabels(['','','',''])
                        
#plt.tight_layout()
plt.show()
plt.savefig('smp_comp_flux.png')

stop

plt.figure(1)



val1,val1e,val2,val2e,mjd,nam,fil = np.loadtxt('smp_comp.txt', usecols=(0,1,2,3,4,5,6), unpack=True, dtype='string')
mjd=mjd.astype(float)
val1=val1.astype(float)
val2=val2.astype(float)
val1e=val1e.astype(float)
val2e=val2e.astype(float)
val1e=val1e*1.1
fig, ax = plt.subplots(2,1)
xx=np.where(np.absolute(mjd)>100)
rvec=np.random.randn(len(xx[0]))
n, bins, patches = ax[0].hist(rvec, bins=30,range=[-4,4], facecolor='r', alpha=0.25)
n, bins, patches = ax[0].hist((val1[xx[0]])/val1e[xx[0]], bins=30,range=[-4,4], facecolor='g', alpha=0.75)
ax[0].set_xlabel('Normalized Flux')
ax[0].set_ylabel('#')
ax[0].set_title('SMP '+str(1.48*np.median(np.absolute((val1[xx[0]])/val1e[xx[0]]))))
n, bins, patches = ax[1].hist(rvec, bins=30,range=[-4,4], facecolor='r', alpha=0.25)
n, bins, patches = ax[1].hist((val2[xx[0]])/val2e[xx[0]], bins=30,range=[-4,4], facecolor='r', alpha=0.75)
ax[1].set_xlabel('Normalized Flux')
ax[1].set_ylabel('#')
ax[1].set_title('Diff '+str(1.48*np.median(np.absolute((val2[xx[0]])/val2e[xx[0]]))))
print 1.48*np.median(np.absolute((val1[xx[0]])/val1e[xx[0]]))
print 1.48*np.median(np.absolute((val2[xx[0]])/val2e[xx[0]]))


plt.tight_layout()
plt.show()
plt.savefig('smp_comp_flux_hist.png')
