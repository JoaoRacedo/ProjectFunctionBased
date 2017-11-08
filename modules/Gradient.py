# -*- coding: utf-8 -*-
import skimage.filters
import numpy as np


__doc__ = """\
Gradient
========

Compute the image gradient with the desired transformation.
the posibles transformations are:
    - Sobel : Find the edge magnitude using the Sobel transfor.
    - CentralDifference : dI/dx = (I(x+1) - I(x-1))/2
"""


def Sobel(src):
    return skimage.filters.sobel(src)


def CentralDifference(src):
    gradientx, gradienty = np.gradient(src)
    return np.sqrt(gradientx**2 + gradienty**2)


def GradientChoice(src, choice):
    if choice == 0:
        return Sobel(src)
    elif choice == 1:
        return CentralDifference(src)
