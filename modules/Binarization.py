# -*- coding: utf-8 -*-
import skimage.filters
import numpy as np


__doc__ = """\
Binarization
========

Transform an image in binary with threshold. In this case using the Otsu Method
"""


def OtsuMethod(src):
    return skimage.filters.threshold_otsu(src)


def Image2Binary(src, threshold):
    return src > threshold


def TransformImage(src1, src2):
    temp1 = np.copy(src1)
    temp2 = np.copy(src2)
    temp2[temp1 != 0] = 255
    return temp2
