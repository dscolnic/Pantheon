import getdist.plots as gplot
import matplotlib.pyplot as plt
import numpy as np
import plotsetup
gplot.GetDistPlotSettings.figure_legend_frame=False
gplot.GetDistPlotSettings.legend_frame=False
g = gplot.getPlotter(chain_dir = '/scratch/midway/rkessler/dscolnic/cosmomc/chains2')
#plotsetup.halfpaperfig()

g.settings.fig_width_inch = 5.0
g.settings.lw_contour = 2.0
g.settings.solid_contour_palefactor = 0.2
g.settings.legend_frame = False
g.settings.axes_fontsize=12
g.settings.legend_fontsize=12
g.settings.lab_fontsize=14

#g.rcSizes(axes_fontsize=14, lab_fontsize=12, legend_fontsize=14)
#roots = ['cmb_omw', 'tutorG10_omw', 'bao_omw']

roots=['noSN_bao_wwa','DS17_ALL_wwa','DS17_ALL_bao_hst_wwa']

#colors=['teal','k','blue','red']
colors=['#443742','#B098A4','#846C5B','#1A090D']
colors=['#0B3954','#087E8B','#BFD7EA','#FF5A5F','#C81D25']
colors=['#235789','#C1292E','#020100','#FDFFFC']
colors=['#235789','#C1292E','purple','#FDFFFC']
colors=['#235789','#C1292E','gold']

x=np.arange(-2,2,.1)

#line, = g.plot(x, x*0, lw=2,color='black',linestyle='--')
#line, = g.plot(x*0, x, lw=2,color='black',linestyle='--')
g.add_x_marker(-1)
g.add_y_marker(0)
#g.axvline(-1, color='gray', ls='--') 
#g.axhline(0, color='gray', ls='--')

g.plot_2d(roots,'w','wa',
                                filled=[True,True,False,False],colors=colors)
        
#g.plot_2d(roots, 'omeg', 'w', filled=True)
#line, = plt.plot(np.arange(-5,5,0.1), np.arange(-5,5,0.1)*0, lw=1,alpha=0.3)
#line, = plt.plot(np.arange(-5,5,0.1)*0-1, np.arange(-5,5,0.1), lw=1,alpha=0.3)


#plt.xticks([])
#plt.yticks([])

#g.add_legend(['BAO+CMB', 'SN+CMB', 'SN+CMB+BAO','SN+CMB+BAO+H0'], legend_loc='upper right');

props = dict(boxstyle='round', facecolor='white', alpha=0.5)
plt.text(-.95,0.25,"SN+CMB+BAO+H0", color='purple',rotation=0,bbox=props)
#plt.text(0.28,-.75,"CMB+BAO", color='yellow')

props = dict(boxstyle='round', facecolor='blue', alpha=0.5)
plt.text(-0.78,-0.05,"CMB+BAO", color='yellow', bbox=props,rotation=320)

props = dict(boxstyle='round', facecolor='red', alpha=0.5)
plt.text(-1.15,-.3,"Pantheon SN + CMB",color='black', bbox=props,rotation=305)

#leg = plt.legend()
#plt.legend(frameon=False)


g.add_x_marker(-1)
g.add_y_marker(0)
plt.xlabel(r'$w_0$',labelpad=10)
plt.ylabel(r'$w_a$',labelpad=5)
plt.title(r'$w_0w_a$CDM' +' Constraints For Combined Samples')
plt.xlim(-1.25,-0.65)
plt.ylim(-1.0,0.99)
#-1.25 < w0< -0.65 and -1 < wa < 1
plt.figure(figsize=(20,10))
g.export('plot_wwa.png')
