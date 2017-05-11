import numpy as np
import matplotlib.pyplot as plt

def makeitnice():
    plt.xlabel('$x$ (m)')
    plt.ylabel('$y$ (m)')
    plt.tight_layout()
    return
    
# create artificial data
y, x = np.mgrid[-4:4:50j, -4:4:50j]
U =-5*y #+ np.random.randn(*x.shape)*.2
V =+5*x #+ np.random.randn(*y.shape)*.2
speed = np.sqrt(U**2+V**2)
nspeed=4*speed/speed.max()

# Here we plot every other third point because otherwise there are too many quivers and it's hard to see!
plt.figure(figsize=(8,5))
Q = plt.quiver(x[::3, ::3], y[::3, ::3], U[::3, ::3], V[::3, ::3], pivot='mid', scale_units='dots', scale=1)
plt.quiverkey(Q, 0.9, 0.05, 20, r'20 m/s', labelpos='E',
                   coordinates='figure')
plt.quiverkey(Q, 0.75, 0.05, 10, r'10 m/s', labelpos='E',
                   coordinates='figure')
plt.title('Quiver plot\nSpeed (m/s)')
makeitnice()
plt.savefig('quiver.png')


plt.figure(figsize=(8,5))
plt.contourf(x,y,speed)
plt.colorbar(label='Speed (m/s)')
Q = plt.quiver(x[::3, ::3], y[::3, ::3], U[::3, ::3], V[::3, ::3], pivot='mid', scale_units='dots', scale=1)
plt.quiverkey(Q, 0.9, 0.05, 20, r'20 m/s', labelpos='E',
                   coordinates='figure')
plt.quiverkey(Q, 0.75, 0.05, 10, r'10 m/s', labelpos='E',
                   coordinates='figure')
plt.title('Quiver plot')
makeitnice()
plt.savefig('quiver_contourf.png')

# We can combine the plots to see something better
plt.figure(figsize=(8,5))
plt.imshow(speed, origin='power', interpolation='bicubic', extent=[x.min(), x.max(), y.min(), y.max()], aspect='auto')
plt.colorbar(label='Speed (m/s)')
plt.streamplot(x,y,U,V, linewidth=nspeed, color='k')
plt.title('Streamlines (sort of)')
makeitnice()
plt.savefig('streamlines.png')
plt.close()

# Streamlines are also possible
plt.figure(figsize=(6,5))
plt.imshow(speed, origin='power', interpolation='bicubic', extent=[x.min(), x.max(), y.min(), y.max()], aspect=1)
plt.colorbar(label='Speed (m/s)')
plt.streamplot(x,y,U,V, linewidth=nspeed, color='k')
plt.title('Streamlines (sort of)')
makeitnice()
plt.savefig('streamlines_equal.png')
plt.close()

