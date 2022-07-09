import cv2

image = cv2.imread('dog.png')

gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grises', gris)
cv2.waitKey()
cv2.destroyAllWindows()
