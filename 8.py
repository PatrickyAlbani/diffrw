# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 18:48:08 2021

@author: pasouza
"""

# Trajeto dos walkers em 2d
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

M = 100 # Número de walkers
L = 100 # Tamanho da malha

# A cada intervalo de tempo, mover os walkers

p = 0.1 # Probabilidade de andar
pinv = 1.0-p
nsteps = 2001 # Número de intervalos de tempo

# Iniciando os walkers

Z = [(0,0) for i in range (M)] # Posição inicial dos walkers (x, y)
edgesrw = np.array(range(-L,L+1))-0.5
xc = 0.5*(edgesrw[:-1]+edgesrw[1:])

#%%

def animate(it):
    global x
    x = get_data(Z, M)

    # Trajetória dos walkers nos eixos x e y
    if (np.mod(it,noutput)==0):
        plot.set_offsets(Z)
        ax.set_title('Tempo = {}'.format(it))

    # Apenas geração de frames para o trabalho escrito     
    noutput2 = 100
    if (np.mod(it,noutput2)==0):
        plot.set_offsets(Z)
        ax.set_title('Tempo = {}'.format(it))
        plt.savefig('tempo_{}.png'.format(it), dpi = 300)
    return plot

def get_data(Z, M):
    # Atualizar a posição de todos os walkers
    for iw in range(M):
        rndx = random.random()
        dx = -1*(rndx<p)+1*(rndx>pinv)
        rndy = random.random()
        dy = -1*(rndy<p)+1*(rndy>pinv)
        x, y = Z[iw]
        Z[iw] = x+dx, y+dy
    return Z

plt.ion()
noutput = 5
fig, ax = plt.subplots()
fig.set_size_inches(6, 6)
ax.set_xlim((-100, 100))
ax.set_ylim((-100, 100))
ax.set_xlabel('Distância percorrida (x)')
ax.set_ylabel('Distância percorrida (y)')
x = get_data(Z, M)
plot = ax.scatter (*zip(*Z), s = 1)
            
ani = animation.FuncAnimation(fig = fig, func = animate, frames = nsteps, interval = 50)
ani.save('randomwalk2d.mp4')
plt.show()