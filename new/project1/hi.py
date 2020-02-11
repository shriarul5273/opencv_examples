import cv2
import imutils.paths as Path
import numpy as np

images = list(Path.list_images('images'))

ima = []

for image in images:
    im = cv2.imread(image)
    ima.append(im)
def combine_images(rows,coloums,shape,image):
    height = shape[0]//rows
    width = shape[1]//coloums
    imag = []
    for i in image :
        ji =cv2.resize(i,(height,width),interpolation=cv2.INTER_CUBIC)
        imag.append(ji)
    coloum_images = []
    image_no = 0
    for n,coloum in enumerate(range(coloums)):
        row_images = []
        kimag = []
        print(type(kimag))
        for q in range(image_no,image_no+rows,1):
            print(q)
            kimag.append(imag[q])
        for (i,k) in enumerate(kimag):
            if i == 0:
                row_images = np.hstack([k])
            else:
                row_images = np.hstack([row_images,k])
        if n ==0:
            coloum_images = np.vstack([row_images])
        else:
            coloum_images = np.vstack([coloum_images,row_images])
        image_no += rows
    return coloum_images



ko = combine_images(6,8,(800,800),ima)

print(ko.shape)
cv2.imshow('0',ko)
cv2.waitKey(0)
cv2.imwrite('s.png',ko)
