# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 20:05:50 2022

@author: pasouza
"""

# Trajeto dos walkers em 3d
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as mpatches
import random

M = 100 # Número de walkers
L = 50 # Tamanho da malha

# A cada intervalo de tempo, mover os walkers

p = 0.22 # Probabilidade de andar, coeficiente de difusão
p0 = 0.22
pinv = 1.0-p
alpha = 0.9 # Slope da curva experimental
nsteps = 2001 # Número de intervalos de tempo

# Iniciando os walkers

x = np.zeros(M) # Posição inicial dos walkers nos eixos x, y e z
Z = [(0,0,0) for i in range (M)]
edgesrw = np.array(range(-L,L+1))-0.5
xc = 0.5*(edgesrw[:-1]+edgesrw[1:])

#%%

def animate(it):
    global x

    # Trajetória dos walkers nos eixos x, y e z
    if (np.mod(it,noutput)==0):
        if it == 0:
            p = p0
        else:
            p = p0*it**(alpha-1)
        pinv = 1.0-p
            
        x = get_data(Z, M, p, pinv)
        A = np.float64(Z)
        plot._offsets3d = (A[:,0], A[:,1], A[:,2])
        ax.set_title('Tempo = {}, alpha = {}, p = {}'.format(it, alpha, str(round(p, 4))))

        # Apenas geração de frames para o trabalho escrito 
        noutput2 = 100
        if (np.mod(it,noutput2)==0):
            plot._offsets3d = (A[:,0], A[:,1], A[:,2])
            ax.set_title('Tempo = {}, alpha = {}, p = {}'.format(it, alpha, str(round(p, 4))))
            plt.savefig('tempo_{}.png'.format(it), dpi = 300)
        return plot

def get_data(Z, M, p, pinv):
    # Atualizar a posição de todos os walkers
    for iw in range(M):
        rndx = random.random()
        dx = -1*(rndx<p)+1*(rndx>pinv)
        rndy = random.random()
        dy = -1*(rndy<p)+1*(rndy>pinv)
        rndz = random.random()
        dz = -1*(rndz<p)+1*(rndz>pinv)
        x, y, z = Z[iw]
        Z[iw] = x+dx, y+dy, z+dz
    return Z

plt.ion()
noutput = 5
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
fig.set_size_inches(6, 6)
ax.set_xlim((-50, 50))
ax.set_ylim((-50, 50))
ax.set_zlim((-50, 50))
ax.set_xlabel('Distância percorrida (x)')
ax.set_ylabel('Distância percorrida (y)')
ax.set_zlabel('Distância percorrida (z)')
subs1 = mpatches.Patch(color = 'red', label = "Ca²\u207A")
ax.legend(handles = [subs1])

x = get_data(Z, M, p, pinv)
plot = ax.scatter (*zip(*Z), marker = 'o', s = 3, color = 'red')
          
ani = animation.FuncAnimation(fig = fig, func = animate, frames = nsteps, interval = 50)
ani.save('Íons Ca2+, alpha = {}.mp4'.format(alpha))
plt.show()