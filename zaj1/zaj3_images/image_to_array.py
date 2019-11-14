import math
import numpy as np
import cv2
import matplotlib.pyplot as plt

def transform(px,a,b):
  R = int(px[0])
  G = int(px[1])
  B = int(px[2])
  px[0] = R*a #min(R*a,255)
  px[1] = G*b
  px[2] = B*b
  # if (R*a>255):
  #     print(R*a, px[0])


def transform2(img,x,y,R_max,a_max, b_max):
    _x = img.shape[1]/2-x
    _y= img.shape[0]/2-y
    R = math.sqrt(_x**2+_y**2)
    factor = R/R_max
    transform(img[x][y],a_max*factor, b_max*factor)

img = cv2.imread("../data/parrot.jpeg")
print( type(img))
print(img.shape)
print(img[30,15])
#cv2.imshow("Obrazek",img)
#cv2.waitKey(0)
#TRANSFORMACJA
for x in range(0,img.shape[0]):
    for y in range (0, img.shape[1]):
      transform2(img,x,y,min(img.shape[1],img.shape[0])/2,1.3,.8)

cv2.imshow("Obrazek",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
plt.imshow(np.real(img))

