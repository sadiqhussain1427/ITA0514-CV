import cv2
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

cascade_path = filedialog.askopenfilename(
    title="Select cars.xml",
    filetypes=[("XML files", "*.xml")]
)

video_path = filedialog.askopenfilename(
    title="Select vehicle video",
    filetypes=[("Video files", "*.mp4 *.avi *.mov")]
)

vehicle_cascade = cv2.CascadeClassifier(cascade_path)

if vehicle_cascade.empty():
    print("Unable to load vehicle classifier")
else:
    video = cv2.VideoCapture(video_path)

    if not video.isOpened():
        print("Error opening video")
    else:
        while True:
            ret, frame = video.read()

            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            vehicles = vehicle_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=3
            )

            for (x, y, w, h) in vehicles:
                cv2.rectangle(
                    frame,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    2
                )

            cv2.imshow("Vehicle Detection", frame)

            if cv2.waitKey(30) & 0xFF == 27:
                break

        video.release()
        cv2.destroyAllWindows()
