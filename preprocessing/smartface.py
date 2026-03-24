import cv2
import numpy as np

image = cv2.imread("kusum.jpg")

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

if image is not None:

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Blur
    blurred = cv2.GaussianBlur(gray, (7,7), 9)

    # Contrast enhancement
    enhanced = cv2.equalizeHist(blurred)

    # Edge detection
    edges = cv2.Canny(gray, 100, 200)

    # Threshold
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contour_img = image.copy()
    cv2.drawContours(contour_img, contours, -1, (0,255,0), 2)

    # Face detection
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    face_img = image.copy()
    for (x,y,w,h) in faces:
        cv2.rectangle(face_img, (x,y), (x+w,y+h), (0,255,0), 2)

    print(f"Faces found: {len(faces)}")

    # Show results
    cv2.imshow("Original", image)
    cv2.imshow("Grayscale", gray)
    cv2.imshow("Blurred", blurred)
    cv2.imshow("Enhanced", enhanced)
    cv2.imshow("Edges", edges)
    cv2.imshow("Contours", contour_img)
    cv2.imshow("Face Detection", face_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Image not available")