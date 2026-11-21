import cv2
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

video_path = filedialog.askopenfilename(
    title="Select Input Video",
    filetypes=[("Video files", "*.mp4 *.avi *.mov")]
)

frames = []

if video_path:
    video = cv2.VideoCapture(video_path)

    while True:
        ret, frame = video.read()

        if not ret:
            break

        frames.append(frame)

    video.release()

    if len(frames) == 0:
        print("Unable to read video")
    else:
        frames.reverse()

        height, width, layers = frames[0].shape

        output_path = filedialog.asksaveasfilename(
            title="Save Reversed Video",
            defaultextension=".mp4",
            initialfile="reverse_video.mp4",
            filetypes=[("MP4 Video", "*.mp4")]
        )

        if output_path:
            output = cv2.VideoWriter(
                output_path,
                cv2.VideoWriter_fourcc(*"mp4v"),
                30,
                (width, height)
            )

            for frame in frames:
                output.write(frame)

            output.release()

            cap = cv2.VideoCapture(output_path)

            while True:
                ret, frame = cap.read()

                if not ret:
                    break

                cv2.imshow("Reverse Video", frame)

                if cv2.waitKey(30) & 0xFF == 27:
                    break

            cap.release()
            cv2.destroyAllWindows()

            print("Reversed video saved successfully")
