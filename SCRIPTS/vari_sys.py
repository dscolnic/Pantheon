import os
import string
import numpy as np

#SYSLINE: [CALIBRATION] [+cal,=DEFAULT]
#SYSLINE: [NOCALIBRATION] [-cal,=DEFAULT]
#SYSLINE: [SCATTER] [=DEFAULT,=C11]
#SYSLINE: [SHIFTMASS] [=DEFAULT,+DEFAULT_SHIFTMASS]
#SYSLINE: [MASSEVOL] [=DEFAULT,+DEFAULT_EVGAMMA]
#SYSLINE: [EBV] [+MWEBV,=DEFAULT]
#SYSLINE: [VPEC] [+VPEC,=DEFAULT]
#SYSLINE: [SALT] [+SALT,=DEFAULT]
#SYSLINE: [HST_cal] [+HST_cal,=DEFAULT]
#SYSLINE: [SURVCAL] [+survcal,=DEFAULT]
#SYSLINE: [SELECTION] [=DEFAULT,=DEFAULT_SYS]
#SYSLINE: [BETAEVOL] [=DEFAULT,=DEFAULT_EVBETA]
def ff(str1):
         return "{:.3f}".format(str1)
def ffp(str1):
         
         x="{:.3f}".format(str1)
         if ('-' not in x): x='+'+x
         return x

v1=open('vari_sys.table','w')
weadd=[]
weadd2=[]
areas=[]
for jj in range(0,1):
         if (jj==0): survvar,wvar,wverr,omvar,omverr,chi2 = np.loadtxt('/project/rkessler/dscolnic/cosmomc_s16/syscomb.txt', usecols=(0,2,3,4,5,8), unpack=True, dtype='string')
         if (jj==1): survvar,wvar,wverr,omvar,omverr,chi2 = np.loadtxt('/project/rkessler/dscolnic/cosmomc_s16/syscomb.txt', usecols=(0,2,3,4,5,8), unpack=True, dtype='string')

         #xx=(survvar==survs[0])
         w1=wvar
         w1e=wverr
         w1=w1[0][1:-2]
         w1e=w1e[0][1:-2]
         w1x = float(w1)
         w1ex = float(w1e)
         om1e=omverr[0][1:-2]
         print 'area a',1.0/(w1ex*float(om1e))
         area1a=1.0/np.sqrt(w1ex*float(om1e))
         

         #v1.write('Stat. Uncertainty & '+"{:.3f}".format(w1ex)+' & 1.0 '+r'\\'+' \n')
         xx=(survvar==survvar[0])
         w1=wvar[xx]
         w1e=wverr[xx]
         w1=w1[0][1:-2]
         w1e=float(w1e[0][1:-2])
         om1=omvar[xx]
         om1e=omverr[xx]
         om1=om1[0][1:-2]
         om1e=om1e[0][1:-2]
         
         area2=1.0/np.sqrt(w1ex*float(om1e))
         print 'area2',area2/area1a
         w1fixed=float(w1)
         omfixed=float(om1)
         w1vec=[]
         
         omvec=[]
         
         print 'area b',1.0/(float(w1e)*float(om1e))         
         #print w1e,w1x
         errs=np.sqrt(w1e**2-w1ex**2)
         #v1.write('Total Sys Uncertainty & '+"{:.3f}".format(errs)+'& '+"{:.3f}".format(errs**2/w1ex**2)+r'\\'+' \n')
         serrs=w1ex**2
         for i in range(0,len(survvar)):

                  xx=(survvar==survvar[i])  
                  w1=wvar[xx]
                  w1e=wverr[xx]
                  w1=w1[0][1:-2]
                  w1e=float(w1e[0][1:-2])
                  #print w1e,w1x
                  errs=0
                  errs=np.sqrt(w1e**2)
                  weadd=np.append(weadd,errs)
                  
                  w1vec=np.append(w1vec,float(w1)-w1fixed)
                           
                  #weadd2=np.append(weadd2,errs**2/serrs)
                  #w1=float(w1)
                  #w1e=float(w1e)
                  om1=omvar[xx]
                  print 'om1', om1, omfixed
                                    
                  om1e=omverr[xx]
                  om1=om1[0][1:-2]
                  om1e=om1e[0][1:-2]
                  omvec=np.append(omvec,float(om1)-float(omfixed))
                                    
                  chi=chi2[xx]
                  chi=chi[0][1:-2]
                  #print 'area i',1.0/(w1e*float(om1e))
                  area2=1.0/np.sqrt(w1e*float(om1e))
                  areas=np.append(areas,area2/area1a)
                  print area2/area1a

print len(weadd), len(weadd2)
print areas         
print np.prod(areas[0:18])
#we1=(weadd[0:18]+weadd[19:37])/2.0
we1=(weadd[0:18]+weadd[0:18])/2.0
weadd2=weadd*0
xx=(weadd>weadd[0])
yy=(weadd<weadd[0])

