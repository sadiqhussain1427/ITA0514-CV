import cv2
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
)

eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)

image = cv2.imread(file_path)

if image is None:
    print("Unable to load image")
elif eye_cascade.empty():
    print("Unable to load eye classifier")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    eyes = eye_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )

    for (x, y, w, h) in eyes:
        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (255, 0, 0),
            2
        )

    cv2.imshow("Eye Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
