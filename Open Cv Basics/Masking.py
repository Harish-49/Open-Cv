# Exploring Masking Functions

# Importing Libraries and Packages
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reading Input
img = cv2.imread("Resources\Homes.jfif")

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("grey", grey)

# Laplacian
lap = cv2.Laplacian(grey, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow("Lap", lap)

# Sobel
sobelx = cv2.Sobel(grey, cv2.CV_64F, 1, 0)
cv2.imshow("sobelx", sobelx)

sobely = cv2.Sobel(grey, cv2.CV_64F, 0, 1)
cv2.imshow("sobely", sobely)

# Combining Sobel x and Sobel y images
com = cv2.bitwise_and(sobelx, sobely)
cv2.imshow("combined", com)

cv2.waitKey(0)