# -*- coding: utf-8 -*-
import skimage.exposure
import skimage.morphology
import skimage.util
import numpy as np


__doc__ = """\
Adjustment
========

Adjust image according to the desired contrast especified by the user.
the posibles contrast are:
    - rescale_intensity : Return image after stretching or shrinking its
                          intensity levels.
    - equalize_adapthist : Contrast Limited Adaptive Histogram Equalization
                           (CLAHE).
    - equalize_hist : histogram equalization.

for more information visit http://scikit-image.org/docs/dev/api/skimage.
                        exposure.html#skimage.exposure.rescale_intensity

Or can reconstruct an image in base of another with Reconstruction and invert
the values of the image with Invert

"""


def Contrast(src, choice):
        if choice == 0:  # rescale_intensity
            return skimage.exposure.rescale_intensity(src)
        elif choice == 1:  # equalize_adapthist
            return skimage.exposure.equalize_adapthist(src)
        elif choice == 2:  # equalize_hist
            return skimage.exposure.equalize_hist(src)


def Reconstruction(src1, src2):
    return skimage.morphology.reconstruction(src1, src2).astype(np.uint8)


def Invert(src):
    return skimage.util.invert(src)
