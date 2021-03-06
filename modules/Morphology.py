# -*- coding: utf-8 -*-
import cv2
import skimage.morphology
from scipy import ndimage as ndi


__doc__ = """\
Morphology
==========

Morphological transformations are some simple operations based on the image
shape.

the posible transformations that can be done are:
    - Disk :
    - Square :
    - Erode :
    - Dilation :
    - Closing :
    - Local_maxima : Determine all local maxima of the image.
    - Remove_small_objects :
    - fill_holes :
"""


def Disk(kernel):
    if kernel < 0:
        print("Error, kernel can't be less than 0, using kernel = 0")
        return skimage.morphology.disk(0)
    else:
        return skimage.morphology.disk(kernel)


def Square(kernel):
    if kernel <= 0:
        print("Error, kernel can't be less or equal than 0, using kernel = 1")
        return skimage.morphology.square(1)
    else:
        return skimage.morphology.square(kernel)


def Erode(src, kernel=1):
    if kernel == 1:
        return cv2.erode(src, Disk(1))
    else:
        return cv2.erode(src, Disk(kernel))


def Dilation(src, kernel=1):
    if kernel == 1:
        return cv2.dilate(src, Disk(1))
    else:
        return cv2.dilate(src, Disk(kernel))


def Closing(src, kernel=1):
    if kernel == 1:
        return skimage.morphology.closing(src, Square(1))
    else:
        return skimage.morphology.closing(src, Square(kernel))


def Local_maxima(src):
    return skimage.morphology.local_maxima(src).astype(bool)


def Remove_small_objects(src, pixels):
    return skimage.morphology.remove_small_objects(src, pixels)


def Fill_holes(src1):
    return ndi.morphology.binary_fill_holes(src1)
