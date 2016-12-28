import numpy as np
import cv2

cap = cv2.VideoCapture("video2.mp4")
face_cascade = cv2.CascadeClassifier("../../../data/haarcascades/haarcascade_frontalface_alt.xml")

while(True):
	ret, gray = cap.read()
	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	#cv2.imshow("frame",gray)
	faces = face_cascade.detectMultiScale(gray,1.3,minNeighbors=4, minSize=(30, 30), flags = cv2.cv.CV_HAAR_SCALE_IMAGE)
	for (x,y,w,h) in faces:
		cv2.rectangle(gray,(x,y),((x+w),(y+h)),(255,0,0),2)
	cv2.imshow("Image",gray)
	if cv2.waitKey(1) & 0xff==ord("q"):
		break
cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
