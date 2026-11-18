import cv2
import matplotlib.pyplot as plt
import numpy as np
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
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    sobel_x = cv2.Sobel(
        gray,
        cv2.CV_64F,
        1,
        0,
        ksize=3
    )

    sobel_y = cv2.Sobel(
        gray,
        cv2.CV_64F,
        0,
        1,
        ksize=3
    )

    sobel_x = np.uint8(np.absolute(sobel_x))
    sobel_y = np.uint8(np.absolute(sobel_y))

    sobel_combined = cv2.addWeighted(
        sobel_x,
        0.5,
        sobel_y,
        0.5,
        0
    )

    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(gray, cmap="gray")
    plt.title("Gray Image")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(sobel_x, cmap="gray")
    plt.title("Sobel X")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(sobel_combined, cmap="gray")
    plt.title("Sobel Edge Detection")
    plt.axis("off")

    plt.show()
