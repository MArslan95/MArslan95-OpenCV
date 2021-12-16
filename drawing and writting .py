import cv2
import numpy as np

image = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)
# line on an image use this command
cv2.line(image, (20, 20), (140, 140), (255, 255, 0), 15)
# Rectangle  on an image use this command
cv2.rectangle(image, (15, 20), (250, 150), (0, 255, 0), 15)
# Circle  on an image use this command
cv2.circle(image, (70, 70), (40), (0, 0, 255), -1)
# Polygon  on an image use this command and for tha we need to make and an array for points
pts = np.array([[50, 45], [40, 30], [70, 40], [50, 60]], np.int32)
# if we want to reshape the point
# pts=pts.reshape((-1,1,2))
cv2.polylines(image, [pts], True, (0, 255, 255), 5)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, "Open Cv Tuts!", (0, 130),
            font, 1, (200, 0, 0), 2, cv2.LINE_AA)
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
