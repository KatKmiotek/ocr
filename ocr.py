import cv2
import pytesseract
from PIL import Image
image = cv2.imread('images/note.png', 0)
def preprocess(image)
    #cv2.imread('images/note.png', 0)
    cv2.rotate(imgage, cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.cvtColor(img_rotated, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 180, 255, cv2.THRESH_BINARY)
image_final = cv2.bitwise_and(img2gray, img2gray, mask=mask)
ret, new_img = cv2.threshold(image_final, 180, 255, cv2.THRESH_BINARY)

