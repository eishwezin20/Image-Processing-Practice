#import required packages
import cv2
import numpy as np
#Read image
image = cv2.imread("????.jpg")        #file name

#Create a dummy image that stores different contrast and brightness
new_image = np.zeros(image.shape, image.dtype)
#Brightness and contrast parameters
contrast = 3.0
bright = 2
#Change the contrast and brightness
for y in range(image.shape[0]):
  for x in range(image.shape[1]):
    for c in range(image.shape[2]):
       new_image[y,x,c] = np.clip(contrast*image[y,x,c] + bright, 0, 255)

figure(0)
io.imshow(image)
figure(1)
io.imshow(new_image)