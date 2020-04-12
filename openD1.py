import cv2
import numpy as np

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
# cap = cv2.imread('shubha.jpg')
id = input('enter user id')
samplenum = 0
while (True):
    ret, img = cam.read()
    # img = cv2.imread('shubha.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        samplenum = samplenum + 1
        cv2.imwrite("dataSets/user." + str(id) + '.' + str(samplenum) + ".jpg", gray[y:y + h, x:w + x])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.waitKey(30)

    cv2.imshow('frame', img)
    cv2.waitKey(1)
    if (samplenum > 30):
        break

cam.release()
cv2.destroyAllWindows()