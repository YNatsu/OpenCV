from cv2 import *
import matplotlib.pyplot as plt

img_gray = imread('resource/a.jpg', flags=0)


ret, thresh1 = threshold(img_gray, 127, 255, THRESH_BINARY)
ret, thresh2 = threshold(img_gray, 127, 255, THRESH_BINARY_INV)
ret, thresh3 = threshold(img_gray, 127, 255, THRESH_TRUNC)
ret, thresh4 = threshold(img_gray, 127, 255, THRESH_TOZERO)
ret, thresh5= threshold(img_gray, 127, 255, THRESH_TOZERO_INV)


images = [
    img_gray, thresh1, thresh2, thresh3, thresh4, thresh5
]

titles = [
    'Original image', 'THRESH_BINARY', 'THRESH_BINARY_INV', 
    'THRESH_TRUNC', 'THRESH_TOZERO', 'THRESH_TOZERO_INV'
]

for i in range(6):
    plt.subplot(2, 3, i +1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    
plt.show()