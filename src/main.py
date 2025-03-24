import cv2
import numpy as np


def update_image(r, center):
    mask = np.zeros(shape=result.shape[:2], dtype=np.uint8)
    cv2.circle(mask, center, r, (255, 255, 255), -1)
    blurred_mask = cv2.GaussianBlur(mask, (0, 0), sigmaX=20)
    blurred_mask = cv2.cvtColor(blurred_mask,cv2.COLOR_GRAY2BGR)
    result[:] = image_b * (blurred_mask / 255) + result * (1 - blurred_mask / 255)

    cv2.imshow(winName, result)


def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        center = (x, y)
        radius = cv2.getTrackbarPos("R", winName)
        update_image(radius, center)


im = cv2.imread('ulitsavostok.jpg')
winName = 'Main Window'
cv2.namedWindow(winName)

image_a = cv2.GaussianBlur(im, (5, 5), sigmaX=3, sigmaY=3)
image_b = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
image_b = cv2.cvtColor(image_b, cv2.COLOR_GRAY2BGR)

result = image_a.copy()

cv2.createTrackbar("R", winName, 50, 500, lambda x: None)

cv2.setMouseCallback(winName, mouse_callback)

cv2.imshow(winName, result)
cv2.waitKey(0)