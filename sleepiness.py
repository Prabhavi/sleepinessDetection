import numpy as np
import cv2
import thread, winsound

face_cascade = cv2.CascadeClassifier('C:/opencv/build/etc/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:/opencv/build/etc/haarcascades/haarcascade_eye.xml')

def beep():
  for i in xrange(2):
    winsound.Beep(2000, 300)

video = cv2.VideoCapture(0)# capture through web cam
count = 0
iters = 0

while(1):
      ret, frame = video.read() #read capture
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #colour convert to gray
      faces = face_cascade.detectMultiScale(gray,scaleFactor = 1.1, minNeighbors=1, minSize=(10,10))# detect faces
      for (x,y,w,h) in faces:
      	
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        #cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        eyes = eye_cascade.detectMultiScale(roi_gray,scaleFactor = 1.1, minNeighbors=1, minSize=(10,10))#detect eyes in the face
        if len(eyes) == 0:# if eyes are not detected
          print "Eyes closed"
        else:
          print "Eyes open"
          print eyes
          
        count += len(eyes)
        iters += 1
        if iters == 3: #if eyes are closed 3 times frequently   
          iters = 0
          if count == 0:
            print "Sleeping Detected!!!"
            thread.start_new_thread(beep,())# give sound
          count = 0
        for (ex,ey,ew,eh) in eyes:
          cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh), (0,255,0),2)
        	#print(ex,ey,ew,eh)
      cv2.imshow('frame', frame)

#closing window
      if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
