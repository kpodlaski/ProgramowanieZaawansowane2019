import math
import numpy as np
import cv2

img = cv2.imread("../data/clouds.png")
print("Shape of the picture",img.shape)
print(img[0,0,0],img[0,0,1], img[0,0,2])