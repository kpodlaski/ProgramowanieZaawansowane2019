import cv2
import matplotlib.pyplot as plt
import numpy as np


film  =  cv2.VideoCapture("../data/Bouncing_Ball.mp4")
success = True
count =0
while success:
    success, frame = film.read()
    plt.imshow(np.real(frame))
    count+=1
print(count)
