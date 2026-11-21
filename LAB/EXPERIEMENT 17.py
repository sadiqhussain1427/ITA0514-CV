import cv2
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
    watermark = image.copy()

    cv2.putText(
        watermark,
        "COPYRIGHT",
        (50, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    watermarked_image = cv2.addWeighted(
        image,
        0.7,
        watermark,
        0.3,
        0
    )

    cv2.imshow("Original Image", image)
    cv2.imshow("Watermarked Image", watermarked_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
