# Exploring RGB colors:

# Importing Libraries and Packages
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reading Input
img = cv2.imread("Resources\Homes.jfif")
blank = np.zeros(img.shape[:2], dtype='unit8')
grey = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# we can use such colors also = [RGB,LAB,HSV,[HSV_BGR-LAB_BGR]]
# But to plot use RGB
cv2.imshow("Grey", grey)
# plt.imshow(grey)
# plt.show()

# Separating Blue, Green and Red color.
b, g, r = cv2.split(img)
bl = cv2.merge([b, blank, blank])
gr = cv2.merge([blank, g, blank])
re = cv2.merge([blank, blank, r])
cv2.imshow("b", bl)
cv2.imshow("g", gr)
cv2.imshow("r", re)

# Combining all colors
merged = cv2.merge([b, g, r])
cv2.imshow("Merged", merged)

# Printing x and y coordinates
print(img.shape[1])
print(img.shape[0])
print(img.shape[:2])
print(b.shape)
print(g.shape)
print(r.shape)
cv2.waitKey(0)


