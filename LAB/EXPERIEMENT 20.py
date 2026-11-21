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
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    kernel = np.ones((5, 5), np.uint8)

    dilated_image = cv2.dilate(
        gray,
        kernel,
        iterations=1
    )

    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.imshow(gray, cmap="gray")
    plt.title("Original Gray Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(dilated_image, cmap="gray")
    plt.title("Dilated Image")
    plt.axis("off")

    plt.show()
