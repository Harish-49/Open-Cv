# Using Drawing Functions


# Importing Libraries and Packages
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Creating Blank image to draw
blank = np.zeros((500, 500, 3))
cv2.imshow("blank", blank)

# rectangle
cv2.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 250, 0), thickness=-1)
#cv2.imshow("rectangle", blank)

# Circle
cv2.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 50, (0, 0, 250), thickness=-1)
#cv2.imshow("circle", blank)

# Line
cv2.line(blank, (200, 200), (400, 400), (250, 0, 0), thickness=5)
#cv2.imshow("line", blank)

# Adding Text
cv2.putText(blank, "HelloWorld", (140, 430), cv2.FONT_HERSHEY_COMPLEX, 2.0, (255, 255, 255), 1)
cv2.imshow("Text", blank)

cv2.waitKey(0)