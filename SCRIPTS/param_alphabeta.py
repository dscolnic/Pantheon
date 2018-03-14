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
import linef
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
      return ''+"%.3f"%float(x[0])+'\pm'+"%.3f"%float(x[1])+''

def precb(x):
            return ''+"%.2f"%float(x[0])+'\pm'+"%.2f"%float(x[1])+''
      

def grabfitres2(file1, variable, num):
          g=open(file1,'r')
          co=0
          coall=0
          for line in g:
                if variable in line:
                      x=string.split(line)
                      return [(x[3])]

def prec2(x):
      return ''+"%.3f"%float(x[0])+''

def prec3b(x):
          return ''+"%.3f"%float(x)
    
def prec2b(x):
            return ''+"%.2f"%float(x[0])+''
      
def prec3(x):
            print 'prec3', x
            return ''+"%.2f"%float(x)
      
def disp(fitres,idsurv,cut=3):
  headn=linef.linef(fitres,'zCMB')    
  #ids,mures = np.loadtxt(fitres, usecols=(3,41), unpack=True, dtype='string', skiprows=45)
  data1=np.genfromtxt(fitres,skip_header=headn,names=True,comments='#')
  zCMB=data1['zCMB'].astype(float)
  MU=data1['MU'].astype(float)
  MU_MODEL=data1['MUMODEL'].astype(float)
  mures=MU-MU_MODEL  
  mures=mures.astype(float)
  #print mures
  
  #if ((idsurv=='15')|(idsurv=='1')|(idsurv=='4')):
  #      xx=(ids==idsurv)
  #if ((idsurv!='15')&(idsurv!='1')&(idsurv!='4')):
  #      xx=((ids!='15')&(ids!='1')&(ids!='4'))
  if (idsurv==99):
        xx=(np.absolute(mures)>(-1000))
  #print xx
  #print mures[xx]
  mures=mures[zCMB<cut]
  #print idsurv, 1.48*np.median(np.absolute(mures[xx])), len(mures[xx])
  #return 1.48*np.median(np.absolute(mures[xx]))
  return np.sqrt(np.mean(np.square(mures)))
#print (disp('../DATA/SALT2mu/SALT2mu_fitoptgos_sdss.fitres',99))
#stop

v1=open('vari_alphabeta.tex','w')
#SALT2mu/SALT2mu_fitoptcs_global.fitres 
v1.write('\\newcommand{\\salphanumg}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgs_global.fitres','alpha0',3))+'}}\n')
v1.write('\\newcommand{\\sbetanumg}{\ensuremath{'+precb(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgs_global.fitres','beta0',3))+'}}\n')
v1.write('\\newcommand{\\sgammanumg}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgs_global.fitres','gamma0',3))+'}}\n')
v1.write('\\newcommand{\\sintnumg}{\ensuremath{'+prec2b(grabfitres2('../DATA/SALT2mu/SALT2mu_fitoptgs_global.fitres','iterat',3))+'}}\n')
v1.write('\\newcommand{\\sdispnumg}{\ensuremath{'+prec3(disp('../DATA/SALT2mu/SALT2mu_fitoptgs_global.fitres',99))+'}}\n')

v1.write('\\newcommand{\\salphanums}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgs_snls.fitres','alpha0',3))+'}}\n')
v1.write('\\newcommand{\\sbetanums}{\ensuremath{'+precb(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgs_snls.fitres','beta0',3))+'}}\n')
v1.write('\\newcommand{\\sgammanums}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgs_snls.fitres','gamma0',3))+'}}\n')
v1.write('\\newcommand{\\sintnums}{\ensuremath{'+prec2b(grabfitres2('../DATA/SALT2mu/SALT2mu_fitoptgs_snls.fitres','iterat',3))+'}}\n')
v1.write('\\newcommand{\\sdispnums}{\ensuremath{'+prec3(disp('../DATA/SALT2mu/SALT2mu_fitoptgs_snls.fitres',99))+'}}\n')

v1.write('\\newcommand{\\salphanumd}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgs_sdss.fitres','alpha0',3))+'}}\n')
v1.write('\\newcommand{\\sbetanumd}{\ensuremath{'+precb(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgs_sdss.fitres','beta0',3))+'}}\n')
v1.write('\\newcommand{\\sgammanumd}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgs_sdss.fitres','gamma0',3))+'}}\n')
v1.write('\\newcommand{\\sintnumd}{\ensuremath{'+prec2b(grabfitres2('../DATA/SALT2mu/SALT2mu_fitoptgs_sdss.fitres','iterat',3))+'}}\n')
v1.write('\\newcommand{\\sdispnumd}{\ensuremath{'+prec3(disp('../DATA/SALT2mu/SALT2mu_fitoptgs_sdss.fitres',99))+'}}\n')

