import cv2
import numpy as np


faceDetect= cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml")
cap= cv2.VideoCapture(0)

while(True):
     ret, img= cap.read()
     gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
     faces= faceDetect.detectMultiScale(gray,1.3,5)
     for(x,y,w,h) in  faces:
          cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
     cv2.imshow("Face", img)
     if(cv2.waitKey(1)==ord('g')):
          break
cam.release()
cv2.destroyAllWindows()
