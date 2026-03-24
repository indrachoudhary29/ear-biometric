Day 1 — Image Basics

\# Load image

img = cv2.imread("image.jpg")



\# Show image

cv2.imshow("Title", img)

cv2.waitKey(0)

cv2.destroyAllWindows()



\# Save image

cv2.imwrite("saved.jpg", img)



\# Grayscale

gray = cv2.cvtColor(img, cv2.COLOR\_BGR2GRAY)



Day 2 — Preprocessing



\# Noise Removal

blur = cv2.GaussianBlur(img, (5,5), 0)



\# Contrast Enhancement

enhanced = cv2.equalizeHist(gray)



\# Sharpening

kernel = np.array(\[\[0,-1,0],

&#x20;                  \[-1,5,-1],

&#x20;                  \[0,-1,0]])

sharpened = cv2.filter2D(img, -1, kernel)

Day 3 — Edge Detection

\# Convert to black white

\_, thresh = cv2.threshold(

&#x20;           gray, 127, 255, 

&#x20;           cv2.THRESH\_BINARY)



\# Find edges

edges = cv2.Canny(img, 100, 200)

Day 3 — Contours

\# Find boundaries

contours, \_ = cv2.findContours(

&#x20;             thresh,

&#x20;             cv2.RETR\_TREE,

&#x20;             cv2.CHAIN\_APPROX\_SIMPLE)



\# Draw boundaries

cv2.drawContours(

img, contours, -1, (0,255,0), 2)



Your Project Pipeline Formula

import cv2



img = cv2.imread("ear.jpg")



\# Step 1 - Grayscale

gray = cv2.cvtColor(img, cv2.COLOR\_BGR2GRAY)



\# Step 2 - Noise Removal

blur = cv2.GaussianBlur(gray, (5,5), 0)



\# Step 3 - Contrast Enhancement

enhanced = cv2.equalizeHist(blur)



\# Step 4 - Find Ear Boundary

\_, thresh = cv2.threshold(

&#x20;           enhanced, 127, 255,

&#x20;           cv2.THRESH\_BINARY)

contours, \_ = cv2.findContours(

&#x20;             thresh,

&#x20;             cv2.RETR\_TREE,

&#x20;             cv2.CHAIN\_APPROX\_SIMPLE)

cv2.drawContours(img, contours, -1, (0,255,0), 2)



\# Step 5 - Show Result

cv2.imshow("Processed Ear", img)

cv2.waitKey(0)

cv2.destroyAllWindows()

```



\---



\## Quick Reference Card 🃏

```

imread      → Load image

imshow      → Show image

imwrite     → Save image

cvtColor    → Grayscale

GaussianBlur→ Remove noise

equalizeHist→ Enhance contrast

Canny       → Find edges

threshold   → Black and white

findContours→ Find boundary

drawContours→ Draw boundary

```



\---



\## Values To Always Remember

```

GaussianBlur  → (5,5) and 0

threshold     → 127, 255

Canny         → 100, 200

drawContours  → -1, (0,255,0), 2

RETR\_TREE     → all boundaries

RETR\_EXTERNAL → outer only

``
import cv2

# 1️⃣ Load detector
face_cascade = cv2.CascadeClassifier(
cv2.data.haarcascades +
'haarcascade_frontalface_default.xml')

# 2️⃣ Load image + grayscale
img = cv2.imread("image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3️⃣ Detect faces
faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5)

# 4️⃣ Draw box on each face
for (x, y, w, h) in faces:
    cv2.rectangle(img,
                 (x, y),
                 (x+w, y+h),
                 (0,255,0), 2)

# 5️⃣ Show result
print(f"Faces found: {len(faces)}")
cv2.imshow("Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

## What To Memorise ✅
```
CascadeClassifier → loads detector
detectMultiScale  → finds faces
scaleFactor=1.1   → always same!
minNeighbors=5    → always same!
x,y,w,h           → face location
rectangle         → draws box
```

#import cv2

# 1️⃣ Load detector
face_cascade = cv2.CascadeClassifier(
cv2.data.haarcascades +
'haarcascade_frontalface_default.xml')

# 2️⃣ Load image + grayscale
img = cv2.imread("image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3️⃣ Detect faces
faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5)

# 4️⃣ Draw box on each face
for (x, y, w, h) in faces:
    cv2.rectangle(img,
                 (x, y),
                 (x+w, y+h),
                 (0,255,0), 2)

# 5️⃣ Show result
print(f"Faces found: {len(faces)}")
cv2.imshow("Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

## What To Memorise ✅
```
CascadeClassifier → loads detector
detectMultiScale  → finds faces
scaleFactor=1.1   → always same!
minNeighbors=5    → always same!
x,y,w,h           → face location
rectangle         → draws box
```

import cv2

# 1️⃣ Load detector
face_cascade = cv2.CascadeClassifier(
cv2.data.haarcascades +
'haarcascade_frontalface_default.xml')

# 2️⃣ Load image + grayscale
img = cv2.imread("image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3️⃣ Detect faces
faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5)

# 4️⃣ Draw box on each face
for (x, y, w, h) in faces:
    cv2.rectangle(img,
                 (x, y),
                 (x+w, y+h),
                 (0,255,0), 2)

# 5️⃣ Show result
print(f"Faces found: {len(faces)}")
cv2.imshow("Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

## What To Memorise ✅
```
CascadeClassifier → loads detector
detectMultiScale  → finds faces
scaleFactor=1.1   → always same!
minNeighbors=5    → always same!
x,y,w,h           → face location
rectangle         → draws box
```
