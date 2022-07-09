import cv2
import numpy as np

image = cv2.imread('dog.png')

b, g, r = cv2.split(image)

blank = np.zeros(image.shape[:2], dtype='uint8')

red_and_green = cv2.merge([blank, g, r])

cv2.imwrite('Red_And_Green.png', red_and_green)

cv2.imshow('Red And Green', red_and_green)
cv2.waitKey()
cv2.destroyAllWindows()

