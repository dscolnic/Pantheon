import os
import string
import numpy as np


def conv(num,ran2,pre='3'):
    #if ran2>0: ran=np.random.rand(1)+99
    if ran2>0: ran=0
    if ran2==0: ran=0
    return "%.3f"%(float(num)+ran)


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

survvar,wvar,wverr,omvar,omverr,chi2,ho1,ho2 = np.loadtxt('/project/rkessler/dscolnic/cosmomc_s16/cosmocomb.txt', usecols=(0,2,3,4,5,8,9,10), unpack=True, dtype='string')
#xx=(survvar==survs[0])
#w1=wvar[xx]
#w1e=wverr[xx]
#w1=w1[0][1:-2]
#w1e=w1e[0][1:-2]
#w1x = float(w1)
#w1ex = float(w1e)
survs=['CMB_OMW','CMB+BAO_OMW','CMB+HST_OMW','CMB+BAO+HST_OMW','SN+CMB_OMW','SN+CMB+BAO_OMW','SN+CMB+HST_OMW','SN+CMB+BAO+HST_OMW']
labels=['CMB','CMB+BAO','CMB+H0','CMB+BAO+H0','SN+CMB','SN+CMB+BAO','SN+CMB+H0','SN+CMB+BAO+H0']
labels2=['CMBx','CMBBAOx','CMBHSTx','CMBBAOHSTx','SNCMBx','SNCMBBAOx','SNCMBHSTx','SNCMBBAOHSTx']
v1=open('vari_cosmo.tex','w')
v2=open('vari_cosmo1.table','w')

for i in range(1,len(survs)):
                      ran=0
                      if (i>3): ran=1
                      xx=(survvar==survs[i])
                      w1=wvar[xx]
                      w1e=wverr[xx]
                      w1=conv(w1[0][1:-2],ran)
                      w1e=conv(w1e[0][1:-2],0)
                      om1=omvar[xx]
                      om1e=omverr[xx]
                      om1=conv(om1[0][1:-2],ran)
                      om1e=conv(om1e[0][1:-2],0)
                      ho=conv(ho1[xx][0][1:-2],ran)
                      hoe=conv(ho2[xx][0][1:-2],0)
                      chi=chi2[xx]
                      chi=chi[0][1:-2]
                      v2.write(labels[i]+' & $ '+w1+' \pm '+w1e+'$ & $ '+om1+' \pm '+om1e+' $&$ '+ho+'\pm'+hoe+'$'+r'\\'+'\n')
                      v1.write('\\newcommand{\\'+labels2[i]+'OM}{\ensuremath{'+om1+' \pm '+om1e+'}}\n')
                      v1.write('\\newcommand{\\'+labels2[i]+'W}{\ensuremath{'+w1+' \pm '+w1e+'}}\n')
                      v1.write('\\newcommand{\\'+labels2[i]+'H}{\ensuremath{'+ho+' \pm '+hoe+'}}\n')
                                            
                      print 'survs ', i,survs[i]
                      
v2.close()

survs=['CMB_WWA','CMB+BAO_WWA','CMB+HST_WWA','CMB+BAO+HST_WWA','SN+CMB_WWA','SN+CMB+BAO_WWA','SN+CMB+HST_WWA','SN+CMB+BAO+HST_WWA']
labels=['CMB','CMB+BAO','CMB+H0','CMB+BAO+H0','SN+CMB','SN+CMB+BAO','SN+CMB+H0','SN+CMB+BAO+H0']
labels2=['CMBw','CMBBAOw','CMBHSTw','CMBBAOHSTw','SNCMBw','SNCMBBAOw','SNCMBHSTw','SNCMBBAOHSTw']
v2=open('vari_cosmo2.table','w')
survvar,fom,wvar,wverr,omvar,omverr,wav,waev,chi2,ho1,ho2 = np.loadtxt('/project/rkessler/dscolnic/cosmomc_s16/cosmocomb.txt', usecols=(0,1,2,3,4,5,6,7,8,9,10), unpack=True, dtype='string')
print fom


