# -*- coding: utf-8 -*-
import skimage.filters


__doc__ = """\
Binarization
========

Transform an image in binary with threshold. In this case using the Otsu Method
"""


def OtsuMethod(src):
    return skimage.filters.threshold_otsu(src)


def Image2Binary(src, threshold):
    return src > threshold
