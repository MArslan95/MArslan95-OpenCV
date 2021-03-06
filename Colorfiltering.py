import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([150, 150, 150])
    upper_red = np.array([180, 255, 150])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((15, 15), np.float32)/225
    smoothed = cv2.filter2D(res, -1, kernel)
    cv2.imshow('Frame', frame)
    #cv2.imshow('Mask', mask)
    cv2.imshow('Res', res)
    cv2.imshow('Smoothed', smoothed)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()
# We can't convert the single color into HSV color
# dark_red=np.uint8([[[12,22,121]]])
#dark_red=cv2.cvtColor(dark_red,cv2.COLOR_BGR2HSV )
