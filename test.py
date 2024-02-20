import cv2
import numpy
import matplotlib.pyplot as plt

img_1 = cv2.imread('images/test/resize_000.png', cv2.IMREAD_GRAYSCALE)
img_2 = cv2.imread('images/test/resize_003.png', cv2.IMREAD_GRAYSCALE)
print("ok")

plt.figure()
plt.imshow(img_1)
plt.colorbar()
plt.grid(False)
plt.show()