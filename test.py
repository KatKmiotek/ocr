import cv2
import pytesseract
from PIL import Image
import numpy as np
import imutils

img = cv2.imread('images/note.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('image', gray)
#cv2.waitKey(0)

grayed = cv2.bilateralFilter(gray, 11, 17, 17)
#cv2.imshow('image greyed', grayed)
#cv2.waitKey(0)
blurred= cv2.medianBlur(grayed,5)
#cv2.imshow('image blurred', blurred)
#cv2.waitKey(0)
rotated = cv2.rotate(blurred, cv2.ROTATE_90_COUNTERCLOCKWISE)

custom_config= r'--oem 3 --psm 6'

original = pytesseract.image_to_string(rotated, config=custom_config, lang='eng')

print (original)