v1.write('\\newcommand{\\salphanuml}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgs_lowz.fitres','alpha0',3))+'}}\n')
v1.write('\\newcommand{\\sbetanuml}{\ensuremath{'+precb(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgs_lowz.fitres','beta0',3))+'}}\n')
v1.write('\\newcommand{\\sgammanuml}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgs_lowz.fitres','gamma0',3))+'}}\n')
v1.write('\\newcommand{\\sintnuml}{\ensuremath{'+prec2b(grabfitres2('../DATA/SALT2mu/SALT2mu_fitoptgs_lowz.fitres','iterat',3))+'}}\n')
v1.write('\\newcommand{\\sdispnuml}{\ensuremath{'+prec3(disp('../DATA/SALT2mu/SALT2mu_fitoptgs_lowz.fitres',99))+'}}\n')

v1.write('\\newcommand{\\salphanump}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgs_ps1.fitres','alpha0',3))+'}}\n')
v1.write('\\newcommand{\\sbetanump}{\ensuremath{'+precb(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgs_ps1.fitres','beta0',3))+'}}\n')
v1.write('\\newcommand{\\sgammanump}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgs_ps1.fitres','gamma0',3))+'}}\n')
v1.write('\\newcommand{\\sintnump}{\ensuremath{'+prec2b(grabfitres2('../DATA/SALT2mu/SALT2mu_fitoptgs_ps1.fitres','iterat',3))+'}}\n')
v1.write('\\newcommand{\\sdispnump}{\ensuremath{'+prec3(disp('../DATA/SALT2mu/SALT2mu_fitoptgs_ps1.fitres',99))+'}}\n')


v1.write('\\newcommand{\\calphanumg}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptcs_global.fitres','alpha0',3))+'}}\n')
v1.write('\\newcommand{\\cbetanumg}{\ensuremath{'+precb(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptcs_global.fitres','beta0',3))+'}}\n')
v1.write('\\newcommand{\\cgammanumg}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptcs_global.fitres','gamma0',3))+'}}\n')
v1.write('\\newcommand{\\cintnumg}{\ensuremath{'+prec2b(grabfitres2('../DATA/SALT2mu/SALT2mu_fitoptcs_global.fitres','iterat',3))+'}}\n')
v1.write('\\newcommand{\\cdispnumg}{\ensuremath{'+prec3(disp('../DATA/SALT2mu/SALT2mu_fitoptcs_global.fitres',99))+'}}\n')


v1.write('\\newcommand{\\calphanums}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptcs_snls.fitres','alpha0',3))+'}}\n')
v1.write('\\newcommand{\\cbetanums}{\ensuremath{'+precb(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptcs_snls.fitres','beta0',3))+'}}\n')
v1.write('\\newcommand{\\cgammanums}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptcs_snls.fitres','gamma0',3))+'}}\n')
v1.write('\\newcommand{\\cintnums}{\ensuremath{'+prec2b(grabfitres2('../DATA/SALT2mu/SALT2mu_fitoptcs_snls.fitres','iterat',3))+'}}\n')
v1.write('\\newcommand{\\cdispnums}{\ensuremath{'+prec3(disp('../DATA/SALT2mu/SALT2mu_fitoptcs_snls.fitres',99))+'}}\n')

v1.write('\\newcommand{\\calphanumd}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptcs_sdss.fitres','alpha0',3))+'}}\n')
v1.write('\\newcommand{\\cbetanumd}{\ensuremath{'+precb(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptcs_sdss.fitres','beta0',3))+'}}\n')
v1.write('\\newcommand{\\cgammanumd}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptcs_sdss.fitres','gamma0',3))+'}}\n')
v1.write('\\newcommand{\\cintnumd}{\ensuremath{'+prec2b(grabfitres2('../DATA/SALT2mu/SALT2mu_fitoptcs_sdss.fitres','iterat',3))+'}}\n')
v1.write('\\newcommand{\\cdispnumd}{\ensuremath{'+prec3(disp('../DATA/SALT2mu/SALT2mu_fitoptcs_sdss.fitres',99))+'}}\n')

