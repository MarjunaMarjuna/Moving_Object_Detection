import cv2

import imutils

img = cv2.imread('initialimage.jpg')
resizedImg = imutils.resize(img, width=50)

cv2.imwrite('resizedImage.jpg', resizedImg)
