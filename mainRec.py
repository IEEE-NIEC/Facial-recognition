import cv2
import numpy as np 
import os

recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.load('training/training.yml')
detector= cv2.CascadeClassifier('/home/geekysethi/opencv-3.2.0/data/haarcascades/haarcascade_frontalface_default.xml')

cam =cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX
while(True):
	ret,img = cam.read()

	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	faces = detector.detectMultiScale(gray,1.2,5)

	for x,y,w,h in faces:

		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

		Id,conf=recognizer.predict(gray[y:y+h,x:x+w])

		if(conf<50):
			if(Id==1):

				text='Ashish'
		else:
			text="Unknown"
		print("ID",Id)
		print("Conf",conf)
		cv2.putText(img,text,(x,y+h), font,1,(255,0,0))
	cv2.imshow('image',img)
	if cv2.waitKey(10) & 0xFF==ord('q'):
		break
cam.release()
cv2.destroyAllWindows()