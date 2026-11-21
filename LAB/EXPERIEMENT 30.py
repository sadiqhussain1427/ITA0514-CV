import cv2
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

smile_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_smile.xml"
)

image = cv2.imread(file_path)

if image is None:
    print("Unable to load image")
elif face_cascade.empty() or smile_cascade.empty():
    print("Unable to load Haar Cascade classifiers")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    for (x, y, w, h) in faces:
        face_region = gray[y:y+h, x:x+w]

        smiles = smile_cascade.detectMultiScale(
            face_region,
            scaleFactor=1.7,
            minNeighbors=20
        )

        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(
                image,
                (x + sx, y + sy),
                (x + sx + sw, y + sy + sh),
                (0, 255, 0),
                2
            )

    cv2.imshow("Smile Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
