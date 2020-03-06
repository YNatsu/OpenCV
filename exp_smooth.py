from cv2 import *
import matplotlib.pyplot as plt

img = imread('resource/a.jpg', flags=1)


img = cvtColor(img, COLOR_BGR2RGB)
img_blur = blur(img, (5, 5))  # 均值滤波

img_t = boxFilter(img, -1, (3,3), normalize=True)
img_f = boxFilter(img, -1, (3,3), normalize=False)

# GaussianBlur 高斯滤波
# medianBlur 中值滤波

plt.subplot(2, 2, 1)
plt.imshow(img)
plt.title('Original image')
plt.subplot(2, 2, 2)
plt.imshow(img_blur)
plt.title('Blur')

plt.subplot(2, 2, 3)
plt.imshow(img_t)
plt.title('boxFilter true')

plt.subplot(2, 2, 4)
plt.imshow(img_f)
plt.title('BboxFilter false')

plt.show()