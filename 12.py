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

p1 = 0.22 # Probabilidade de andar, coeficiente de difusão
p2 = 0.22 # Probabilidade de andar, coeficiente de difusão
p20 = 0.22
pinv1 = 1.0-p1
pinv2 = 1.0-p2
alpha = 0.829402 # Slope da curva experimental
nsteps = 2001 # Número de intervalos de tempo

# Iniciando os walkers

Z1 = [(0,0,0) for i in range (M)] # Posição inicial dos walkers nos eixos x, y e z
Z2 = [(0,0,0) for i in range (M)] # Posição inicial dos walkers nos eixos x, y e z
edgesrw = np.array(range(-L,L+1))-0.5
xc = 0.5*(edgesrw[:-1]+edgesrw[1:])

#%%

def animate(it):
    global x

    # Trajetória dos walkers nos eixos x, y e z
    if (np.mod(it,noutput)==0):
        if it == 0:
            p2 = p20
        else:
            p2 = p20*it**(alpha-1)
        pinv2 = 1.0-p2
        
        x = get_data(Z1, Z2, M, p2, pinv2)
        A1 = np.float64(Z1)
        plot1._offsets3d = (A1[:,0], A1[:,1], A1[:,2])
        A2 = np.float64(Z2)
        plot2._offsets3d = (A2[:,0], A2[:,1], A2[:,2])
        ax.set_title('Tempo = {}, alpha = {}, p1 = {}, p2 = {}'.format(it, alpha, p1, str(round(p2, 4))))
        
        # Apenas geração de frames para o trabalho escrito              
        noutput2 = 100
        if (np.mod(it,noutput2)==0):
            A1 = np.float64(Z1)
            plot1._offsets3d = (A1[:,0], A1[:,1], A1[:,2])
            A2 = np.float64(Z2)
            plot2._offsets3d = (A2[:,0], A2[:,1], A2[:,2])
            ax.set_title('Tempo = {}, alpha = {}, p1 = {}, p2 = {}'.format(it, alpha, p1, str(round(p2, 4))))
            plt.savefig('tempo_{}.png'.format(it), dpi = 300)
    return plot1, plot2

def get_data(Z1, Z2, M, p2, pinv2):
    # Atualizar a posição de todos os walkers
    for iw in range(M):
        rndx1 = random.random()
        dx1 = -1*(rndx1<p1)+1*(rndx1>pinv1)
        rndy1 = random.random()
        dy1 = -1*(rndy1<p1)+1*(rndy1>pinv1)
        rndz1 = random.random()
        dz1 = -1*(rndz1<p1)+1*(rndz1>pinv1)
        x1, y1, z1 = Z1[iw]
        Z1[iw] = x1+dx1, y1+dy1, z1+dz1
        
        rndx2 = random.random()
        dx2 = -1*(rndx2<p2)+1*(rndx2>pinv2)
        rndy2= random.random()
        dy2 = -1*(rndy2<p2)+1*(rndy2>pinv2)
        rndz2 = random.random()
        dz2 = -1*(rndz2<p2)+1*(rndz2>pinv2)
        x2, y2, z2 = Z2[iw]
        Z2[iw] = x2+dx2, y2+dy2, z2+dz2
    return Z1, Z2

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
subs1 = mpatches.Patch(color = 'blue', label = "$D_a$$_,$$_b$ constante")
subs2 = mpatches.Patch(color = 'red', label = "$D_a$$_,$$_b$ variável")
ax.legend(handles = [subs1, subs2])

x = get_data(Z1, Z2, M, p2, pinv2)
plot1 = ax.scatter (*zip(*Z1), marker = 'o', s = 3, color = 'blue') 
plot2 = ax.scatter (*zip(*Z2), marker = 'o', s = 3, color = 'red')
          
ani = animation.FuncAnimation(fig = fig, func = animate, frames = nsteps, interval = 50)
ani.save('Comparação entre Dab constante e variável, alpha = {}.mp4'.format(alpha))
plt.show()