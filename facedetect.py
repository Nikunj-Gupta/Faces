import cv2
import numpy as np

grayimg = cv2.imread("faces4.jpg",1)
face_cascade = cv2.CascadeClassifier("../../../data/haarcascades/haarcascade_frontalface_alt.xml")

faces = face_cascade.detectMultiScale(grayimg,1.3,minNeighbors=4, minSize=(30, 30), flags = cv2.cv.CV_HAAR_SCALE_IMAGE)
for (x,y,w,h) in faces:
	cv2.rectangle(grayimg,(x,y),((x+w),(y+h)),(255,0,0),2)
cv2.imshow("Image",grayimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
