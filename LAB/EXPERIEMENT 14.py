import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
)

image = cv2.imread(file_path)

if image is None:
    print("Unable to load image")
else:
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    height, width = image_rgb.shape[:2]

    points1 = np.float32([
        [50, 50],
        [width - 50, 50],
        [50, height - 50],
        [width - 50, height - 50]
    ])

    points2 = np.float32([
        [0, 0],
        [width, 0],
        [0, height],
        [width, height]
    ])

    matrix = cv2.getPerspectiveTransform(points1, points2)

    perspective_image = cv2.warpPerspective(
        image_rgb,
        matrix,
        (width, height)
    )

    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.imshow(image_rgb)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(perspective_image)
    plt.title("Perspective Transformed Image")
    plt.axis("off")

    plt.show()
