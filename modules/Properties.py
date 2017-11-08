# -*- coding: utf-8 -*-
import skimage.measure

__doc__ = """\
Properties
==========

Measure properties of labeled image regions. The ones used are:
    - area : Number of pixels of region.
    - eccentricity : The eccentricity is the ratio of the focal distance
                    (distance between focal points) over the major axis length.
    - solidity : Ratio of pixels in the region to pixels of the convex hull
                 image.
    cache = False doesn't calculate the properties until you call them.
"""


def RegionProps(src, choice):
    regionprops = skimage.measure.regionprops(src, cache=False)
    if choice == 0:
        areas = [r.area for r in regionprops]
        solidities = [r.solidity for r in regionprops]
        _, NumObjects = skimage.measure.label(src, return_num=True)
        return areas, solidities, NumObjects
    elif choice == 1:
        areas = [r.area for r in regionprops]
        eccentricities = [r.eccentricity for r in regionprops]
        return areas, eccentricities
