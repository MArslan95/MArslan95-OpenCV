import cv2
import numpy as np
import matplotlib.pyplot as plt
# in here we use imread to read the image and also provide the grayscale to
# image because it is easy to read the iange in gray scale
# we also use IMREAD_COLOR=1 IMGREAD_UNCHANGE=-1
img = cv2.imread("watch.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Image Here", img)
cv2.imwrite('watch.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([100, 100], [90, 100], 'b', linewidth=10)
plt.show()

# now we use pyplot to read and show the image

#img = cv2.imread('watch.jpg')
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# plt.imshow(gray)
#plt.title('my picture')
# plt.show()
