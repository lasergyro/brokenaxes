import matplotlib.pyplot as plt
from brokenaxes import brokenaxes
import numpy as np
from matplotlib.gridspec import GridSpec


def test_standard():
    fig = plt.figure(figsize=(5, 2))
    bax = brokenaxes(xlims=((0, .1), (.4, .7)), ylims=((-1, .7), (.79, 1)), hspace=.05)
    x = np.linspace(0, 1, 100)
    bax.plot(x, np.sin(10 * x), label='sin')
    bax.plot(x, np.cos(10 * x), label='cos')
    bax.legend(loc=3)
    bax.set_xlabel('time')
    bax.set_ylabel('value')


def test_subplots():
    sps1, sps2 = GridSpec(2, 1)

    bax = brokenaxes(xlims=((.1, .3), (.7, .8)), subplot_spec=sps1)
    x = np.linspace(0, 1, 100)
    bax.plot(x, np.sin(x * 30), ls=':', color='m')

    x = np.random.poisson(3, 1000)
    bax = brokenaxes(xlims=((0, 2.5), (3, 6)), subplot_spec=sps2)
    bax.hist(x, histtype='bar')
