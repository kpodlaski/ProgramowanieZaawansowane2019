import struct

import cv2
import numpy as np
import matplotlib.pyplot as plt

def read_mnist_labels(file_path):
    labels = None
    #open file
    file = open(file_path,"rb")
    #magic number
    file.read(4)
    size = struct.unpack(">i",file.read(4))[0]
    labels = []
    for i in range(size):
        label = struct.unpack(">B",file.read(1))
        labels.append(label)
    file.close()
    return labels


def read_mnist_images(file_path):
    images = None
    file = open(file_path, "rb")
    # magic number
    file.read(4)
    size, rows, cols = struct.unpack(">iii", file.read(12))
    print (size, rows, cols)
    images = []
    for i in range(size):
        image = []
        for x in range(rows*cols):
            pixel = struct.unpack(">B", file.read(1))
            image.append(pixel)
        images.append(np.array(image, dtype='float'))
    file.close()
    return np.array(images), rows, cols


test_labels = read_mnist_labels("../data/mnist/t10k-labels.idx1-ubyte")
train_labels = read_mnist_labels("../data/mnist/train-labels.idx1-ubyte")
print(len(test_labels))
print(len(train_labels))
images, rows, cols = read_mnist_images("../data/mnist/t10k-images.idx3-ubyte")
print(images.shape)
line = ""
for x in range(len(images[3])):
    line+=str(images[3][x][0])
    if x%cols == 0:
        print(line)
        line=""

plt.imshow(images[3].reshape((rows,cols)), cmap='gray')
print(train_labels())
#cv2.imshow(np.real(images[3].reshape(rows,cols)))