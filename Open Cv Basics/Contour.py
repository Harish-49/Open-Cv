# Contours and Edges

# Importing Libraries and Packages
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reading Input
img = cv2.imread("Resources\Homes.jfif")
#cv2.imshow("Image",img)

# Creating Blank image to draw the Contours
blank = np.zeros(img.shape, dtype='uint8')

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Grey", grey)

blur = cv2.GaussianBlur(grey, (5, 5), cv2.BORDER_DEFAULT)
# cv2.imshow("blur", blur)

canny = cv2.Canny(blur, 100, 50)
# cv2.imshow("canny", canny)

ret,thresh = cv2.threshold(grey, 100, 300, cv2.THRESH_BINARY)
# [cv2.THRESH_BINARY_INV , cv2.ADAPTIVE_THRESH_MEAN] --> Also be used.
cv2.imshow("thresh", thresh)

contours, hierarchies = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# Printing Contours Length
print(len(contours))

# drawing Contours in Blank image
cv2.drawContours(blank, contours, -1, (0, 255, 0), 1)
cv2.imshow("Contour", blank)

cv2.waitKey(0)