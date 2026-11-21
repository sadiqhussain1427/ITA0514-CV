import cv2
import numpy as np

height = int(input("Enter image height: "))
width = int(input("Enter image width: "))

image = np.ones((height, width, 3), dtype=np.uint8) * 255

start_point = (100, 100)
end_point = (300, 250)

cv2.rectangle(image, start_point, end_point, (255, 0, 0), 3)

cv2.imshow("Rectangle Shape", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