weadd[xx]=np.sqrt(weadd[xx]**2-weadd[0]**2)
weadd2[xx]=np.sqrt(weadd[xx]**2/weadd[0]**2)
weadd[yy]=0
weadd2[yy]=0

print 'weadd', weadd
print w1vec
#w1vec=-w1vec
v2=open('vari_sys.tex','w')

v1.write('Stat. Uncertainty & '+ffp(w1vec[0])+' & '+ff(weadd[0])+' & 1.000 '+r'\\'+' \n')
v1.write('Total Sys Uncertainty & '+ffp(w1vec[1])+'& '+ff(weadd[1])+'& '+ff(weadd2[1])+r'\\'+' \n')
v1.write('~~Calibration&~&~&'+r'\\'+' \n')  
v1.write('~~SALT2 Cal & '+ffp(w1vec[9])+'& '+ff(weadd[9])+' & '+ff(weadd2[9])+r'\\'+' \n')
v1.write('~~Survey Cal & '+ffp(w1vec[11])+'& '+ff(weadd[11])+' & '+ff(weadd2[11])+r'\\'+' \n')
v1.write('~~HST Cal & '+ffp(w1vec[10])+'& '+ff(weadd[10])+' & '+ff(weadd2[10])+r'\\'+' \n')
v1.write('~~Supercal & '+ffp(w1vec[14])+'& '+ff(weadd[14])+' & '+ff(weadd2[14])+r'\\'+' \n')
v1.write('~SN Modeling&~&~&'+r'\\'+' \n')
v1.write('~~Selection & '+ffp(w1vec[12])+'& '+ff(weadd[12])+' & '+ff(weadd2[12])+r'\\'+' \n')
v1.write('~~Intrinsic Scatter & '+ffp(w1vec[4])+'& '+ff(weadd[4])+' & '+ff(weadd2[4])+r'\\'+' \n')
v1.write('~~'+r'$\beta$'+' Evol. & '+ffp(w1vec[13])+'& '+ff(weadd[13])+' & '+ff(weadd2[13])+r'\\'+' \n')
v1.write('~~'+r'$\gamma$'+' Evol. & '+ffp(w1vec[6])+'& '+ff(weadd[6])+' & '+ff(weadd2[6])+r'\\'+' \n')
v1.write('~~'+r'$m_{\rm step}$'+'Shift & '+ffp(w1vec[5])+'& '+ff(weadd[5])+' & '+ff(weadd2[5])+r'\\'+' \n')
v1.write('~External&~&~&'+r'\\'+' \n')
v1.write('~~MW Extinction & '+ffp(w1vec[7])+'& '+ff(weadd[7])+' & '+ff(weadd2[7])+r'\\'+' \n')
v1.write('~~Pec. Vel. & '+ffp(w1vec[8])+'& '+ff(weadd[8])+' & '+ff(weadd2[8])+r'\\'+' \n')

#v1.write('~~SNLS & '+ffp(w1vec[15])+'& '+ff(weadd[15])+' & '+ff(weadd2[15])+r'\\'+' \n')
#v1.write('~~SDSS & '+ffp(w1vec[16])+'& '+ff(weadd[16])+' & '+ff(weadd2[16])+r'\\'+' \n')
#v1.write('~~PS1 & '+ffp(w1vec[17])+'& '+ff(weadd[17])+' & '+ff(weadd2[17])+r'\\'+' \n')
#v1.write('~~CSP & '+ffp(w1vec[18])+'& '+ff(weadd[18])+' & '+ff(weadd2[18])+r'\\'+' \n')
#v1.write('~~CFA & '+ffp(w1vec[19])+'& '+ff(weadd[19])+' & '+ff(weadd2[19])+r'\\'+' \n')


#v1.write(survvar[i]+' & $ '+str(errs)+' \pm '+'\\\ \n')
print np.sqrt(np.sum(weadd[4:12]**2))
v1.close()


v2.write('\\newcommand{\\sysstat}{\ensuremath{'+"{:.3f}".format(weadd[0])+'}}\n')
v2.write('\\newcommand{\\syssys}{\ensuremath{'+"{:.3f}".format(weadd[1])+'}}\n')
v2.write('\\newcommand{\\sysbeta}{\ensuremath{'+"{:.3f}".format(weadd[13])+'}}\n')
v2.write('\\newcommand{\\sysint}{\ensuremath{'+"{:.3f}".format(weadd[4])+'}}\n')
v2.write('\\newcommand{\\syssalt}{\ensuremath{'+"{:.3f}".format(weadd[9])+'}}\n')
v2.write('\\newcommand{\\syssurv}{\ensuremath{'+"{:.3f}".format(weadd[11])+'}}\n')
v2.close()
