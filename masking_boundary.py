#USAGE 
	#python masking_boundary.py  --image images/opencv_logo.png --output masked_combined.jpg
	#OR
	#python masking_boundary.py  --image images/opencv_logo.png 
#Initialize all the required package
import cv2
import numpy as np
import argparse
from combine_images import combine_image2x2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True,help='Path to the image')
ap.add_argument('-o','--output',required=False,help='output file name')
args = vars(ap.parse_args())

# load the image,it of the form numpy array and convart to grascale
image = cv2.imread(args['image'])
imag = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#kernel of 5x5 for GaussianBlur and apply it the image
kernel = np.ones((5,5),np.uint8)/25
blured = cv2.GaussianBlur(imag,(15,15),2)

#erode the blured image to make the pixel move from original positon
erodation = cv2.erode(blured,kernel,iterations=1)

#apply OTSU threshold on the grayscale image
_,threshold = cv2.threshold(erodation,0,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
#mask it with the original
masked = cv2.bitwise_and(image,image,mask = threshold)

#combine_image2x2.image_combine takes 2 images and returns them as combined one
output_image = combine_image2x2.image_combine(image,masked)

cv2.imshow('Output image',output_image)

#save the image with output file name
if not(args['output'] == None):
	cv2.imwrite('{}'.format(args['output']),output_image)
else:
	cv2.imwrite('masked_combined.jpg',output_image)

cv2.waitKey(0)

