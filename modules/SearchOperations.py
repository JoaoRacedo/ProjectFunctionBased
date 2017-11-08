# -*- coding: utf-8 -*-
import numpy as np
import skimage.measure


__doc__ = """\
SearchOperations
================

Search indexes or values in lists according to the properties given.
"""


def Find(properties, choice):
    if choice == 0:
        Index_area = [i for i, x in enumerate(properties[0]) if x >= 100]
        Index_solidity = [i for i, x in enumerate(properties[1])if x <= 0.9]
        return sorted(list(set(Index_area).intersection(Index_solidity)))
    elif choice == 1:
        Index_area = [i for i, x in enumerate(properties[0]) if x < 10]
        return Index_area


def IsMember(src1, src2):
    temp1 = np.copy(src1)
    for x in range(0, temp1.shape[0]):
        for y in range(0, temp1.shape[1]):
            temp1[x][y] = IsFound(temp1[x][y], src2)
    return temp1


def IsFound(src1, src2):
    if(src1 in src2):
        return True
    else:
        return False


def FindContours(src, level):
    return skimage.measure.find_contours(src, level)
