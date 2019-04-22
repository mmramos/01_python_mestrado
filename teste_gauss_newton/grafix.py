from pylab import *;import scipy as sp;import numpy as np;import matplotlib.pyplot as plt;
import matplotlib.patches as mpatches;import matplotlib.mlab as mlab;from matplotlib.gridspec import GridSpec
from mpl_toolkits.axes_grid1 import make_axes_locatable;from matplotlib.colors import LogNorm
from matplotlib.ticker import MultipleLocator

def grafix1(VP,VPp,m,x,y,c):
    error = []
    for i in range(len(VP)):
        error.append(abs(VP[i]-VPp[i]))
    bins_s=60
    bins_vp = np.linspace(min(VP), max(VP), bins_s)
    scatterP= m+' \n $r=$'+str(round(np.corrcoef(VP,VPp)[0,1],2))
    label_hist_pl = '\n '+x+'\n $\overline{e} =$'+str(round(np.mean(error))) \
    +'\n $\sigma_e =$'+str(round(np.std(error)))
    #--------------------------------------------------------------------------------------------------#
    X_VP  = np.linspace(min(VP), max(VP),bins_s)
    dx_VP = np.histogram(VP ,bins=bins_vp)[1][1] - np.histogram(VP ,bins=bins_vp)[1][0]
    Y_VP  = mlab.normpdf(np.linspace(min(VP),max(VP),bins_s),np.mean(VP),np.sqrt(np.var(VP)))*len(VP)*dx_VP
    #-----------------------------------------------------------------------------------------------------#
    X_VPp  = np.linspace(min(VPp), max(VPp),bins_s)
    dx_VPp = np.histogram(VPp ,bins=bins_vp)[1][1] - np.histogram(VPp ,bins=bins_vp)[1][0]
    Y_VPp  = mlab.normpdf(np.linspace(min(VPp),max(VPp),bins_s),np.mean(VPp),np.sqrt(np.var(VPp)))*len(VPp)*dx_VPp
    #-----------------------------------------------------------------------------------------------------#
    fig = plt.figure(figsize= (12,12))

    ax1 = plt.subplot(222)
    ax1.hist(VP,bins_vp,histtype='bar',stacked=True,color='k',alpha=0.5,label='Valores $VP$')
    ax1.plot(X_VP,Y_VP,linewidth=2,color='k')
    ax1.hist(VPp , bins_vp, histtype='bar', stacked=True, color=c, alpha=0.3,label=label_hist_pl)
    ax1.plot(X_VPp,Y_VPp,linewidth = 2, color=c)
    plt.xlabel('Velocidades $(m / s)$');plt.ylabel('Distribuição');plt.grid();plt.xlim(xmax=max(VP),xmin=min(VP));
    plt.ylim(ymax=180,ymin=0);legend = ax1.legend(loc=1, shadow=True)

    ax2=plt.subplot(221);ax2.plot(VP,VP,'+k');ax2.plot(VP,VPp,'+'+c,label=scatterP);legend=ax2.legend(loc=4)
    plt.xlim(xmax=max(VP),xmin=min(VP));plt.ylim(ymax=max(VP),ymin=min(VP));
    plt.xlabel('Velocidade Original $VP$ em $m/s$')
    plt.ylabel('Velocidade Estimada '+x+' em $m/s$');plt.grid()

    plt.show()
    
def grafix2(VP,VPp,m,x,y,c):
    error = []
    for i in range(len(VP)):
        error.append(abs(VP[i]-VPp[i]))
    bins_s=60
    bins_vp = np.linspace(min(VP), max(VP), bins_s)
    scatterP= m+' \n $r=$'+str(round(np.corrcoef(VP,VPp)[0,1],2))
    label_hist_pl = '\n '+x+'\n $\overline{e} =$'+str(round(np.mean(error))) \
    +'\n $\sigma_e =$'+str(round(np.std(error)))
    #--------------------------------------------------------------------------------------------------#
    X_VP  = np.linspace(min(VP), max(VP),bins_s)
    dx_VP = np.histogram(VP ,bins=bins_vp)[1][1] - np.histogram(VP ,bins=bins_vp)[1][0]
    Y_VP  = mlab.normpdf(np.linspace(min(VP),max(VP),bins_s),np.mean(VP),np.sqrt(np.var(VP)))*len(VP)*dx_VP
    #-----------------------------------------------------------------------------------------------------#
    X_VPp  = np.linspace(min(VPp), max(VPp),bins_s)
    dx_VPp = np.histogram(VPp ,bins=bins_vp)[1][1] - np.histogram(VPp ,bins=bins_vp)[1][0]
    Y_VPp  = mlab.normpdf(np.linspace(min(VPp),max(VPp),bins_s),np.mean(VPp),np.sqrt(np.var(VPp)))*len(VPp)*dx_VPp
    #-----------------------------------------------------------------------------------------------------#
    fig = plt.figure(figsize= (12,12))

    ax1 = plt.subplot(222)
    ax1.hist(VP,bins_vp,histtype='bar',stacked=True,color='k',alpha=0.5,label='Valores $VP$')
    ax1.plot(X_VP,Y_VP,linewidth=2,color='k')
    ax1.hist(VPp , bins_vp, histtype='bar', stacked=True, color=c, alpha=0.3,label=label_hist_pl)
    ax1.plot(X_VPp,Y_VPp,linewidth = 2, color=c)
    plt.xlabel('Velocidades $(m / s)$',fontsize=16);plt.ylabel('Distribuição',fontsize=16);plt.grid();plt.xlim(xmax=max(VP),xmin=min(VP));
    plt.ylim(ymax=180,ymin=0);legend = ax1.legend(loc=1, shadow=True,fontsize=16)
    ax1.tick_params(axis='x', labelsize=16)
    ax1.tick_params(axis='y', labelsize=16)

    ax2=plt.subplot(221);ax2.plot(VP,VP,'+k');ax2.plot(VP,VPp,'+'+c,label=scatterP);legend=ax2.legend(loc=4,fontsize=16)
    plt.xlim(xmax=max(VP),xmin=min(VP));plt.ylim(ymax=max(VP),ymin=min(VP));
    plt.xlabel('Velocidade Original $VP$ em $m/s$',fontsize=16)
    plt.ylabel('Velocidade Estimada '+x+' em $m/s$',fontsize=16);plt.grid()
    ax2.tick_params(axis='x', labelsize=16)
    ax2.tick_params(axis='y', labelsize=16)

    plt.show()

