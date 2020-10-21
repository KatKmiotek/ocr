import cv2
import pytesseract
from PIL import Image
import numpy as np
import imutils

img = cv2.imread('images/hellow.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('image', gray)
#cv2.waitKey(0)

img_blur = cv2.GaussianBlur(gray,(5,5),0)
#cv2.imwrite(r"./images/result/img_blur1.png", img_blur)

grayed = cv2.bilateralFilter(img_blur, 11, 17, 17)
#cv2.imwrite(r"./images/result/img_grayed1.png",grayed)

#cv2.imshow('tres', img_blur)
#cv2.waitKey(0)
#cv2.imshow('image greyed', grayed)
#cv2.waitKey(0)
#norm = cv2.normalize(grayed, None, alpha=0, beta=1, norm_type= cv2.NORM_MINMAX, dtype=cv2.CV_32F)

adap_thresh = cv2.adaptiveThreshold(grayed, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 4)
#thresh = cv2.threshold(grayed, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
#cv2.imwrite(r"./images/result/img_threshold1.png",tres)
#cv2.imshow('tres', tres)
#cv2.waitKey(0)

rotated = cv2.rotate(adap_thresh, cv2.ROTATE_90_COUNTERCLOCKWISE)

custom_config= r'--oem 3 --psm 4'

original = pytesseract.image_to_string(rotated, config=custom_config)

print (original)