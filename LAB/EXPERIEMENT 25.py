import cv2
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

reference_path = filedialog.askopenfilename(
    title="Select Reference Watch Image",
    filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
)

test_path = filedialog.askopenfilename(
    title="Select Test Image",
    filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
)

reference_image = cv2.imread(reference_path)
test_image = cv2.imread(test_path)

if reference_image is None or test_image is None:
    print("Unable to load images")
else:
    gray1 = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)

    orb = cv2.ORB_create()

    kp1, des1 = orb.detectAndCompute(gray1, None)
    kp2, des2 = orb.detectAndCompute(gray2, None)

    if des1 is None or des2 is None:
        print("No features detected in one or both images")
    else:
        matcher = cv2.BFMatcher(
            cv2.NORM_HAMMING,
            crossCheck=True
        )

        matches = matcher.match(des1, des2)

        matches = sorted(
            matches,
            key=lambda x: x.distance
        )

        result = cv2.drawMatches(
            reference_image,
            kp1,
            test_image,
            kp2,
            matches[:20],
            None,
            flags=2
        )

        cv2.imshow("Object Recognition Result", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
