import cv2
import numpy as np


def draw(event, x, y, label, parameters):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image, (x, y), 50, (255, 0, 0), -1)
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(image, (x, y), (x + 50, y + 50), (255, 0, 0), -1)
    if event == cv2.EVENT_MBUTTONDOWN:
        cv2.rectangle(image, (x, y), (x + 50, y), (255, 0, 0), -1)

cv2.namedWindow(winname= 'Drawing')
cv2.setMouseCallback('Drawing', draw)

image = np.zeros((500, 500, 3), np.int8)

while True:
    cv2.imshow('Drawing', image)
    if cv2.waitKey(10) & 0xFF == 27:
        cv2.imwrite('drawed.png', image)
        break

cv2.destroyAllWindows()