for i in range(1,len(survs)):
    ran=0
    if (i>3): ran=1
                          
    xx=(survvar==survs[i])
    w1=wvar[xx]
    w1e=wverr[xx]
    w1=conv(w1[0][1:-2],ran)
    w1e=conv(w1e[0][1:-2],0)
    om1=omvar[xx]
    om1e=omverr[xx]
    om1=conv(om1[0][1:-2],ran)
    om1e=conv(om1e[0][1:-2],0)
    ho=conv(ho1[xx][0][1:-2],ran)
    hoe=conv(ho2[xx][0][1:-2],0)
    wa=conv(wav[xx][0][1:-2],ran)
    wae=conv(waev[xx][0][1:-2],0)
    chi=chi2[xx]
    chi=chi[0][1:-2]
    fom2="%.1f"%float((fom[xx][0][2:-2]))
    v2.write(labels[i]+' & $ '+w1+' \pm '+w1e+'$ & $ '+wa+' \pm '+wae+'$ & $ '+om1+' \pm '+om1e+' $&$ '+ho+'\pm'+hoe+'$& '+fom2+r'\\'+'\n')
    v1.write('\\newcommand{\\'+labels2[i]+'OM}{\ensuremath{'+om1+' \pm '+om1e+'}}\n')
    v1.write('\\newcommand{\\'+labels2[i]+'WO}{\ensuremath{'+w1+' \pm '+w1e+'}}\n')
    v1.write('\\newcommand{\\'+labels2[i]+'WA}{\ensuremath{'+wa+' \pm '+wae+'}}\n')    
    v1.write('\\newcommand{\\'+labels2[i]+'H}{\ensuremath{'+ho+' \pm '+hoe+'}}\n')
    
    print 'survs ', i,survs[i]
    
v2=open('vari_cosmo3.table','w')
#'SN_OMOL'
#,'DS17_ALL_omolflat_alone'
#SN+CMB+BAO+HST_OMOL
#'SN+CMB+BAO+H0'
#'SNCMBBAOHOo'
survs=['CMB_OMOL','CMB+BAO_OMOL','CMB+HST_OMOL','CMB+BAO+HST_OMOL','SN+CMB_OMOL','SN+CMB+BAO_OMOL','SN+CMB+HST_OMOL','SN+CMB+BAO+HST_OMOL','SN_OMOL','SN_fOMOL']
labels=['CMB','CMB+BAO','CMB+H0','CMB+BAO+H0','SN+CMB','SN+CMB+BAO','SN+CMB+H0','SN+CMB+BAO+H0','SN','SNo']
labels2=['CMBo','CMBBAOo','CMBHSTo','CMBBAOHSTo','SNCMBo','SNCMBBAOo','SNCMBHSTo','SNCMBBAOHSTo','SNo','SNl']
survvar,wvar,wverr,omvar,omverr,okvar, okverr,chi2,ho1,ho2 = np.loadtxt('/project/rkessler/dscolnic/cosmomc_s16/cosmocomb.txt', usecols=(0,2,3,4,5,6,7,8,9,10), unpack=True, dtype='string')

for i in range(1,len(survs)):
    ran=0
    if (i>3): ran=1
    xx=(survvar==survs[i])
    print 'survs', survs[i]
    w1=wvar[xx]
    w1e=wverr[xx]
    print 'su', survs[i]
    print 'ran', ran
    print 'w1', w1[0][1:-2]
    w1=conv(w1[0][1:-2],ran)
    w1e=conv(w1e[0][1:-2],0)
    om1=omvar[xx]
    om1e=omverr[xx]
    om1=conv(om1[0][1:-2],ran)
    om1e=conv(om1e[0][1:-2],0)

    ok1=okvar[xx]
    ok1e=okverr[xx]
    ok1=conv(ok1[0][1:-2],ran)
    ok1e=conv(ok1e[0][1:-2],0)
    
    ho=conv(ho1[xx][0][1:-2],ran)
    hoe=conv(ho2[xx][0][1:-2],0)
    chi=chi2[xx]
    chi=chi[0][1:-2]
    if (i<(len(survs)-2)): v2.write(labels[i]+' & $ '+w1+' \pm '+w1e+'$ & $ '+om1+' \pm '+om1e+' $& $ '+ok1+' \pm '+ok1e+' $&$ '+ho+'\pm'+hoe+'$'+r'\\'+'\n')
    #v2.write(labels[i]+' & $ '+w1+' \pm '+w1e+'$ & $ '+om1+' \pm '+om1e+' $&$ '+ho+'\pm'+hoe+'$'+r'\\'+'\n')
        
    v1.write('\\newcommand{\\'+labels2[i]+'OM}{\ensuremath{'+w1+' \pm '+w1e+'}}\n')
    v1.write('\\newcommand{\\'+labels2[i]+'OL}{\ensuremath{'+om1+' \pm '+om1e+'}}\n')
    v1.write('\\newcommand{\\'+labels2[i]+'H}{\ensuremath{'+ho+' \pm '+hoe+'}}\n')
    
    print 'survs ', i,survs[i]
    
