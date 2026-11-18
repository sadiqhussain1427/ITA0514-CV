import cv2
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

image_path = filedialog.askopenfilename(
    title="Select your image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
)

image = cv2.imread(image_path)

if image is None:
    print("Image not selected or could not be loaded.")
else:
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    rotated_image = cv2.rotate(image_rgb, cv2.ROTATE_180)

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(image_rgb)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(rotated_image)
    plt.title("180 Degree Rotated Image")
    plt.axis("off")

    plt.show()

root.destroy()
