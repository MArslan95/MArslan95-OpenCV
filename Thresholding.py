import cv2
import numpy as np

image = cv2.imread('bookpage.jpg')
retval, threshold = cv2.threshold(image, 12, 255, cv2.THRESH_BINARY)
grayscaled = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
retval, threshold1 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(
    grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
retval1, otsu = cv2.threshold(grayscaled, 120, 255, cv2.THRESH_BINARY +
                              cv2.THRESH_OTSU)
cv2.imshow('Original', image)
cv2.imshow('Threshold Image', threshold)
cv2.imshow('Gray Saled Image', threshold1)
cv2.imshow('Gausian Image', gaus)
cv2.imshow('OTSU Image', otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()
