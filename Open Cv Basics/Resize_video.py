# Resizing video


# Importing Libraries and Packages
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reading Input
video = cv2.VideoCapture("Resources\DC.ts")

# function to resize
def resize_video_scale(frame, scale=0.50):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv2.resize(frame, dimensions)


while True:
    isTrue, frame = video.read()
    frameresize = resize_video_scale(frame, scale=0.25)
    cv2.imshow("Original Video", frame)
    cv2.imshow("Resized Video",frameresize)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyWindow()


