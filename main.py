import cv2
import numpy as np

# Load the input image
img = cv2.imread('parking_lot.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Define parking spot rectangles: (x, y, w, h)
spots = [
    (50, 60, 100, 180),
    (180, 60, 100, 180),
    # Add more manually based on your image
]

for i, (x, y, w, h) in enumerate(spots):
    roi = gray[y:y+h, x:x+w]
    blur = cv2.GaussianBlur(roi, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY_INV)

    white_px = cv2.countNonZero(thresh)

    # Tweak this threshold depending on image brightness and shadow
    if white_px > 2000:
        status = "Occupied"
        color = (0, 0, 255)
    else:
        status = "Empty"
        color = (0, 255, 0)

    cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
    cv2.putText(img, status, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

cv2.imshow("Parking Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
