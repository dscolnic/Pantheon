import os
import string
import numpy as np
import linef

#list1, idsurvey, z1,pke,x11,x11e,c1,c1e,fitp,mu1, mu1e = np.loadtxt('../DATA/DS17_PS1_Scolnic2/NewDan101f_DS17/FITOPT000.FITRES', usecols=(1,3, 7,19,20,21,22,23,33,34,35), unpack=True, dtype='string', skiprows=12)



name1='../DATA/DS17_PS1_Scolnic2/PS1_Spec_DS17/FITOPT000.FITRES'
header1=linef.linef(name1,'zCMB')
data1=np.genfromtxt(name1,skip_header=header1,names=True,comments='#')
list1=np.genfromtxt(name1,skip_header=header1,usecols=(1),comments='#',dtype='str')[1:]
z1 = data1['zCMB'].astype(float)
SNRMAX11=data1['SNRMAX1'].astype(float)
x11 = data1['x1'].astype(float)
c1 = data1['c'].astype(float)
NDOF1=data1['NDOF'].astype(float)
TGAPMAX1=data1['TGAPMAX'].astype(float)
fitp=data1['FITPROB'].astype(float)
PKMJD1=data1['PKMJD'].astype(float)
RA1=data1['RA'].astype(float)
DEC1=data1['DECL'].astype(float)
idsurvey=data1['IDSURVEY'].astype(float)
NDOF1=data1['NDOF'].astype(float)
c1e=data1['cERR'].astype(float)
x11e=data1['x1ERR'].astype(float)
pke=data1['PKMJDERR'].astype(float)
TrestMAX=data1['TrestMAX'].astype(float)

name1='../DATA/SALT2mu/SALT2mu_fitoptgos_ps1.fitres'
header1=linef.linef(name1,'zCMB')
data1=np.genfromtxt(name1,skip_header=header1,names=True,comments='#')
list2=np.genfromtxt(name1,skip_header=header1,usecols=(1),comments='#',dtype='str')[1:]
z2 = data1['zCMB'].astype(float)
SNRMAX12=data1['SNRMAX1'].astype(float)
x12 = data1['x1'].astype(float)
c2 = data1['c'].astype(float)
NDOF2=data1['NDOF'].astype(float)
TGAPMAX2=data1['TGAPMAX'].astype(float)
fitp2=data1['FITPROB'].astype(float)
PKMJD2=data1['PKMJD'].astype(float)
RA2=data1['RA'].astype(float)
DEC2=data1['DECL'].astype(float)
idsurvey2=data1['IDSURVEY'].astype(float)
NDOF2=data1['NDOF'].astype(float)
c2e=data1['cERR'].astype(float)
x12e=data1['x1ERR'].astype(float)
pke2=data1['PKMJDERR'].astype(float)
mu2=data1['MU'].astype(float)
mu2e=data1['MUERR'].astype(float)
mupull2=data1['MUPULL'].astype(float)
TrestMAX2=data1['TrestMAX'].astype(float)

name1='../DATA/SALT2mu/SALT2mu_fitoptgs_ps1.fitres'
header1=linef.linef(name1,'zCMB')
data1=np.genfromtxt(name1,skip_header=header1,names=True,comments='#')
list3=np.genfromtxt(name1,skip_header=header1,usecols=(1),comments='#',dtype='str')[1:]
z3 = data1['zCMB'].astype(float)
SNRMAX13=data1['SNRMAX1'].astype(float)
x13 = data1['x1'].astype(float)
c3 = data1['c'].astype(float)
NDOF3=data1['NDOF'].astype(float)
TGAPMAX3=data1['TGAPMAX'].astype(float)
fitp3=data1['FITPROB'].astype(float)
PKMJD3=data1['PKMJD'].astype(float)
RA3=data1['RA'].astype(float)
DEC3=data1['DECL'].astype(float)
idsurvey3=data1['IDSURVEY'].astype(float)
NDOF3=data1['NDOF'].astype(float)
c3e=data1['cERR'].astype(float)
x13e=data1['x1ERR'].astype(float)
pke3=data1['PKMJDERR'].astype(float)
mu3=data1['MU'].astype(float)
mu3e=data1['MUERR'].astype(float)
mupull3=data1['MUPULL'].astype(float)
TrestMAX3=data1['TrestMAX'].astype(float)

