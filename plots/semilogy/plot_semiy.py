import numpy as np
from matplotlib import pyplot as plt

N=200
nlevel=1e4
X = np.linspace(0,1e2,N)
clean = 3*np.exp(-X)
Y = clean + abs(np.random.randn(N)*nlevel*np.exp(-X))


def plot(X, Y, fname, plotfunc=plt.plot, title='', theory=False, set_bounds=False):
    plt.close('all')
    plotfunc(X, Y, label='Exp. data')
    if theory:
        plotfunc(X, clean, label='Theoretical slope')
    plt.grid()
    plt.title(title)
    plt.legend()
    plt.ylabel('Concentration (kg/m$^3)$')
    plt.xlabel('Time (s)')
    if set_bounds:
        plt.ylim(1e-40, 1e6)
    plt.savefig(fname)
    plt.close()
    return


plot(X, Y, 'linlin_exp_decay.pdf', plotfunc=plt.plot, title='Linear attempt')
plot(X, Y, 'semiy_exp_decay.pdf', plotfunc=plt.semilogy, title='Semilog', set_bounds=True)
plot(X, Y, 'semiy_exp_decay2.pdf', plotfunc=plt.semilogy, theory=True, title='Semilog', set_bounds=True)