v1.write('\\newcommand{\\calphanuml}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptcs_lowz.fitres','alpha0',3))+'}}\n')
v1.write('\\newcommand{\\cbetanuml}{\ensuremath{'+precb(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptcs_lowz.fitres','beta0',3))+'}}\n')
v1.write('\\newcommand{\\cgammanuml}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptcs_lowz.fitres','gamma0',3))+'}}\n')
v1.write('\\newcommand{\\cintnuml}{\ensuremath{'+prec2b(grabfitres2('../DATA/SALT2mu/SALT2mu_fitoptcs_lowz.fitres','iterat',3))+'}}\n')
v1.write('\\newcommand{\\cdispnuml}{\ensuremath{'+prec3(disp('../DATA/SALT2mu/SALT2mu_fitoptcs_lowz.fitres',99))+'}}\n')

v1.write('\\newcommand{\\calphanump}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptcs_ps1.fitres','alpha0',3))+'}}\n')
v1.write('\\newcommand{\\cbetanump}{\ensuremath{'+precb(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptcs_ps1.fitres','beta0',3))+'}}\n')
v1.write('\\newcommand{\\cgammanump}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptcs_ps1.fitres','gamma0',3))+'}}\n')
v1.write('\\newcommand{\\cintnump}{\ensuremath{'+prec2b(grabfitres2('../DATA/SALT2mu/SALT2mu_fitoptcs_ps1.fitres','iterat',3))+'}}\n')
v1.write('\\newcommand{\\cdispnump}{\ensuremath{'+prec3(disp('../DATA/SALT2mu/SALT2mu_fitoptcs_ps1.fitres',99))+'}}\n')

v1.write('\\newcommand{\\oalphanump}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgos_ps1.fitres','alpha0',3))+'}}\n')
v1.write('\\newcommand{\\obetanump}{\ensuremath{'+precb(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgos_ps1.fitres','beta0',3))+'}}\n')
v1.write('\\newcommand{\\ogammanump}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgos_ps1.fitres','gamma0',3))+'}}\n')
v1.write('\\newcommand{\\ointnump}{\ensuremath{'+prec2b(grabfitres2('../DATA/SALT2mu/SALT2mu_fitoptgos_ps1.fitres','iterat',3))+'}}\n')
v1.write('\\newcommand{\\odispnump}{\ensuremath{'+prec3(disp('../DATA/SALT2mu/SALT2mu_fitoptgos_ps1.fitres',99))+'}}\n')

v1.write('\\newcommand{\\oalphanums}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgos_snls.fitres','alpha0',3))+'}}\n')
v1.write('\\newcommand{\\obetanums}{\ensuremath{'+precb(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgos_snls.fitres','beta0',3))+'}}\n')
v1.write('\\newcommand{\\ogammanums}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgos_snls.fitres','gamma0',3))+'}}\n')
v1.write('\\newcommand{\\ointnums}{\ensuremath{'+prec2b(grabfitres2('../DATA/SALT2mu/SALT2mu_fitoptgos_snls.fitres','iterat',3))+'}}\n')
v1.write('\\newcommand{\\odispnums}{\ensuremath{'+prec3(disp('../DATA/SALT2mu/SALT2mu_fitoptgos_snls.fitres',99))+'}}\n')

v1.write('\\newcommand{\\oalphanumd}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgos_sdss.fitres','alpha0',3))+'}}\n')
v1.write('\\newcommand{\\obetanumd}{\ensuremath{'+precb(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgos_sdss.fitres','beta0',3))+'}}\n')
v1.write('\\newcommand{\\ogammanumd}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgos_sdss.fitres','gamma0',3))+'}}\n')
v1.write('\\newcommand{\\ointnumd}{\ensuremath{'+prec2b(grabfitres2('../DATA/SALT2mu/SALT2mu_fitoptgos_sdss.fitres','iterat',3))+'}}\n')
v1.write('\\newcommand{\\odispnumd}{\ensuremath{'+prec3(disp('../DATA/SALT2mu/SALT2mu_fitoptgos_sdss.fitres',99))+'}}\n')

