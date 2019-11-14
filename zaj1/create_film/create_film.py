import math

import cv2
import matplotlib.pyplot as plt
import numpy as np

max_frames = 1000
frames = []
bg = cv2.imread('../data/sky.jpeg')
width, height, colors = bg.shape

for fr in range(0, max_frames):
    x = int(width/2*(1+math.sin(fr)))
    y = int( height*fr*(1000-fr) -(fr**2)+1000*fr)   #fr*(-a*fr + b ) -> a*1000 - b = 0 -> b/a =1000
    frame = np.copy(bg)
    cv2.circle(frame,(x,y),10,(255,0,0))
    frames.append(frame)

out = cv2.VideoWriter('../out/project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, (width,height))
for i in range(len(frames)):
    out.write(frames[i])
    print("frame:",i)
out.release()

