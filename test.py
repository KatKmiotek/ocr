import cv2
import pytesseract
from PIL import Image
import numpy as np
import imutils

img = cv2.imread('images/hello.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('image', gray)
#cv2.waitKey(0)

img_blur = cv2.GaussianBlur(gray,(5,5),0)
cv2.imwrite(r"./images/result/img_blur.png", img_blur)

grayed = cv2.bilateralFilter(img_blur, 11, 17, 17)
cv2.imwrite(r"./images/result/img_grayed.png",grayed)

#cv2.imshow('tres', img_blur)
#cv2.waitKey(0)
#cv2.imshow('image greyed', grayed)
#cv2.waitKey(0)


tres = cv2.threshold(grayed, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
cv2.imwrite(r"./images/result/img_threshold.png",tres)
#cv2.imshow('tres', tres)
#cv2.waitKey(0)

rotated = cv2.rotate(tres, cv2.ROTATE_90_COUNTERCLOCKWISE)

custom_config= r'--oem 3 --psm 6'

original = pytesseract.image_to_string(rotated, config=custom_config)

print (original)