import cv2

image = cv2.imread('dog.png')

blue = image[:, :, 0]

cv2.imshow('Blue Channel', blue)
cv2.waitKey()
cv2.destroyAllWindows()
