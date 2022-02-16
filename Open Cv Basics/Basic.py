# Basic Operations with images in Computer Visions:

# Importing Libraries and Packages
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reading Input
img = cv2.imread("Resources\Homes.jfif")

# Displaying Output
cv2.imshow("Homes", img)


# Grey scale
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# colors = [RGB,LAB,HSV,[HSV_BGR-LAB_BGR]] --> These type of colors also can be used instead of GRAY in COLOR_BGR2GRAY.
cv2.imshow("Grey", grey)


# blur
blur = cv2.GaussianBlur(grey, (5, 5), cv2.BORDER_DEFAULT)
cv2.imshow("Blur", blur)

# Edge cascade
canny = cv2.Canny(blur, 150, 150)
cv2.imshow("Canny", canny)

# Dilated
dilated = cv2.dilate(canny, (3, 3), iterations=1)
cv2.imshow("Dilated", dilated)

# Eroding
erode = cv2.erode(dilated, (3, 3), iterations=1)
cv2.imshow("Erode", erode)

# Resize
resize = cv2.resize(img, (350, 500), interpolation=cv2.INTER_CUBIC)
cv2.imshow("Resize", resize)

# Cropping
crop = img[100:200, 20:350]
cv2.imshow("Crop", crop)

# Translating
def translate(img, x, y):
   transMat = np.float32([[1, 0, x], [0, 1, y]])
   dimensions = (img.shape[1], img.shape[0])
   return cv2.warpAffine(img, transMat, dimensions)

translate = translate(img, 100, 200)
cv2.imshow("Translated", translate)

# Rotate
def rotate(img, angle, rotpoint=None):
   width, height = img.shape[:2]
   if rotpoint==None:
       rotpoint = (width//2, height//2)
   rotMat = cv2.getRotationMatrix2D(rotpoint, angle, 1.0)
   dimensions = (width, height)
   return cv2.warpAffine(img, rotMat, dimensions)

rotate = rotate(img, 50)
cv2.imshow("Rotate", rotate)

# Flipping
flip = cv2.flip(img, -1)
cv2.imshow("Flip", flip)


cv2.waitKey(0)
cv2.destroyAllWindows()