import cv2
import pytesseract
from PIL import Image
import numpy as np
import imutils

img = cv2.imread('test.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17) 
blurred= cv2.medianBlur(gray,5)

#edged = cv2.Canny(blurred, 30, 200)

#cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#cnts = imutils.grab_contours(cnts)
#cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
#screenCnt = None

#mask = np.zeros(gray.shape,np.uint8)
#new_image = cv2.drawContours(mask,[screenCnt],0,255,-1,)
#new_image = cv2.bitwise_and(image,image,mask=mask)

original = pytesseract.image_to_string(blurred, config='')

print (original)