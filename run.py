# -*- coding: utf-8 -*-

import modules.RdData as RdData
import modules.ShowData as ShowData
import modules.Adjust as Adjust
import modules.Gradient as Gradient
import modules.Morphology as Morphology
import modules.Binarization as Binarization
import modules.BasicOperations as BasicOperations
import modules.Watershed as Watershed
import modules.SearchOperations as SearchOperations
import modules.Properties as Properties
import numpy as np


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
Watershed_Original = Watershed.Watershed(Sum_FB, 0)
#  --Merge--
Propers = Properties.RegionProps(Watershed_Original, 0)
FindIndex = SearchOperations.Find(Propers, 0)
Adjustment_Merge = Binarization.TransformImage(Watershed_Original, Adjustment)
Thershold_Merge = Binarization.OtsuMethod(Adjustment_Merge)
Binary_Merge = Binarization.Image2Binary(Adjustment_Merge, Thershold_Merge)
WFI_Members = SearchOperations.IsMember(Watershed_Original, FindIndex)
New_Adjustment = BasicOperations.MultImages(Adjustment, WFI_Members)
Image_Merge = BasicOperations.SubsImages(Binary_Merge, WFI_Members)
Thershold_NewAdjust = Binarization.OtsuMethod(New_Adjustment)
Binary_NewAdjust = Binarization.Image2Binary(New_Adjustment,
                                             Thershold_NewAdjust)
HF_Binary = Morphology.Fill_holes(Binary_NewAdjust)
Watershed_Merge = Watershed.Watershed(HF_Binary, 1)
WatershedMerge_Copy = np.copy(Watershed_Merge)
WatershedMerge_Copy = Binarization.TransformImage(Watershed_Merge,
                                                  WatershedMerge_Copy)
Thershold_WMergeCopy = Binarization.OtsuMethod(WatershedMerge_Copy)
Binary_WMergeCopy = Binarization.Image2Binary(WatershedMerge_Copy,
                                              Thershold_WMergeCopy)
Remove_BWMC = Morphology.Remove_small_objects(Binary_WMergeCopy, 10)
Propers_Merge = Properties.RegionProps(Remove_BWMC.astype(np.uint8), 1)  # HERE
FindIndex_Merge = SearchOperations.Find(Propers_Merge, 1)
RemoveIndex_Members = SearchOperations.IsMember(Remove_BWMC.astype(np.uint8),
                                                FindIndex_Merge)
Closing_Merge = Morphology.Closing(RemoveIndex_Members, 3)
Sum_CR = BasicOperations.AddImages(Closing_Merge, Remove_BWMC)
Sum_CRIM = BasicOperations.AddImages(Sum_CR, Image_Merge)
Contours = SearchOperations.FindContours(Sum_CRIM, 0.5)
ShowData.ShowBoundaries(Contours)
