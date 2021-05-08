import cv2,os
import numpy as np
from PIL import Image
from Tkinter import *


path = os.path.dirname(os.path.abspath(__file__))
face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(path+r'\trainer\trainer.yml')
cascadePath = path+"\Classifiers\face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX #Creates a font
while True:
    #Through Laptop Cam
    ret, frame =cam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for(x,y,w,h) in faces:
        nbr_predicted, conf = recognizer.predict(gray[y:y+h,x:x+w])
        cv2.rectangle(frame,(x-50,y-50),(x+w+50,y+h+50),(0,255,0),2)
        if(nbr_predicted==0 and conf<=63):
             tag='MM'
        else:
            tag='unknown'
        cv2.putText(frame,tag, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255),2)
        print(tag)
        print(nbr_predicted)
        print(conf)

        window = Tk()
        window.title("Door Simulation")
        window.geometry("400x500")

        if(tag=='MM'):
            color="black"
            ltext="Open!"
        else:
            color="brown"
            ltext="Close!"
        
        l = Label(window,text="DOOR",font=("Times New Roman",50))
        l.pack()
        l2 = Label(window,text=ltext,font=("Arial Italic",20))
        l2.pack()
        c = Canvas(window,bg="black")
        c.pack()
        door = c.create_rectangle(120,20,250,250,
                                  outline="white", fill=color, width=10)

        window.after(1000, lambda: window.destroy())
        window.mainloop()

    cv2.imshow('frame',frame)
    k=cv2.waitKey(20) & 0xFF
    if k==27 or k==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()









