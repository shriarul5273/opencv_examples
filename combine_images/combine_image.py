#Initialize all the required package
import cv2
import numpy as np

#functions takes in two images and coimbines them in the width and retuens the combined one.

def image_combine(original=0,second=0,third=0,fourth=0,number_of_images=0):

	if number_of_images == 4 :
		(h,w,c) = original.shape
		big_image = np.zeros((2*h,2*w,c),np.uint8)
		big_image[:h,:w,:] = original
		big_image[:h,w:,:] = second
		big_image[h:,:w,:] = third
		big_image[h:,w:,:] = fourth

		return big_image
	if number_of_images == 2:
		(h,w,c) = original.shape
		big_image = np.zeros((h,2*w,c),np.uint8)

		big_image[:,:w,:] = original
		big_image[:,w:,:] = second

		return big_image