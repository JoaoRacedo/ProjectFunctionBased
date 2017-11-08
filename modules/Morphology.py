# -*- coding: utf-8 -*-
import cv2
import skimage.morphology


__doc__ = """\
Morphology
==========

Morphological transformations are some simple operations based on the image
shape.

the posible transformations that can be done are:
    - Erode :
    - Dilation :
    - Disk :
    - Local_maxima : Determine all local maxima of the image.
    - Remove_small_objects :
"""


def Disk(kernel):
    if kernel < 0:
        print("Error, kernel can't be less than 0, using kernel = 0")
        return skimage.morphology.disk(0)
    else:
        return skimage.morphology.disk(kernel)


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


def Local_maxima(src):
    return skimage.morphology.local_maxima(src).astype(bool)


def Remove_small_objects(src, pixels):
    return skimage.morphology.remove_small_objects(src, pixels)
