import os
import string
import numpy as np


v1=open('vari_canal.table','w')



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


labels=['None','No Bias Corr.','No Mass Corr.','No Supercal Corr.', 'No PV Corr.']

files1=['SALT2mu/SALT2mu_fitoptg0','SALT2mu/SALT2mu_fitoptn0',
 'SALT2mu/SALT2mu_fitoptg3',
'SALT2mu/SALT2mu_fitoptg13',
        'SALT2mu/SALT2mu_fitoptg14'
]
files2=['SALT2mu/SALT2mu_fitoptc0','SALT2mu/SALT2mu_fitoptn0',
        'SALT2mu/SALT2mu_fitoptc3',
        'SALT2mu/SALT2mu_fitoptc13',
        'SALT2mu/SALT2mu_fitoptc14']   

xx=[0,1,2,3,4,5,6]

basedir='../DATA/'
endext='.fitres.cospar'
x1=grabvarcos(basedir+files1[0]+endext)
x2=grabvarcos(basedir+files2[0]+endext)
nomw="%.3f"%((float(x1[0])+float(x2[0]))/2.0)
nomo="%.3f"%((float(x1[2])+float(x2[2]))/2.0)


#v1.write(labels[0]+' & $ \phantom{-} 0.000 \pm '+"%.3f"%float(x1[1])+'$ & $ \phantom{-}0.000 \pm '+"%.3f"%float(x1[3])+'$'+r'\\ '+'\n')
#v1.write('Fit Changes: & ~ & ~\\\ \n')         
for i in range(1,len(files1)):
    print i
    print xx[i]
    x1=grabvarcos(basedir+files1[xx[i]]+endext)
    x2=grabvarcos(basedir+files2[xx[i]]+endext)
    wvalb="%.3f"%((float(x1[0])+float(x2[0]))/2.0)
    ovalb="%.3f"%((float(x1[2])+float(x2[2]))/2.0)
    wval=float(wvalb)-float(nomw)
    oval2=float(ovalb)-float(nomo)
    wval2="%.3f"%float(wval)
    oval3="%.3f"%float(oval2)
    wval2e="%.3f"%float(x1[1])
    oval3e="%.3f"%float(x1[3])
    if '-' not in wval2: wval2='+'+wval2
    if '-' not in oval3: oval3='+'+oval3
        
    print wval2, oval3
    #v1.write(labels[xx[i]]+' & $ '+wval2+' \pm '+wval2e+'$ & $ '+oval3+' \pm '+oval3e+'$'+r'\\ '+'\n')
    v1.write(labels[xx[i]]+' & $ '+wval2+'$ & $ '+oval3+'$'+r'\\ '+'\n')
        
    if xx[i]==14: v1.write('Sample Changes: & ~ & ~\\\ \n')
             
v1.close()
