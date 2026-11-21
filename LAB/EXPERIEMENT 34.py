import cv2
import numpy as np

height = int(input("Enter image height: "))
width = int(input("Enter image width: "))

image = np.ones((height, width, 3), dtype=np.uint8) * 255

center = (width // 2, height // 2)
radius = 100

cv2.circle(image, center, radius, (0, 0, 255), 3)

cv2.imshow("Circle Shape", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
