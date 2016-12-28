import cv2.cv as cv
import time
cv.NamedWindow("camera", 1)
capture = cv.CaptureFromCAM(1)
num = 0
while True:
    img = cv.QueryFrame(capture)
    cv.ShowImage("camera", img)
    cv.SaveImage('newpic'+str(num)+'.jpg', img)
    if cv.WaitKey(1000) == 27:
        break
    num += 1
