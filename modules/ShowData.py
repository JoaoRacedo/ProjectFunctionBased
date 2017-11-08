# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import skimage.color


__doc__ = """\
ShowData
========

Show data, the data is a matrix that can have 2 or 3 dimensions
"""


def ShowData(src):
    plt.imshow(src, cmap='gray', interpolation='bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()


def Label2RGB(src):
    LabelImage = skimage.color.label2rgb(src)
    ShowData(LabelImage)
