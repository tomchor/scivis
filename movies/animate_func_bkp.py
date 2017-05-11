import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

A=np.load('../../data/TC.npz')
T=A['T']


fig = plt.figure()


def f(x, y):
    return np.sin(x) + np.cos(y)

x = np.linspace(0, 2 * np.pi, 120)
y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)
it = 0

im = plt.imshow(T[it], animated=True, cmap='seismic', origin='lower', extent=[-1e3, 1e3, -1e3, 1e3])
def updatefig(it):
    im.set_array(T[it])
    return im,

ani = animation.FuncAnimation(fig, updatefig, frames=np.arange(0,300), interval=50, blit=True)
ani.save('func.mp4')
