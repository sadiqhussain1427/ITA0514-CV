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
elif image.shape[0] < 400 or image.shape[1] < 400:
    print("Please select an image with at least 400 x 400 pixels")
else:
    roi = image[50:200, 50:200].copy()

    image[250:400, 250:400] = roi

    cv2.imshow("Region of Interest", roi)
    cv2.imshow("Copied Image", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
