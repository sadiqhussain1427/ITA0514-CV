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

    rows, cols = image_rgb.shape[:2]

    points1 = np.float32([
        [50, 50],
        [200, 50],
        [50, 200]
    ])

    points2 = np.float32([
        [10, 100],
        [200, 50],
        [100, 250]
    ])

    matrix = cv2.getAffineTransform(points1, points2)

    affine_image = cv2.warpAffine(
        image_rgb,
        matrix,
        (cols, rows)
    )

    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.imshow(image_rgb)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(affine_image)
    plt.title("Affine Transformed Image")
    plt.axis("off")

    plt.show()
