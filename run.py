# -*- coding: utf-8 -*-

import modules.RdData as RdData
import modules.ShowData as ShowData
import modules.Adjust as Adjust
import modules.Gradient as Gradient
import modules.Morphology as Morphology
import modules.Binarization as Binarization
import modules.BasicOperations as BasicOperations
import modules.Watershed as Watershed


Image = RdData.ReadData('Snap-16290_Rhodamine_1.tif', 0)
Adjustment = Adjust.Contrast(Image, 0)
Gradient = Gradient.GradientChoice(Adjustment, 1)
Erosion = Morphology.Erode(Adjustment)
Opening_by_Reconstruction = Adjust.Reconstruction(Erosion, Adjustment)
Dilation = Morphology.Dilation(Opening_by_Reconstruction)
Dilation = Adjust.Invert(Dilation)
Opening_by_Reconstruction = Adjust.Invert(Opening_by_Reconstruction)
OC_by_Reconstruction = Adjust.Reconstruction(Dilation,
                                             Opening_by_Reconstruction)
OC_by_Reconstruction = Adjust.Invert(OC_by_Reconstruction)
ForegroundImage = Morphology.Local_maxima(OC_by_Reconstruction)
Foreground_Removed = Morphology.Remove_small_objects(ForegroundImage, 5)
Thershold = Binarization.OtsuMethod(OC_by_Reconstruction)
Binary_Image = Binarization.Image2Binary(OC_by_Reconstruction, Thershold)
Sum_FB = BasicOperations.AddImages(Foreground_Removed, Binary_Image)
Watershed = Watershed.Watershed(Sum_FB, 0)