v1.write('\\newcommand{\\oalphanuml}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgos_lowz.fitres','alpha0',3))+'}}\n')
v1.write('\\newcommand{\\obetanuml}{\ensuremath{'+precb(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgos_lowz.fitres','beta0',3))+'}}\n')
v1.write('\\newcommand{\\ogammanuml}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgos_lowz.fitres','gamma0',3))+'}}\n')
v1.write('\\newcommand{\\ointnuml}{\ensuremath{'+prec2b(grabfitres2('../DATA/SALT2mu/SALT2mu_fitoptgos_lowz.fitres','iterat',3))+'}}\n')
v1.write('\\newcommand{\\odispnuml}{\ensuremath{'+prec3(disp('../DATA/SALT2mu/SALT2mu_fitoptgos_lowz.fitres',99))+'}}\n')


v1.write('\\newcommand{\\oalphanumg}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgos_global.fitres','alpha0',3))+'}}\n')
v1.write('\\newcommand{\\obetanumg}{\ensuremath{'+precb(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgos_global.fitres','beta0',3))+'}}\n')
v1.write('\\newcommand{\\ogammanumg}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgos_global.fitres','gamma0',3))+'}}\n')
v1.write('\\newcommand{\\ointnumg}{\ensuremath{'+prec2b(grabfitres2('../DATA/SALT2mu/SALT2mu_fitoptgos_global.fitres','iterat',3))+'}}\n')
v1.write('\\newcommand{\\odispnumg}{\ensuremath{'+prec3(disp('../DATA/SALT2mu/SALT2mu_fitoptgos_global.fitres',99))+'}}\n')

v1.write('\\newcommand{\\ogammanumeg}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgose_global.fitres','gamma0',3))+'}}\n')
v1.write('\\newcommand{\\egammanumeg}{\ensuremath{'+prec(grabfitres('../DATA/SALT2mu/SALT2mu_fitoptgose_global.fitres','gamma1',3))+'}}\n')

v1.write('\\newcommand{\pdispnump}{\ensuremath{'+prec3b(disp('../DATA/SALT2mu/SALT2mu_fitoptg0.fitres',99,cut=0.05))+'}}\n')
v1.write('\\newcommand{\pdispnumn}{\ensuremath{'+prec3b(disp('../DATA/SALT2mu/SALT2mu_fitoptg0nopec.fitres',99,cut=0.05))+'}}\n')


v1.close()

v1=open('param_palphabeta.table','w')
v1.write('PS1-BCD & $\salphanump$ & $\sbetanump$ & $\sgammanump$ & $\sintnump$ '+r'\\'+'\n')
v1.write('PS1-nom & $\salphanumo$ & $\sbetanumo$ & $\sgammanumo & $\sintnumo$ '+r'\\'+'\n')
v1.close()

v1=open('param_alphabeta.table','w')
v1.write('G10: &~ &~ &~ &~ '+r'\\'+'\n')
v1.write('All & $\salphanumg$ & $\sbetanumg$ & $\sgammanumg$ & $\sintnumg$ '+r'\\'+'\n')
v1.write('Low-z & $\salphanuml$ & $\sbetanuml$ & $\sgammanuml$ & $\sintnuml$ '+r'\\'+'\n')
v1.write('SDSS & $\salphanumd$ & $\sbetanumd$ & $\sgammanumd$ & $\sintnumd$ '+r'\\'+'\n')
v1.write('PS1 & $\salphanump$ & $\sbetanump$ & $\sgammanump$ & $\sintnump$ '+r'\\'+'\n')
v1.write('SNLS & $\salphanums$ & $\sbetanums$ & $\sgammanums & $\sintnums$ '+r'\\'+'\n')
v1.write('C11: &~ &~ &~ &~ '+r'\\'+'\n')
v1.write('All & $\calphanumg$ & $\cbetanumg$ & $\cgammanumg$ & $\cintnumg$ '+r'\\'+'\n')
v1.write('Low-z & $\calphanuml$ & $\cbetanuml$ & $\cgammanuml$ & $\cintnuml$ '+r'\\'+'\n')
v1.write('SDSS & $\calphanumd$ & $\cbetanumd$ & $\cgammanumd$ & $\cintnumd$ '+r'\\'+'\n')
v1.write('PS1 & $\calphanump$ & $\cbetanump$ & $\cgammanump$ & $\cintnump$ '+r'\\'+'\n')
v1.write('SNLS & $\calphanums$ & $\cbetanums$ & $\cgammanums & $\cintnums$ '+r'\\'+'\n')

v1.close()

