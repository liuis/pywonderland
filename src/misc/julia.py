# -*- coding: utf-8 -*-

"""
~~~~~~~~~~~~~~~~~~~
A Julia Set Fractal 
~~~~~~~~~~~~~~~~~~~
"""

import numpy as np
import matplotlib.pyplot as plt
from numba import jit


MAXITERS = 500
RADIUS = 4
C = 0.7


@jit('float32(complex64, complex64)')
def escape(z, c):
    for i in range(1, MAXITERS):
        if z.real * z.real + z.imag * z.imag > RADIUS:
            break
        z = (z*z + c) / (z*z - c)
    return i


def main(xmin, xmax, ymin, ymax, width, height):
    y, x = np.ogrid[ymax: ymin: height*1j, xmin: xmax: width*1j]
    z = x + y*1j
    img = np.asarray(np.frompyfunc(escape, 2, 1)(z, C)).astype(np.float)
    img /= np.max(img)
    img = np.sin(img**2 * np.pi)
    fig = plt.figure(figsize=(width/100.0, height/100.0), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1], aspect=1)
    ax.axis('off')
    ax.imshow(img, cmap='hot')
    fig.savefig('julia.png')


if __name__ == '__main__':
    main(-2, 2, -1.6, 1.6, 600, 480)
