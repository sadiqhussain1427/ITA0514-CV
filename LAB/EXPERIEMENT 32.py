import cv2
import numpy as np

height = int(input("Enter image height: "))
width = int(input("Enter image width: "))

image = np.ones(
    (height, width, 3),
    dtype=np.uint8
) * 255

box_size = min(height, width) // 10

cv2.rectangle(
    image,
    (0, 0),
    (box_size, box_size),
    (0, 0, 0),
    -1
)

cv2.rectangle(
    image,
    (width - box_size, 0),
    (width, box_size),
    (255, 0, 0),
    -1
)

cv2.rectangle(
    image,
    (0, height - box_size),
    (box_size, height),
    (0, 255, 0),
    -1
)

cv2.rectangle(
    image,
    (width - box_size, height - box_size),
    (width, height),
    (0, 0, 255),
    -1
)

cv2.imshow("Colored Boxes Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
