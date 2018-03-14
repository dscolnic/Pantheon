import os
import string
import numpy as np
import linef


filein='../DATA/SALT2mu/SALT2mu_fitoptg0.fitres'
name1='../DATA/SALT2mu/SALT2mu_fitoptg0.fitres'
header1=linef.linef(name1,'zCMB')


data1=np.genfromtxt(name1,skip_header=header1,names=True,comments='#')
cid1=np.genfromtxt(name1,skip_header=header1,usecols=(1),comments='#',dtype='str')[1:]
idsurvey1=data1['IDSURVEY'].astype(float)
zc = data1['zCMB'].astype(float)

def grabvarcos(file1):
    g=open(file1,'r')
    co=0
    for line in g:
        co=co+1
        x=string.split(line)
        #print 'vari', x[0]                                                                                                                                           
        if (co==2):
            #print 'vari', vari, x[0]                                                                                                                                 
            #if (vari == x[0]):
                #print "%.3f"%float(x[1])
                #g.close()
                return x
                #return ["%.3f"%float(x[1]),"%.3f"%float(x[2])]

def grabvar(file1, vari):
    g=open(file1,'r')
    co=0
    for line in g:
        co=co+1
        x=string.split(line)
        #print 'vari', x[0]
        if co>3:
            #print 'vari', vari, x[0]
            if (vari == x[0]):
                print "%.3f"%float(x[1])
                g.close()
                return ["%.3f"%float(x[1]),"%.3f"%float(x[2])]

def grabfitres(file1, survid,num):
    g=open(file1,'r')
    co=0
    coall=0
    for line in g:
      if 'SN:' in line:
          coall=coall+1
          x=string.split(line)
          if (survid==x[num]): 
              print survid, x[1]
              co=co+1
           
    return [co,coall]


#/project/rkessler/SN/SNDATA_ROOT/SIM/NewDan100f/NewDan100f.LIST
v2=open('vari_surv.table','w')
v1=open('vari_surv.tex','w')

#idsurvey1=data1['IDSURVEY'].astype(float)
#z1 = data1['zCMB'].astype(float)
#"{:.2f}".format(np.median(z1[idsurvey1==5)))

z1=grabfitres(filein,'5',3)
v2.write('CSP & '+repr(z1[0])+' & '+"{:.3f}".format(np.median(zc[idsurvey1==5]))+' \\\ \n')
v1.write('\\newcommand{\\numCSP}{\ensuremath{'+repr(z1[0])+'}}\n')
v1.write('\\newcommand{\\rumCSP}{\ensuremath{'+repr(45-z1[0])+'}}\n')

z1=grabfitres(filein,'63',3)
z2=grabfitres(filein,'64',3)

print z1
#stop
v2.write('CFA3 & '+repr(z1[0]+z2[0])+' & '+"{:.3f}".format(np.median(zc[(idsurvey1==63)|(idsurvey1==64)]))+' \\\ \n')
v1.write('\\newcommand{\\numCFAt}{\ensuremath{'+repr(z1[0]+z2[0])+'}}\n')
v1.write('\\newcommand{\\rumCFAt}{\ensuremath{'+repr(85-(z1[0]+z2[0]))+'}}\n')

z1=grabfitres(filein,'65',3)
z2=grabfitres(filein,'66',3)

v2.write('CFA4 & '+repr(z1[0]+z2[0])+' & '+"{:.3f}".format(np.median(zc[(idsurvey1==65)|(idsurvey1==66)]))+' \\\ \n')
v1.write('\\newcommand{\\numCFAf}{\ensuremath{'+repr(z1[0]+z2[0])+'}}\n')
v1.write('\\newcommand{\\rumCFAf}{\ensuremath{'+repr(43-(z1[0]+z2[0]))+'}}\n')

z1=grabfitres(filein,'61',3)
v2.write('CFA1 & '+repr(z1[0])+' & '+"{:.3f}".format(np.median(zc[idsurvey1==61]))+' \\\ \n')
v1.write('\\newcommand{\\numCFAo}{\ensuremath{'+repr(z1[0])+'}}\n')
v1.write('\\newcommand{\\rumCFAo}{\ensuremath{'+repr(5-z1[0])+'}}\n')

z1=grabfitres(filein,'62',3)
v2.write('CFA2 & '+repr(z1[0])+' & '+"{:.3f}".format(np.median(zc[idsurvey1==62]))+' \\\ \n')
v1.write('\\newcommand{\\numCFAw}{\ensuremath{'+repr(z1[0])+'}}\n')
v1.write('\\newcommand{\\rumCFAw}{\ensuremath{'+repr(19-z1[0])+'}}\n')


z1=grabfitres(filein,'1',3)
v2.write('SDSS & '+repr(z1[0])+' & '+"{:.3f}".format(np.median(zc[idsurvey1==1]))+' \\\ \n')
v1.write('\\newcommand{\\numSDSS}{\ensuremath{'+repr(z1[0])+'}}\n')

z1=grabfitres(filein,'15',3)
v2.write('PS1 & '+repr(z1[0])+' & '+"{:.3f}".format(np.median(zc[idsurvey1==15]))+' \\\ \n')
v1.write('\\newcommand{\\numPS}{\ensuremath{'+repr(z1[0])+'}}\n')


z1=grabfitres(filein,'4',3)
v2.write('SNLS & '+repr(z1[0])+' & '+"{:.3f}".format(np.median(zc[idsurvey1==4]))+' \\\ \n')
v1.write('\\newcommand{\\numSNLS}{\ensuremath{'+repr(z1[0])+'}}\n')


z1=grabfitres(filein,'101',3)
v2.write('SCP & '+repr(z1[0])+' & '+"{:.3f}".format(np.median(zc[idsurvey1==101]))+' \\\ \n')
v1.write('\\newcommand{\\numSCP}{\ensuremath{'+repr(z1[0])+'}}\n')

z1=grabfitres(filein,'100',3)
v2.write('GOODS & '+repr(z1[0])+' & '+"{:.3f}".format(np.median(zc[idsurvey1==100]))+' \\\ \n')
v1.write('\\newcommand{\\numGOOD}{\ensuremath{'+repr(z1[0])+'}}\n')

z1=grabfitres(filein,'106',3)
#v2.write('CANDELS & '+repr(z1[0])+' & '+"{:.3f}".format(np.median(zc[idsurvey1==106]))+' \\\ \n')
v2.write('CANDELS & 6& 1.732 \\\ \n')
v2.write('CLASH & 2& 1.555 \\\ \n')


v1.write('\\newcommand{\\numCAN}{\ensuremath{'+repr(z1[0])+'}}\n')


v2.write('\hline  \n')


z1=grabfitres(filein,'50',3)
v2.write('Tot & '+repr(z1[1])+' &  \n')
v1.write('\\newcommand{\\numTOT}{\ensuremath{'+repr(z1[1])+' }}\n')

v1.close()
v2.close()


