import numpy as np
import cv2
import thread, winsound

face_cascade = cv2.CascadeClassifier('C:/opencv/build/etc/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:/opencv/build/etc/haarcascades/haarcascade_eye.xml')
#lefteye_cascade = cv2.CascadeClassifier('C:/opencv/build/etc/haarcascades/haarcascade_lefteye_2splits.xml')

def Alert():
  for i in xrange(2):
    winsound.Beep(2000, 300)

video = cv2.VideoCapture(0)# capture through web cam

trip = 0

while(1):
      ret, frame = video.read() #read capture
      count = 0
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #colour convert to gray
      faces = face_cascade.detectMultiScale(gray,scaleFactor = 1.03, minNeighbors=6)# detect faces
      for (x,y,w,h) in faces:
      	
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        eyes = eye_cascade.detectMultiScale(roi_gray,maxSize=(120,120))#detect eyes in the face
        #left=lefteye_cascade.detectMultiScale(roi_gray,scaleFactor = 1.01, minNeighbors=1, minSize=(10,10))
        #eyes=left
        if len(eyes) == 0:# if eyes are not detected
          print "Eyes closed"
        else:
          print "Eyes open"
          print eyes
          
        count += len(eyes)
        trip += 1
        if trip == 3: #if eyes are closed 3 times frequently   
          trip = 0
          if count == 0:
            print "Sleeping Detected!!!"
            cv2.putText(frame, "Alarm!!!",(105, 105),cv2.FONT_HERSHEY_COMPLEX_SMALL,.9,(0,0,255))
            thread.start_new_thread(Alert,())# give sound
          count = 0
        for (ex,ey,ew,eh) in eyes:
          cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh), (0,255,0),2)
        	#print(ex,ey,ew,eh)
      cv2.imshow('frame', frame)
      #cv2.imshow('image', roi_gray)

#closing window
      if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
