# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 20:27:38 2021

@author: pasouza
"""

# Comparação entre random walk e difusão em 2d
import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib.patches as mpatches
from matplotlib.cm import get_cmap

M = 100000 # Número de walkers
L = 100 # Tamanho da malha

# A cada intervalo de tempo, mover os walkers e propagar a difusão

p = 0.1 # Probabilidade de andar
pinv = 1.0-p
nsteps = 2001 # Número de intervalos de tempo

# Iniciando os walkers

Z = [(0,0) for i in range (M)] # Posição inicial dos walkers (x, y)
edgesrw = np.array(range(-L,L+1))-0.5
xc = 0.5*(edgesrw[:-1]+edgesrw[1:])
xx, yy = np.meshgrid(xc, xc)

#  Iniciando as concentrações

c = np.zeros((2,2*L+1,2*L+1))
i0 = 0
i1 = 1
c[:,L,L] = M # c[:,L,L] corresponde a (x,y) = (0,0)
edgesdiff = np.array(range(-L,L+2))-0.5
xc = 0.5*(edgesdiff[:-1]+edgesdiff[1:])
xx, yy = np.meshgrid(xc, xc)
D = p

#%%
noutput = 100
for it in range(nsteps):
    # Atualizar a posição de todos os walkers
    for iw in range(M):
        rndx = random.random()
        dx = -1*(rndx<p)+1*(rndx>pinv)
        rndy = random.random()
        dy = -1*(rndy<p)+1*(rndy>pinv)
        x, y = Z[iw]
        Z[iw] = x+dx, y+dy
        
    # Executar a etapa na equação de difusão
    for ix in range(1,len(c[0])-1):
        for iy in range (1,len(c[0])-1):
            # Usar i0 e gerar i1
            c[i1,ix,iy] = c[i0,ix,iy] + D*(c[i0,ix-1,iy]+c[i0,ix+1,iy]-4*c[i0,ix,iy]+c[i0,ix,iy-1]+c[i0,ix,iy+1])
    # Inverter i0 e i1
    ii = i1
    i1 = i0
    i0 = ii
        
    # Plotar as concentrações
    if (np.mod(it,noutput)==0):
        fig = plt.figure()
        ax = fig.add_subplot(121, projection = '3d')
        x,y = list(zip(*Z))
        bins = xc.shape[0]
        H, xedges, yedges = np.histogram2d(x, y, bins = bins, range = [[-100,100],[-100,100]])
        ax.cla()
        rw = ax.plot_surface(xx, yy, H, cmap = "Blues")
        ax.set_xlabel('Distância percorrida (x)')
        ax.set_ylabel('Distância percorrida (y)')
        ax.set_zlabel('Concentração')
        rw_cmap = get_cmap('Blues')
        rw_rgba = rw_cmap(0.8)
        rw_patch = mpatches.Patch(color = rw_rgba, label = 'Random Walk')
        ax.legend(handles = [rw_patch])
        
        ax = fig.add_subplot(122, projection = '3d')
        diff = ax.plot_surface(xx, yy, c[0,:,:], cmap = "Reds")
        ax.set_xlabel('Distância percorrida (x)')
        ax.set_ylabel('Distância percorrida (y)')
        ax.set_zlabel('Concentração')
        diff_cmap = get_cmap('Reds')
        diff_rgba = diff_cmap(0.8)
        diff_patch = mpatches.Patch(color = diff_rgba, label = 'Difusão')
        ax.legend(handles = [diff_patch])
        
        plt.suptitle('Tempo = {}, M = {}, p = {}'.format(it, M, p), y = 0.9)
        plt.tight_layout(w_pad = 5.0)
        plt.savefig('tempo_{}.png'.format(it), dpi = 600, bbox_inches = 'tight')
        plt.pause(0.001)
