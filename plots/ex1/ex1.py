import numpy as np
from matplotlib import pyplot as plt

# Create made up x data (50 points from 0 to 10)
x=np.linspace(0,10,50)
# Create y data with sin() and a random component from -0.3 to 0.3 (3 curves!)
curves = [ np.sin(x/3) + np.random.randn(50)*.3 for i in range(3)]

# Plot each of the curves with alpha=.5, which fades the curve
for i, curve in enumerate(curves):
    plt.plot(x, curve, label='Model {}'.format(i), alpha=.5)
# Now we plot the main line
plt.plot(x, np.sin(x/3) + np.random.randn(50)*.1, label='My model', color='black', linewidth=2)

# Include title, grid and labels
plt.title('Comparison of my model with others')
plt.grid()
plt.ylabel('Radiation (W/m$^2$)')
plt.xlabel('Time (hours)')
# legend() is necssary for the curve labels to appear
plt.legend()
plt.savefig('ex1.pdf')
