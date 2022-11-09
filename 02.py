# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 20:27:38 2021

@author: pasouza
"""

# Comparação entre random walk e difusão em 1d
import numpy as np
import matplotlib.pyplot as plt

M = 100000 # Número de walkers
L = 100 # Tamanho da malha

# A cada intervalo de tempo, mover os walkers e propagar a difusão

p = 0.1 # Probabilidade de andar
pinv = 1.0-p
nsteps = 2001 # Número de intervalos de tempo

# Iniciando os walkers

x = np.zeros(M) # Posição inicial dos walkers
x[:int(M/2)] = 50
x[int(M/2):] = -50
edges = np.array(range(-L,L+1))-0.5
xc = 0.5*(edges[:-1]+edges[1:])

#  Iniciando as concentrações

c = np.zeros ((2*L+1,2))
i0 = 0
i1 = 1
c[50] = M/2
c[150] = M/2
cx = range(-L,L+1)
D = p

#%%
plt.ion()
noutput = 100
for it in range(nsteps):
    # Atualizar a posição de todos os walkers
    for iw in range(M):
        rnd = np.random.rand(1)
        dx = -1*(rnd<p)+1*(rnd>pinv)
        x[iw] = x[iw] + dx
        
    # Executar a etapa na equação de difusão
    for ix in range(1,len(c)-1):
        # Usar i0 e gerar i1
        c[ix,i1] = c[ix,i0] + D*(c[ix-1,i0]-2*c[ix,i0]+c[ix+1,i0])
    # Inverter i0 e i1
    ii = i1
    i1 = i0
    i0 = ii
        
    # Plotar as concentrações
    if (np.mod(it,noutput)==0):
        Nx,e = np.histogram(x,edges)
        plt.clf()
        plt.plot(cx,c[:,0],'r',label='Difusão')
        plt.plot(xc,Nx,'b',label='Random Walk')
        plt.title('Tempo = {}, M = {}, p = {}'.format(it, M, p))
        plt.legend()
        plt.xlabel('Distância percorrida')
        plt.ylabel('Concentração')
        plt.savefig('tempo_{}.png'.format(it), dpi = 300)
        plt.pause(0.001)
