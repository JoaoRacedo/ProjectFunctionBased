# -*- coding: utf-8 -*-
from scipy import ndimage as ndi
import skimage.measure
import mahotas
import numpy as np
import modules.BasicOperations as BasicOperations

__doc__ = """\
Watershed
===============

Compute the transformation of the distance with two methods:
    - Euclidian
    - Chamfer
Seeded watershed.
"""


def Watershed(src, choice):
    if choice == 0:  # Euclidian
        distance = ndi.morphology.distance_transform_edt(src)
    elif choice == 1:  # Chamfer
        distance = ndi.morphology.distance_transform_cdt(src)
    distance_stretch = mahotas.stretch(distance)
    surface = distance_stretch.max() - distance_stretch
    footprint = np.ones((8, 8))
    peaks = mahotas.regmax(distance_stretch, footprint)
    markers, _ = mahotas.label(peaks, footprint)
    seeds, RigedLines = mahotas.cwatershed(surface, markers, return_lines=True)
    #  watershed_RL = Combine_Water_Rl(seeds, RigedLines) For checking purposes
    watershed = BasicOperations.MultImages(seeds, src)
    watershed = skimage.measure.label(watershed)
    return watershed


def Combine_Water_Rl(src1, src2):
    temp1 = np.copy(src1)
    temp2 = np.copy(src2)
    temp1[temp2 == True] = 0
    return temp1
