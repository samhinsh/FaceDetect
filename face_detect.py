import cv2
import sys

# Get user supplied values
imagePath = sys.argv[1]
cascPath = sys.argv[2]

# Create the face haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # convert it to gray

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
)

print faces

print "Found {0} faces!".format(len(faces))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # recognize the eyes 
    eyeCascade = cv2.CascadeClassifier("haarcascade_eye.xml")
    eyes = eyeCascade.detectMultiScale(
    	gray,
    	scaleFactor=1.1,
    	minNeighbors=5,
    	minSize=(30, 30),
    	flags = cv2.CASCADE_SCALE_IMAGE
    )

    print eyes
    print "Found {0} eyes!".format(len(eyes))

    for (ex, ey, ew, eh) in eyes:
    	cv2.rectangle(image, (ex, ey), (ex+ew, ey+eh), (255, 0, 200), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)
