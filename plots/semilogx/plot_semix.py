import numpy as np
from matplotlib import pyplot as plt

N=200
nlevel=1e-1
X = np.logspace(-5,1,N)
clean = np.log(2.*X**5.) +1.e2
clean[clean>=80.]=80.
Y = clean + np.random.randn(N)*nlevel*clean

def plot(X, Y, fname, plotfunc=plt.plot, title='', theory=False, set_bounds=False):
    plt.close('all')
    plotfunc(X, Y, label='Exp. data')
    if theory:
        plotfunc(X, np.log(2.*X**5.)+1.e2, label='Log-law')
    plt.grid()
    plt.title(title)
    plt.legend()
    plt.ylabel('Variance of data (a.u.)')
    plt.xlabel('Time (s)')
    if set_bounds:
        plt.ylim(30,100)
    plt.savefig(fname)
    plt.close()
    return


plot(X, Y, 'semix_lin.pdf', title='Linear scale')
plot(X, Y, 'semix_semix.pdf', plotfunc=plt.semilogx, title='With log scale', set_bounds=True)
plot(X, Y, 'semix_semix2.pdf', plotfunc=plt.semilogx, title='With log scale', theory=True, set_bounds=True)

