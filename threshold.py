import cv2

image = cv2.imread('dog.png', 0)

_, binary = cv2.threshold(image, 210, 255, cv2.THRESH_BINARY)
cv2.imshow('Binary Threshold Image', binary)
cv2.waitKey()
cv2.destroyAllWindows()
