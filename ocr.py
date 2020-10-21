import cv2 as cv
import numpy as np

img = cv.imread('hellow.png',0)


blur = cv.GaussianBlur(img,(5,5),0)
ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

rotated = cv2.rotate(th3, cv2.ROTATE_90_COUNTERCLOCKWISE)

custom_config= r'--oem 3 --psm 6'

original = pytesseract.image_to_string(rotated, config=custom_config)

print (original)