from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

phi_s = 2
phi_u = 1

def plot(X, Y, fname, nice=False):
    label=r'$\phi_{{{}}}(\zeta)$ (Exp.)'
    labels=[label.format('c'), label.format(r'\theta'), label.format('q'), label.format('w')]
    if nice:
        f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row', figsize=(4,6))
    else:
        f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(4,6))
    for i, ax in enumerate(f.axes):
        ax.grid()
        #set format y "$10^{%+T}$"
        #set format x "$10^{%+T}$"
        ax.set_xlabel(r"$\zeta$ (dimensionless)")
        if i==0 or i==2:
            ax.set_ylabel(r"(Dimensionless)")
        ax.loglog(X[i] ,Y[i], 'ko', markersize=2, label=labels[i])
        #ax.scatter(X[i] ,Y[i], color='k')

        print(i)
        if i==3:
            ax.axhline(y=phi_u, color='k', label='Theor. line')
        else:
            ax.axhline(y=phi_s, color='k', label='Theor. line')

        if nice:
            ax.set_xlim([0.01,10])
            ax.set_ylim([0.5,1000])
            ax.legend()

    #set label "a)" at screen 0.12, 0.915
    #set label "b)" at screen 0.62, 0.915
    #set label "c)" at screen 0.12, 0.415
    #set label "d)" at screen 0.62, 0.415
    if nice:
        plt.tight_layout()
    plt.savefig(fname)
    return f, ax1


c="../../data/phi_c2.csv"
t="../../data/phi_t2.csv"
q="../../data/phi_q2.csv"
w="../../data/phi_w2.csv"

zeta_c, phi_c=np.loadtxt(c, delimiter=',', skiprows=1).T
zeta_t, phi_t=np.loadtxt(t, delimiter=',', skiprows=1).T
zeta_q, phi_q=np.loadtxt(q, delimiter=',', skiprows=1).T
zeta_w, phi_w=np.loadtxt(w, delimiter=',', skiprows=1).T

X=[zeta_c, zeta_t, zeta_q, zeta_w]
Y=[phi_c, phi_t, phi_q, phi_w]

f,axa=plot(X, Y, 'bad_subplots.pdf', nice=False)
f,axa=plot(X, Y, 'good_subplots.pdf', nice=True)

