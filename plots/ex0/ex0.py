import numpy as np
from matplotlib import pyplot as plt

# Create some made up simple data
y1=[1,4,6,8]
y2=[1,2,3,4]

# Create a new figure with pre-defined sizes and plot everything
plt.figure(figsize=(3,4))
plt.plot(y1)
plt.plot(y2)
plt.savefig('bad_ex.pdf')
plt.close('all')

# Create another figure with defined sizes
plt.figure(figsize=(3,4))
# Plot with curve labels
plt.plot(y1, label='Speed for runner 1')
plt.plot(y2, label='Speed for runner 2')
# Put axis labels
plt.xlabel('Distance (m)')
plt.ylabel('Speed (m/s)')
# Inlcude title
plt.title('Better version')
# legend() is necessary for the curve labels to appear
plt.legend()
plt.savefig('good_ex.pdf')
