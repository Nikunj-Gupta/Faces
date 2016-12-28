import numpy as np
import cv2

cap = cv2.VideoCapture("video1.mp4")

while(True):
	ret, gray = cap.read()
	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	cv2.imshow("frame",gray)
	if cv2.waitKey(1) & 0xff==ord("q"):
		break
#cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
