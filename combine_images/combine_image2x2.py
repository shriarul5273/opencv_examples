#Initialize all the required package
import cv2
import numpy as np

#functions takes in two images and coimbines them in the width and retuens the combined one.

def image_combine(original,second):
	(h,w,c) = original.shape
	big_image = np.zeros((h,2*w,c),np.uint8)

	big_image[:,:w,:] = original
	big_image[:,w:,:] = second

	return big_image