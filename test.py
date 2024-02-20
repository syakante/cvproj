import cv2
import numpy as np
import matplotlib.pyplot as plt

img_1 = cv2.imread('images/test/resize_000.png', cv2.IMREAD_GRAYSCALE)
img_2 = cv2.imread('images/test/resize_003.png', cv2.IMREAD_GRAYSCALE)

# plt.figure()
# plt.imshow(img_2)
# plt.colorbar()
# plt.grid(False)
# plt.show()

low_threshold = 0 #first threshold for hysteresis procedure
ratio = 3 #second threshold for hystersis procedure
kernel_size = 3 #apertureSize for Sobel operator. Default = 3
#optional bool flag for whether to use L2 or L1 norm. Default = false

img_blur = cv2.blur(img_2, (3,3))
edges2 = cv2.Canny(img_2, low_threshold, low_threshold*ratio, kernel_size)
mask = edges2 != 0
dst = img_2 * (mask[:,:,].astype(img_2.dtype))
print("ok")
#cv2.imshow('', dst)
plt.figure()
plt.imshow(dst)
plt.colorbar()
plt.grid(False)
plt.show()
#next: hough transform, consider some other convolution that's an actual convolution and not itty bitty image resizing