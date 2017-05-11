import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

A=np.load('../data/wTC.npz')
C=A['C']

fig = plt.figure()
ims = []
for it in range(300):
    im = plt.imshow(C[it], animated=True, cmap='plasma', origin='lower', extent=[0, 1e3, 0, 1e3],
        vmin=0., vmax=10., interpolation='bicubic')
    tx = im.axes.text(0, 0, 'Timestep: {}'.format(it), color='white') 
    ims.append([im, tx])

plt.colorbar(label='Oil Concentration (kg/m$^3$)')
plt.xlabel('$x$ (m)')
plt.ylabel('$y$ (m)')
plt.title('Concentration at the top of a convective ocean')
plt.tight_layout()
ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)
ani.save('C_linear.mp4', dpi=150)
plt.close('all')



from matplotlib.colors import LogNorm
fig = plt.figure()
ims = []
for it in range(300):
    im = plt.imshow(C[it], animated=True, cmap='plasma', origin='lower', extent=[0, 1e3, 0, 1e3],
        vmin=1.e-3, vmax=1., interpolation='bicubic', norm=LogNorm())
    tx = im.axes.text(0, 0, 'Timestep: {}'.format(it), color='white') 
    ims.append([im, tx])

plt.colorbar(label='Oil Concentration (kg/m$^3$)')
plt.xlabel('$x$ (m)')
plt.ylabel('$y$ (m)')
plt.title('Concentration at the top of a convective ocean')
plt.tight_layout()
ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)
ani.save('C_log.mp4', dpi=150)
