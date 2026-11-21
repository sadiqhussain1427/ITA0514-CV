import cv2
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

    threshold_value = 127

    ret, segmented = cv2.threshold(
        gray,
        threshold_value,
        255,
        cv2.THRESH_BINARY
    )

    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.imshow(gray, cmap="gray")
    plt.title("Original Gray Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(segmented, cmap="gray")
    plt.title("Segmented Image")
    plt.axis("off")

    plt.show()
