import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('resource/a.jpg', flags=1)  # BGR
print(img1.shape)

img0 = cv2.imread('resource/a.jpg', flags=0)  # GRAY
print(img0.shape)

img_1 = cv2.imread('resource/a.jpg', flags=-1)  # BGR + α
print(img_1.shape)

cv2.line(img1, (0, 0), (2400, 1352), (255, 0, 0), 3)
cv2.rectangle(img1, (600, 325), (1000, 600), (0, 255, 0), 3)
cv2.circle(img1, (1700, 500), 150, (0, 0, 255), 3)
cv2.putText(img1, 'Sukida', (2000, 800), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 3)

# cv2.imshow(winname='Mashiro', mat=img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
plt.imshow(img1)
plt.title(label='Mashiro')
plt.show()
