# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 01:11:42 2022

@author: 13072
"""


import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-pastel')

length = 4
w = 1
k = np.pi*(1/2)*(1/length)
while (True):
    try:
        c = float(input("Enter speed: "))
        break
    except ValueError: 
        print ("Not a valid number. Try again.")
while (True):
    try:
        num = int(input("Enter which harmonic you want: "))
        break
    except ValueError:
        print ("Not a valid entry. Please enter an integer.")


fig = plt.figure()
ax = plt.axes(xlim=(0, 4), ylim=(-2, 2))
line, = ax.plot([], [], lw=3)

def init():
    line.set_data([], [])
    return line,
def animate(i):
    x = np.linspace(0, 4, 1000)
    y = np.sin((num*np.pi/length)*x)*(np.cos(num*(np.pi/length)*i*c)+np.sin(num*(np.pi/length)*i*c))
    line.set_data(x, y)
    return line,

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)


anim.save('sine_wave.gif', writer='imagemagick')

 