xxz=np.where((np.absolute(x11e)<1000))
print len(xxz[0])
#stop
xxa=np.where((np.absolute(x11e)<1))
print 'x11e<1',len(xxa[0])
xxb=np.where(np.absolute(x11e)<1 & (np.absolute(pke)<2))
print 'pke<2',len(xxb[0])
xxc=np.where( (np.absolute(c1)<.3) &  (np.absolute(x11e)<1) & (np.absolute(pke)<2))
print 'c<.3',len(xxc[0])
xxd=np.where((np.absolute(c1)<.3) & (np.absolute(x11)<3) & (np.absolute(x11e)<1) & (np.absolute(pke)<2))
print 'x1<3',len(xxd[0])

xx=np.where((np.absolute(c1)<.3) & (np.absolute(x11)<3) & (np.absolute(x11e)<1) & (np.absolute(pke)<2))
xx1=np.where((np.absolute(c1)<.3) & (np.absolute(x11)<3) & (np.absolute(x11e)<1) & (np.absolute(pke)<2)  & (np.absolute(fitp)<0.001))
xxe=np.where((np.absolute(c1)<.3) & (np.absolute(x11)<3) & (np.absolute(x11e)<1) & (np.absolute(pke)<2)  & (np.absolute(fitp)>0.001))
xxf=np.where((np.absolute(c1)<.3) & (np.absolute(x11)<3) & (np.absolute(x11e)<1) & (np.absolute(pke)<2)  & (np.absolute(fitp)>0.001))
xxg=np.where((np.absolute(c1)<.3) & (np.absolute(x11)<3) & (np.absolute(x11e)<1) & (np.absolute(pke)<2)  & (np.absolute(fitp)>0.001)&(TrestMAX>5))

print len(list1)
print len(list2)
print list1[xxe]
for x in list1[xxe]:
    #print x
    if (x not in list2): print 'oh', x
    
#print 'fitprob','fitp<0.001',len(xx2[0])
#stop   
list2, idsurvey, z1,pk,pk2e,x11,x12e,c1,c1e,mu1, mu1e = np.loadtxt('../DATA/DS17_PS1_Scolnic2/PS1_Spec_DS17/FITOPT000.FITRES', usecols=(1,3, 6,15,16,17,18,19,20,34,35), unpack=True,

 dtype='string', skiprows=12)
print len(list1), len(list2)
for i in range(0,len(list1)):
    xx=np.where(list1[i] == list2)
    #if not xx[0]: print 'o',list1[i],x11[i],x11e[i], c1[i], c1e[i], pk[i],pke[i]

print len(list1), len(list2)
for i in range(0,len(list1)):
    xx=np.where(list1[i] == list2)
    if ((float(x11e[i])>1) | (float(pke[i])>2)): print list1[i], x11e[i], pke[i]

#stop
v1=open('vari_ps1c.tex','w')


v1.write('\\newcommand{\\ruta}{\ensuremath{'+repr(365)+'}}\n')
v1.write('\\newcommand{\\rutxa}{\ensuremath{'+repr(len(xxz[0])-3)+'}}\n')
v1.write('\\newcommand{\\rutxb}{\ensuremath{'+repr(len(xxa[0])-3)+'}}\n')
v1.write('\\newcommand{\\rutxc}{\ensuremath{'+repr(len(xxb[0])-3)+'}}\n')
v1.write('\\newcommand{\\rutxd}{\ensuremath{'+repr(len(xxc[0])-3)+'}}\n')
v1.write('\\newcommand{\\rutxe}{\ensuremath{'+repr(len(xxd[0])-3)+'}}\n')
v1.write('\\newcommand{\\rutxf}{\ensuremath{'+repr(len(xxe[0])-3)+'}}\n')
v1.write('\\newcommand{\\rutxg}{\ensuremath{'+repr(len(xxg[0])-3)+'}}\n')

v1.write('\\newcommand{\\rutya}{\ensuremath{'+repr(368-len(xxz[0]))+'}}\n')
v1.write('\\newcommand{\\rutyb}{\ensuremath{'+repr(len(xxz[0])-len(xxa[0]))+'}}\n')
v1.write('\\newcommand{\\rutyc}{\ensuremath{'+repr(len(xxa[0])-len(xxb[0]))+'}}\n')
v1.write('\\newcommand{\\rutyd}{\ensuremath{'+repr(len(xxb[0])-len(xxc[0]))+'}}\n')
v1.write('\\newcommand{\\rutye}{\ensuremath{'+repr(len(xxc[0])-len(xxd[0]))+'}}\n')
v1.write('\\newcommand{\\rutyf}{\ensuremath{'+repr(len(xxd[0])-len(xxe[0]))+'}}\n')
v1.write('\\newcommand{\\rutyg}{\ensuremath{'+repr(len(xxe[0])-len(xxg[0]))+'}}\n')
v1.write('\\newcommand{\\allPS}{\ensuremath{'+repr(365)+'}}\n')

v1.close()
