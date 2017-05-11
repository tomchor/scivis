from matplotlib import pyplot as plt
import numpy as np

# Define a function to make the plot nicer
def makeitnice():
    plt.xlabel('$x$ (m)')
    plt.ylabel('$y$ (m)')
    plt.tight_layout()
    return

# load data from a numpy binary file
A=np.load('../../data/wTC.npz')
w0=A['w'] # w0 is a 2D (x-y) array

# Plot filled contour
plt.contourf(w0, cmap='jet')
plt.colorbar(label='Vertical velocity (m/s)')
plt.title('First plot looks bad')
makeitnice()
plt.savefig('jet.png')

# Plot filled contour
plt.figure()
plt.contourf(w0, cmap='viridis')
plt.colorbar(label='Vertical velocity (m/s)')
plt.title('A slightly improved version')
makeitnice()
plt.savefig('viridis.png')

# Plot filled contour
plt.figure()
levels=np.linspace(-5e-3, 5e-3, 11)
plt.contourf(w0, levels, cmap='seismic', extend='both')
plt.colorbar(label='Vertical velocity (m/s)')
plt.title('A better version')
makeitnice()
plt.savefig('rdbu.png')
