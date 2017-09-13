import cv2
import sys
import numpy as np
# Get user supplied values
#scaleFactor=1.1,
# minNeighbors=5,
    #minSize=(30, 30)
    #flags = cv2.cv.CV_HAAR_SCALE_IMAGE

cascPath = "C:/opencv/build/etc/haarcascades/haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)
eye_cascade = cv2.CascadeClassifier('C:/opencv/build/etc/haarcascades/haarcascade_eye.xml')
# Read the image
image = cv2.imread('image3.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


faces = faceCascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]
    eyes=eye_cascade.detectMultiScale(gray, 1.01, 3)
    for (ex,ey,ew,eh) in eyes:
          cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh), (0,255,0),2)

    
cv2.imshow('img',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
