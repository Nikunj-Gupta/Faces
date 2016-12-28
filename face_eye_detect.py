import cv2
import numpy as np

img = cv2.imread("lena.jpg",1)
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier("../../../data/haarcascades/haarcascade_frontalface_alt.xml")

faces = face_cascade.detectMultiScale(grayimg,1.3,minNeighbors=4, minSize=(30, 30), flags = cv2.cv.CV_HAAR_SCALE_IMAGE)
for (x,y,w,h) in faces:
        cv2.rectangle(grayimg,(x,y),((x+w),(y+h)),(255,0,0),2)
	roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
img = cv2.cvtColor(grayimg,cv2.COLOR_GRAY2RGB)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
