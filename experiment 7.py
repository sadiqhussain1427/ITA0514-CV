import cv2

video = cv2.VideoCapture(0)

if not video.isOpened():
    print("Unable to open webcam")
    exit()

while True:
    ret, frame = video.read()

    if not ret:
        break

    cv2.imshow("Normal Speed", frame)
    if cv2.waitKey(30) & 0xFF == 27:
        break

    cv2.imshow("Slow Motion", frame)
    if cv2.waitKey(100) & 0xFF == 27:
        break

    cv2.imshow("Fast Motion", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

video.release()
cv2.destroyAllWindows()
