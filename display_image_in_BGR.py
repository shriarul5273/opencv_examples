#USAGE 
	#python display_image_in_BGR.py  --image images/opencv_logo.png --output combined.jpg
	#OR
	#python display_image_in_BGR.py  --image images/opencv_logo.png 
#Initialize all the required packages 
import cv2 #opencv
import numpy as np
import argparse #argument from comand line

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True,help='Path to the image')
ap.add_argument('-o','--output',required=False,help='output file name')
args = vars(ap.parse_args())

# load the image,it of the form numpy array
image = cv2.imread(args['image'])

#print the shape of the image.
print(image.shape)
(height,width,channel) = image.shape

# split the image into different channels 
(B,G,R) = cv2.split(image)

#create the a numpy arry with the size of the original image with out channel
zeros = np.zeros((height,width),np.uint8)

#merge the zero image chanel with all BGR channels individually to form all BGR images 
Blue = cv2.merge([B,zeros,zeros])
Green = cv2.merge([zeros,G,zeros])
Red = cv2.merge([zeros,zeros,R])


#create the a numpy arry with the twice size of the original image to merge all the images
Big_Image = np.ones((2*height,2*width,channel),np.uint8)

#print the size of Big_image 
print(Big_Image.shape)

#using numpy slicing to merge all into one 
Big_Image[:height,:width,:] = image
Big_Image[:height,width:,:] = Blue
Big_Image[height:,:width,:] = Green
Big_Image[height:,width:,:] = Red

#save the image with output file name
if not(args['output'] == None):
	cv2.imwrite('{}'.format(args['output']),Big_Image)
else:
	cv2.imwrite('combined.jpg',Big_Image)

#dispaly all the images 
cv2.imshow('Big_Image',Big_Image)
cv2.imshow('Oringinal',image)

#wait until any key input 
cv2.waitKey(0)