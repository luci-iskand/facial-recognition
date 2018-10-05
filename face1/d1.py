import cv2
import numpy as np
import MySQLdb

conn= MySQLdb.connect(host='Djok', user= 'lucifer', passwd= 'lucifer')
cursor= conn.cursor()
cursor.execute('Use face')
faceDetect= cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml")
cap= cv2.VideoCapture(0)
rec =cv2.face.LBPHFaceRecognizer_create()
rec.read('recognizer/traindata.yml')
id= 0
#font= cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,1,1,0,1)
font = cv2.FONT_HERSHEY_SIMPLEX
while(True):
     ret, img= cap.read()
     gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
     faces= faceDetect.detectMultiScale(gray,1.3,5)
     for(x,y,w,h) in  faces:
          cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
          id, conf= rec.predict(gray[y:y+h, x:x+w])
          if(id==1):
               id="Sk Maurya"
          cv2.putText(img,str(id),(x,y+h) , font, 2, (255, 0, 0), 5)
          cursor.execute("insert n values ('%s')" %(id))
          conn.commit()
          #cv2.cv.PutText(cv2.cv.fromarray(img), str(id), (x, y+h), font, 255)
     cv2.imshow("Face", img)
     if(cv2.waitKey(1)==ord('g')):
          break
cam.release()
