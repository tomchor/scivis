import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc

# Just an example of how to use latex fonts for the plot
rc('font', family='serif', serif='Palatino')
rc('text', usetex=True)

# loads the data as an ASCII file (only using the w component of the wind)
W = np.loadtxt('../../data/20110226-1350.out', delimiter=None, usecols=13)

# Create a Probability density function using numpy
plt.figure(figsize=(6,3))
PDF, bin_edges = np.histogram(W, bins=40, density=True)

# Calculate the middle and the width of the bins
bin_mid = (bin_edges[:-1]+bin_edges[1:])/2
width=(bin_edges[1]-bin_edges[0])
# Plot it using a bar graph
plt.bar(bin_mid,PDF, width=width)
# Put labels and such
plt.grid()
plt.title('Probability density function for $w$')
plt.xlabel('$w$ (m/s)')
plt.ylabel('Probability density')
plt.tight_layout()
plt.savefig('pdf.pdf')