v2.close()
#v1.close()

#SN_OMW [0, '-1.1033772E+00', '2.2879675E-01', '3.1033556E-01', '7.7866698E-02', '0', '0', '4.9873528E+01', '6.0047647E+01', '2.2931633E+01']
#SN_nosys_OMW [0, '-1.2507382E+00', '1.4017495E-01', '3.4220746E-01', '3.3638822E-02', '0', '0', '5.8043857E+01', '6.1072085E+01', '2.3755246E+01']
#SN_fOMOL ['98436.7151039', '2.9017804E-01', '2.1580386E-02', '7.0982196E-01', '2.1580386E-02', '0', '0', '4.9005086E+01', '5.8427760E+01', '2.3357121E+01']
#SN_OMOL ['1.62327698938', '3.1403351E-01', '6.9956941E-02', '7.4549723E-01', '1.0813380E-01', '0', '0', '4.9738610E+01', '6.0541925E+01', '2.3065176E+01']
#SN_nosys_fOMOL ['1.62327698938', '2.7529504E-01', '1.1996702E-02', '7.2470496E-01', '1.1996702E-02', '0', '0', '6.0527141E+01', '5.9121086E+01', '2.3335293E+01']
#SN_nosys_OMOL ['1.59899940534', '3.4263813E-01', '3.9163485E-02', '8.4399583E-01', '6.8171058E-02', '0', '0', '5.8412446E+01', '5.7320525E+01', '2.3141130E+01']

v2=open('vari_cosmo4.table','w')
survs=['SN_nosys_fOMOL','SN_nosys_OMOL','SN_nosys_OMW','SN_fOMOL','SN_OMOL','SN_OMW']
labels=['SN-stat','SN-stat','SN-stat','SN','SN','SN']
labelsb=['\LCDM','\OCDM','\WCDM','\LCDM','\OCDM','\WCDM']

labels2=['SNts','SNtk','SNtw','SNs','SNk','SNw']
survvar,wvar,wverr,omvar,omverr,chi2,ho1,ho2 = np.loadtxt('/project/rkessler/dscolnic/cosmomc_s16/cosmocomb.txt', usecols=(0,2,3,4,5,8,9,10), unpack=True, dtype='string')

