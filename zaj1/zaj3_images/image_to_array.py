import cv2

img = cv2.imread("../data/parrot.png")
print( type(img))
print(img.shape)
print(img[30,15])

