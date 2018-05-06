"""
Compute the Mandelbrot fractal
"""
import numpy as np
import matplotlib.pyplot as plt


def mandel(n: int, thresh: float=50.,
           xlims: np.ndarray=np.array([-2, 1]), nx: int=600,
           ylims: np.ndarray=np.array([-1.5, 1.5]), ny: int=600):
    """
    Creates a grid of numbers between xlims and ylims and computes the Mandelbrot
    fractal. The resulting binary mask is positive if the point belongs to the set.
    """

    # A grid of c-values
    x = np.linspace(xlims[0], xlims[1], nx)
    y = np.linspace(ylims[0], ylims[1], ny)

    c = x[:, np.newaxis] + 1j * y[np.newaxis, :]

    # Mandelbrot iteration
    z = c
    for j in range(n):
        z = z**2 + c

    mandelbrot_set = abs(z) < thresh

    return mandelbrot_set


if __name__ == '__main__':
    mandelbrot_set = mandel(50, nx=1500, ny=1500)
    fig, ax = plt.subplots()
    ax.imshow(mandelbrot_set.T, extent=[-2, 1, -1.5, 1.5], cmap='gray')
    fig.savefig('mandelbrot.png')