for i in range(0,len(survs)):
    print 'i', i
    if (i==4):
        print 'OMOL' in survs[i]
        #stop
    if ('OMW' in survs[i]):
         ran=0
         #if (i>3): ran=1
         xx=(survvar==survs[i])
         w1=wvar[xx]
         w1e=wverr[xx]
         w1=conv(w1[0][1:-2],ran)
         w1e=conv(w1e[0][1:-2],0)
         om1=omvar[xx]
         om1e=omverr[xx]
         om1=conv(om1[0][1:-2],ran)
         om1e=conv(om1e[0][1:-2],0)
         ho=conv(ho1[xx][0][1:-2],ran)
         hoe=conv(ho2[xx][0][1:-2],0)
         chi=chi2[xx]
         chi=chi[0][1:-2]
         v2.write(labels[i]+' & '+labelsb[i]+' & $ '+w1+' \pm '+w1e+'$ & $ '+om1+' \pm '+om1e+'$& '+r'\\'+'\n')
         v1.write('\\newcommand{\\'+labels2[i]+'OM}{\ensuremath{'+om1+' \pm '+om1e+'}}\n')
         v1.write('\\newcommand{\\'+labels2[i]+'W}{\ensuremath{'+w1+' \pm '+w1e+'}}\n')
         #v1.write('\\newcommand{\\'+labels2[i]+'H}{\ensuremath{'+ho+' \pm '+hoe+'}}\n')

    if ('OMOL' in survs[i]):
         
         ran=0
         #if (i>3): ran=1
         xx=(survvar==survs[i])
         print 'survs', survs[i]
         w1=wvar[xx]
         w1e=wverr[xx]
         print 'su', survs[i]
         print 'ran', ran
         print 'w1', w1[0][1:-2]
         w1=conv(w1[0][1:-2],ran)
         w1e=conv(w1e[0][1:-2],0)
         om1=omvar[xx]
         om1e=omverr[xx]
         om1=conv(om1[0][1:-2],ran)
         om1e=conv(om1e[0][1:-2],0)
         ho=conv(ho1[xx][0][1:-2],ran)
         hoe=conv(ho2[xx][0][1:-2],0)
         chi=chi2[xx]
         chi=chi[0][1:-2]
         v2.write(labels[i]+' & '+labelsb[i]+' && $ '+w1+' \pm '+w1e+'$ & $ '+om1+' \pm '+om1e+' $'+r'\\'+'\n')
         #v2.write(labels[i]+' & $ '+w1+' \pm '+w1e+'$ & $ '+om1+' \pm '+om1e+' $&$ '+ho+'\pm'+hoe+'$'+r'\\'+'\n')
        
         v1.write('\\newcommand{\\'+labels2[i]+'OM}{\ensuremath{'+w1+' \pm '+w1e+'}}\n')
         v1.write('\\newcommand{\\'+labels2[i]+'OL}{\ensuremath{'+om1+' \pm '+om1e+'}}\n')
         #v1.write('\\newcommand{\\'+labels2[i]+'H}{\ensuremath{'+ho+' \pm '+hoe+'}}\n')
         
    
    print 'survs ', i,survs[i]
    
v2.close()
v1.close()


survvar,wvar,wverr,omvar,omverr,chi2,ho1,ho2 = np.loadtxt('/project/rkessler/dscolnic/cosmomc_s16/survcomb.txt', usecols=(0,2,3,4,5,8,9,10), unpack=True, dtype='string')
#xx=(survvar==survs[0])
#w1=wvar[xx]
#w1e=wverr[xx]
#w1=w1[0][1:-2]
#w1e=w1e[0][1:-2]
#w1x = float(w1)
#w1ex = float(w1e)
survs=['DS17_MLOWZ','DS17_MSDSS','DS17_MPS1','DS17_MSNLS','DS17_MHST']
labels=['Remove SNLS','Remove SDSS','Remove PS1','Remove SNLS','Remove HST']
labels2=['CMBx','CMBBAOx','CMBHSTx','CMBBAOHSTx','SNCMBx','SNCMBBAOx','SNCMBHSTx','SNCMBBAOHSTx']
v2=open('vari_cosmo5.table','w')

for i in range(0,len(survs)):
    ran=0
    if (i>3): ran=1
    xx=(survvar==survs[i])
    w1=wvar[xx]
    w1e=wverr[xx]
    w1=conv(w1[0][1:-2],ran)
    w1e=conv(w1e[0][1:-2],0)
    om1=omvar[xx]
    om1e=omverr[xx]
    om1=conv(om1[0][1:-2],ran)
    om1e=conv(om1e[0][1:-2],0)
    ho=conv(ho1[xx][0][1:-2],ran)
    hoe=conv(ho2[xx][0][1:-2],0)
    chi=chi2[xx]
    chi=chi[0][1:-2]
    v2.write(labels[i]+' & $ '+w1+' \pm '+w1e+'$ & $ '+om1+' \pm '+om1e+' $&'+labels[i]+'&'+r'\\'+'\n')
    #v1.write('\\newcommand{\\'+labels2[i]+'OM}{\ensuremath{'+om1+' \pm '+om1e+'}}\n')
    #v1.write('\\newcommand{\\'+labels2[i]+'W}{\ensuremath{'+w1+' \pm '+w1e+'}}\n')
    #v1.write('\\newcommand{\\'+labels2[i]+'H}{\ensuremath{'+ho+' \pm '+hoe+'}}\n')
    
    print 'survs ', i,survs[i]
v2.close()
