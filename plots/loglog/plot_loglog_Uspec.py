import numpy as np
from matplotlib import pyplot as plt

# loads the data as an ASCII file
U = np.loadtxt('../../data/20110226-1350.out', delimiter=None, usecols=11)
Ufft = np.fft.rfft(U)
# Creates the power spectrum (except a constants is missing)
Uspec = np.abs(Ufft*np.conjugate(Ufft))
# This creates the frequency vector
freq = np.fft.rfftfreq(len(U), d=1/10)

# For shorthand, we define a function to plot for us, otherwise we would
# have to rewrite this every plot
def plotspec(freq, spec, fname, plotfunc=plt.plot, title='', theory=False, 
        set_bounds=False, errorbars=None):
    if type(errorbars)!=type(None):
        plt.errorbar(freq, spec, yerr=errorbars, label='Exp. data')
        plt.yscale('log')
        plt.xscale('log')
    else:
        plotfunc(freq, spec, label='Exp. data')
    if theory:
        plotfunc(freq, 1e4*freq**(-5/3), label='Theoretical slope')
    if set_bounds:
        plt.xlim(1e-4,1e1)
        plt.ylim(1e-1,1e10)
    plt.grid()
    plt.title(title)
    plt.legend()
    plt.ylabel('$\phi_U$ $(m^3/s^2)$')
    plt.xlabel('Frequency (Hz)')
    plt.savefig(fname)
    plt.close()
    return

# plot with the linear plt.plot() function
plotspec(freq, Uspec, 'linlin_Uspec.pdf', plotfunc=plt.plot, title='The naive approach', theory=False)
# Plot with a loglog approach with plt.loglog()
plotspec(freq, Uspec, 'loglog_Uspec.pdf', plotfunc=plt.loglog, title='A better approach', theory=True, set_bounds=True)

# This is a binning function to smooth the data (careful, depending on the
# data and number of bins it spits out some NaNs that you may want to clean
def classbin(x, y, bins_number=100, function=np.mean, xfunction=np.mean, logscale=True):
    """
    Separates x and y inputs into bins based on the x array.
    x and y do not have to be ordered.
    Parameters
    -----------
    x: np.array
        independent variable
    y: np.array
        dependent variable
    bins_number: int
        number of classes (or bins) desired
    function: callable
        funtion to be applied to both x and y-bins in order to smooth the data
    logscale: boolean
        whether or not to use a log-spaced scale to set the bins
    Returns
    -------
    np.array:
        x binned
    np.array:
        y binned
    """
    import warnings
    import numpy as np

    xmin=np.min(x)
    xmax=np.max(x)
    if logscale:
        #-----------
        # The following if statement gets rid of negative or zero values in the x array, since we are using log-scale
        if (x<=0).any():
            y=np.array([ yy for yy, xx in zip(y,x) if xx > 0 ])
            x=np.array([ el for el in x if el > 0])
            xmin=np.min(x)
            xmax=np.max(x)
        #-----------
        bins=np.logspace(np.log(xmin), np.log(xmax), bins_number+1, base=np.e)
    else:
        bins=np.linspace(xmin, xmax, bins_number+1)
    xsm = np.zeros(bins_number)
    ysm = np.zeros(bins_number)

    #-----------
    # The following process is what actually bins the data using numpy
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        for i in range(bins_number):
            if i == bins_number - 1:
                sel = bins[i] <= x
            else:
                sel = (bins[i] <= x) & (x < bins[i+1])
            xsm[i] = xfunction(x[sel])
            ysm[i] = function(y[sel])
    #-----------
    return xsm, ysm

# Uses binning to smooth the array for better visualization
binfreq, binUspec = classbin(freq, Uspec, logscale=True)
binfreq, binUerr = classbin(freq, Uspec, logscale=True, function=np.std)

# Cleaning up the NaNs that the output may have
binfreq=binfreq[np.isfinite(binfreq)]
binUerr=binUerr[np.isfinite(binUspec)]
binUspec=binUspec[np.isfinite(binUspec)]

# Replot everything in a loglog graph but with smoothed out data
plotspec(binfreq, binUspec, 'loglog2_Uspec.pdf', plotfunc=plt.loglog, title='A cleaner approach', theory=True, set_bounds=True)

# Replot everything but adding errorbars to the smoothed data for completeness
plotspec(binfreq, binUspec, 'loglog3_Uspec.pdf', plotfunc=plt.loglog, title='Errorbars make it better', theory=True, set_bounds=True, errorbars=binUerr)

