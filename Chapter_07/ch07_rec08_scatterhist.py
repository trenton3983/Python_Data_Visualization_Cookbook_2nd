import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable


def scatterhist(x, y, figsize=(8,8)):
    """
    Create simple scatter & histograms of data x, y inside given plot

    @param figsize: Figure size to create figure
    @type figsize: Tuple of two floats representing size in inches

    @param x: X axis data set
    @type x: np.array

    @param y: Y axis data set
    @type y: np.array
    """
    _, scatter_axes = plt.subplots(figsize=figsize)

    # the scatter plot:
    scatter_axes.scatter(x, y, alpha=0.5)
    scatter_axes.set_aspect(1.)

    divider = make_axes_locatable(scatter_axes)
    axes_hist_x = divider.append_axes(position="top", sharex=scatter_axes,
                                      size=1, pad=0.1)
    axes_hist_y = divider.append_axes(position="right", sharey=scatter_axes,
                                      size=1, pad=0.1)

    # compute bins accordingly
    binwidth = 0.25

    # global max value in both data sets
    xymax = np.max([np.max(np.fabs(x)), np.max(np.fabs(y))])
    # number of bins
    bincap = int(xymax / binwidth) * binwidth

    bins = np.arange(-bincap, bincap, binwidth)
    nx, binsx, _ = axes_hist_x.hist(x, bins=bins, histtype='stepfilled',
                     orientation='vertical')
    ny, binsy, _ = axes_hist_y.hist(y, bins=bins, histtype='stepfilled',
                     orientation='horizontal')

    tickstep = 50
    ticksmax = np.max([np.max(nx), np.max(ny)])
    xyticks = np.arange(0, ticksmax + tickstep, tickstep)

    # hide x and y ticklabels on histograms
    for tl in axes_hist_x.get_xticklabels():
        tl.set_visible(False)
    axes_hist_x.set_yticks(xyticks)

    for tl in axes_hist_y.get_yticklabels():
        tl.set_visible(False)
    axes_hist_y.set_xticks(xyticks)

    plt.show()


if __name__ == '__main__':
    # daily search trend for keyword 'flowers' for a year
    d = [
 1.04, 1.04, 1.16, 1.22, 1.46, 2.34, 1.16, 1.12, 1.24, 1.30, 1.44, 1.22, 1.26,
 1.34, 1.26, 1.40, 1.52, 2.56, 1.36, 1.30, 1.20, 1.12, 1.12, 1.12, 1.06, 1.06,
 1.00, 1.02, 1.04, 1.02, 1.06, 1.02, 1.04, 0.98, 0.98, 0.98, 1.00, 1.02, 1.02,
 1.00, 1.02, 0.96, 0.94, 0.94, 0.94, 0.96, 0.86, 0.92, 0.98, 1.08, 1.04, 0.74,
 0.98, 1.02, 1.02, 1.12, 1.34, 2.02, 1.68, 1.12, 1.38, 1.14, 1.16, 1.22, 1.10,
 1.14, 1.16, 1.28, 1.44, 2.58, 1.30, 1.20, 1.16, 1.06, 1.06, 1.08, 1.00, 1.00,
 0.92, 1.00, 1.02, 1.00, 1.06, 1.10, 1.14, 1.08, 1.00, 1.04, 1.10, 1.06, 1.06,
 1.06, 1.02, 1.04, 0.96, 0.96, 0.96, 0.92, 0.84, 0.88, 0.90, 1.00, 1.08, 0.80,
 0.90, 0.98, 1.00, 1.10, 1.24, 1.66, 1.94, 1.02, 1.06, 1.08, 1.10, 1.30, 1.10,
 1.12, 1.20, 1.16, 1.26, 1.42, 2.18, 1.26, 1.06, 1.00, 1.04, 1.00, 0.98, 0.94,
 0.88, 0.98, 0.96, 0.92, 0.94, 0.96, 0.96, 0.94, 0.90, 0.92, 0.96, 0.96, 0.96,
 0.98, 0.90, 0.90, 0.88, 0.88, 0.88, 0.90, 0.78, 0.84, 0.86, 0.92, 1.00, 0.68,
 0.82, 0.90, 0.88, 0.98, 1.08, 1.36, 2.04, 0.98, 0.96, 1.02, 1.20, 0.98, 1.00,
 1.08, 0.98, 1.02, 1.14, 1.28, 2.04, 1.16, 1.04, 0.96, 0.98, 0.92, 0.86, 0.88,
 0.82, 0.92, 0.90, 0.86, 0.84, 0.86, 0.90, 0.84, 0.82, 0.82, 0.86, 0.86, 0.84,
 0.84, 0.82, 0.80, 0.78, 0.78, 0.76, 0.74, 0.68, 0.74, 0.80, 0.80, 0.90, 0.60,
 0.72, 0.80, 0.82, 0.86, 0.94, 1.24, 1.92, 0.92, 1.12, 0.90, 0.90, 0.94, 0.90,
 0.90, 0.94, 0.98, 1.08, 1.24, 2.04, 1.04, 0.94, 0.86, 0.86, 0.86, 0.82, 0.84,
 0.76, 0.80, 0.80, 0.80, 0.78, 0.80, 0.82, 0.76, 0.76, 0.76, 0.76, 0.78, 0.78,
 0.76, 0.76, 0.72, 0.74, 0.70, 0.68, 0.72, 0.70, 0.64, 0.70, 0.72, 0.74, 0.64,
 0.62, 0.74, 0.80, 0.82, 0.88, 1.02, 1.66, 0.94, 0.94, 0.96, 1.00, 1.16, 1.02,
 1.04, 1.06, 1.02, 1.10, 1.22, 1.94, 1.18, 1.12, 1.06, 1.06, 1.04, 1.02, 0.94,
 0.94, 0.98, 0.96, 0.96, 0.98, 1.00, 0.96, 0.92, 0.90, 0.86, 0.82, 0.90, 0.84,
 0.84, 0.82, 0.80, 0.80, 0.76, 0.80, 0.82, 0.80, 0.72, 0.72, 0.76, 0.80, 0.76,
 0.70, 0.74, 0.82, 0.84, 0.88, 0.98, 1.44, 0.96, 0.88, 0.92, 1.08, 0.90, 0.92,
 0.96, 0.94, 1.04, 1.08, 1.14, 1.66, 1.08, 0.96, 0.90, 0.86, 0.84, 0.86, 0.82,
 0.84, 0.82, 0.84, 0.84, 0.84, 0.84, 0.82, 0.86, 0.82, 0.82, 0.86, 0.90, 0.84,
 0.82, 0.78, 0.80, 0.78, 0.74, 0.78, 0.76, 0.76, 0.70, 0.72, 0.76, 0.72, 0.70,
 0.64]

    # Now let's generate random data for the same period
    d1 = np.random.random(365)
    assert len(d) == len(d1)

    # try with the random data
#     d = np.random.randn(1000)
#     d1 = np.random.randn(1000)

    scatterhist(d, d1)
