from cv2 import *
import matplotlib.pyplot as plt

# 算子
# Sobel()
# Scharr()
# Laplacian()
img = imread('resource/a.jpg', flags=1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.subplot(2, 2, 1)
imgx = Sobel(img, -1, 1, 0, ksize=3)
imgx = convertScaleAbs(imgx)
plt.imshow(imgx)

plt.subplot(2, 2, 2)
imgy= Sobel(img, -1, 0, 1,ksize=3)
imgy = convertScaleAbs(imgy)
plt.imshow(imgy)


plt.subplot(2,2, 3)
plt.imshow(img)

plt.subplot(2, 2, 4)
imgxy = addWeighted(imgx, 0.5, imgy, 0.5, 0)
plt.imshow(imgxy)

plt.show()