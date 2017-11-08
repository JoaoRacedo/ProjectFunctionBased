# -*- coding: utf-8 -*-
import cv2
import numpy as np


__doc__ = """\
ReadData
========

Load data from desired path, the data can be either a image (format .tiff)...
...or a matrix (.csv)"""


def ReadData(path, choice):
    if choice == 0:  # data in image format
        return cv2.imread(path, 0)
    elif choice == 1:  # data in matrix format
        return np.genfromtxt(path, delimiter=',')
