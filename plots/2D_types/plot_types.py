import numpy as np
import matplotlib.pyplot as plt

# Function to make the plor look nicer
def makeitnice():
    plt.xlabel('$x$ (m)')
    plt.ylabel('$y$ (m)')
    plt.tight_layout()
    return
    
# Create artificial data
y, x = np.mgrid[-4:2:50j, -4:2:50j]
z = 10 * np.cos(x**2 + y**2) + 5*x + 3*y

# Plot with no interpolation whatsoever
plt.figure(figsize=(8,5))
plt.pcolormesh(x,y,z, vmin=-40, vmax=20)
plt.colorbar(label='Water height (mm)')
plt.title('pcolormesh')
makeitnice()
plt.savefig('pcolormesh.png')

# Plot with a linear interp.
# pcolormesh doesn't have interpolation by default. So we need to change functions
plt.figure(figsize=(8,5))
# note that the extent keywords just gives the limits of the x and y axes
plt.imshow(z, interpolation='bilinear', origin='lower', extent=[x.min(), x.max(), y.min(), y.max()], aspect='auto', vmin=-40, vmax=20)
plt.colorbar(label='Water height (mm)')
plt.title('imshow - bilinear')
makeitnice()
plt.savefig('ims_bilinear.png')

# Same thing but with cubic interpolation
plt.figure(figsize=(8,5))
plt.imshow(z, interpolation='bicubic', origin='lower', extent=[x.min(), x.max(), y.min(), y.max()], aspect='auto', vmin=-40, vmax=20)
plt.colorbar(label='Water height (mm)')
plt.title('imshow - bicubic')
makeitnice()
plt.savefig('ims_bicubic.png')

# Now let's plot it using only contours
plt.figure(figsize=(8,5))
# This creates the contours themselves
CS=plt.contour(x,y,z,5) # 5 is the number of intervals used to colorized. It can be any integer
# This puts the labels in the contours (inline option)
plt.clabel(CS, inline=1, fontsize=10)
plt.title('Only contour')
makeitnice()
plt.savefig('contour.png')

# Now we use interpolation as a background and contour on top of it
plt.figure(figsize=(8,5))
# First the interpolated image, since it's the background
plt.imshow(z, interpolation='bicubic', origin='lower', extent=[-4,2,-4,2], aspect='auto', vmin=-40, vmax=20)
plt.colorbar(label='Water height (mm)')
# Now we create the contours
CS=plt.contour(x,y,z,5, colors='black', linewidths=1.0)
# And finally put the labels in them
plt.clabel(CS, inline=1, fontsize=10)
plt.title('Bicubic + contours')
makeitnice()
plt.savefig('ims_bicubic_contour.png')

# This is almost the same as before, but the contours are filled
plt.figure(figsize=(8,5))
plt.contourf(x,y,z,5) # 5 intervals to be filled
plt.colorbar(label='Water height (mm)')
plt.title('contourf (filled contours)')
makeitnice()
plt.savefig('contourf.png')


