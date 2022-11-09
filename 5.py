# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 20:27:38 2021

@author: pasouza
"""

# Trajeto dos walkers em 1d
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

M = 100 # Número de walkers
L = 100 # Tamanho da malha

# A cada intervalo de tempo, mover os walkers

p = 0.1 # Probabilidade de andar
pinv = 1.0-p
nsteps = 2001 # Número de intervalos de tempo

# Iniciando os walkers

x = np.random.randint(-M, M+1, M) # Posição inicial dos walkers
edges = np.array(range(-L,L+1))-0.5
xc = 0.5*(edges[:-1]+edges[1:])
y = np.zeros(M)

#%%

def animate(it):
    global x
    x = get_data(x, M)

    # Trajetória dos walkers no eixo x
    if (np.mod(it,noutput)==0):
        plot.set_offsets(np.array((x, y)).T)
        ax.set_title('Tempo = {}'.format(it))
      
    # Apenas geração de frames para o trabalho escrito        
    noutput2 = 100
    if (np.mod(it,noutput2)==0):
        plot.set_offsets(np.array((x, y)).T)
        ax.set_title('Tempo = {}'.format(it))
        plt.savefig('tempo_{}.png'.format(it), dpi = 300, bbox_inches = 'tight')
    return plot

def get_data(x, M):
    # Atualizar a posição de todos os walkers
    for iw in range(M):
        rnd = np.random.rand(1)
        dx = -1*(rnd<p)+1*(rnd>pinv)
        x[iw] = x[iw] + dx
    return x

plt.ion()
noutput = 5
fig, ax = plt.subplots()
fig.set_size_inches(12, 2)
fig.set_tight_layout(True)
ax.set_xlim((-100, 100))
ax.axes.get_yaxis().set_visible(False)
ax.set_xlabel('Distância percorrida')
x = get_data(x, M)
plot = ax.scatter (x, y, s = 1)

ani = animation.FuncAnimation(fig = fig, func = animate, frames = nsteps, interval = 50)
ani.save('randomwalk1drand.mp4')
plt.show()