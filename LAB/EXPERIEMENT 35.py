import cv2
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

image_path = filedialog.askopenfilename(
    filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
)

root.destroy()

image = cv2.imread(image_path)

if image is None:
    print("Unable to load image")
else:
    text = input("Enter text to display: ")

    font = cv2.FONT_HERSHEY_SIMPLEX

    cv2.putText(
        image,
        text,
        (50, 50),
        font,
        1,
        (255, 0, 0),
        2
    )

    cv2.imshow("Text Display Image", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
