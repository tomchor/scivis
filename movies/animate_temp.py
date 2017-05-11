import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

A=np.load('../data/wTC.npz')
T=A['T']


fig = plt.figure()
ims = []
for it in range(300):
    im = plt.imshow(T[it], animated=True, cmap='viridis', origin='lower', extent=[0, 1e3, 0, 1e3],
        vmin=283.00, vmax=283.10, interpolation='bicubic')
    tx = im.axes.text(0, 0, 'Timestep: {}'.format(it), color='black') 
    ims.append([im, tx])

plt.colorbar(label='T (K)')
plt.xlabel('$x$ (m)')
plt.ylabel('$y$ (m)')
plt.title('Temperature at the top of a convective ocean')
plt.tight_layout()
ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)
ani.save('T_surf.mp4', dpi=150)
