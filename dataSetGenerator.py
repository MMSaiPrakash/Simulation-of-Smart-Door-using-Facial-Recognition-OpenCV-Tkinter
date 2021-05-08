import cv2
import os
import urllib
import imutils

path = os.path.dirname(os.path.abspath(__file__))
detector=cv2.CascadeClassifier(path+r'\Classifiers\face.xml')
i=0
offset=50
name=raw_input('enter your id')

cam = cv2.VideoCapture(0)
while True:
    #Through IP webcam
    #IP1 = 'http://192.168.43.1:8080/shot.jpg'
    #urllib.urlretrieve(IP1, 'shot1.jpg')
    #frame = cv2.imread('shot1.jpg')
    #frame = imutils.resize(frame, width=600)

    #Through Laptop Cam
    ret, frame =cam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        i=i+1
        cv2.imwrite("dataSet/face-"+name +'.'+ str(i) + ".jpg", gray[y-offset:y+h+offset,x-offset:x+w+offset])
        cv2.rectangle(frame,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
        cv2.imshow('frame',frame[y-offset:y+h+offset,x-offset:x+w+offset])
        cv2.waitKey(100)
    if i>20:
        cam.release()
        cv2.destroyAllWindows()
        break

