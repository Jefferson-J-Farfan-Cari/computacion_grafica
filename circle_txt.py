import cv2

image = cv2.imread("dog.png")

x, y = image.shape[:2]

imageWC = cv2.circle(image, (int(x / 2), int((y / 2) - 120)), 100, (0, 0, 255), 5)
imageWT = cv2.putText(imageWC, "DOG", (int(x / 2.5), 120), 0, 5, (0, 0, 255), 5)

cv2.imwrite('ImageWCT.png', imageWT)

cv2.imshow('Image With Circle And Text', imageWT)
cv2.waitKey(0)
