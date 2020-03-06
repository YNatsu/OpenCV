from cv2 import *
import matplotlib.pyplot as plt
import numpy as np

img = imread('resource/a.jpg', flags=1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.subplot(2, 2, 1)
plt.imshow(img)

img = erode(img, np.ones(shape=[3, 3]), iterations=1)
plt.subplot(2, 2, 2)
plt.imshow(img)

img = erode(img, np.ones(shape=[3, 3]), iterations=3)
plt.subplot(2, 2, 3)
plt.imshow(img)

img = erode(img, np.ones(shape=[3, 3]), iterations=4)
plt.subplot(2, 2, 4)
plt.imshow(img)

plt.show()
