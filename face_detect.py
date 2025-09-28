import cv2
from cv2.data import haarcascades
from cv2 import CascadeClassifier

modelPath=haarcascades+"haarcascade_frontalface_default.xml"
app=CascadeClassifier(modelPath)

camera=cv2.VideoCapture(0)

while True :
    status,image=camera.read()
    faces=app.detectMultiScale(image,1.3,5)
    for face in faces:
        x,y,w,h=face
        image=cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,255),2)

    cv2.imshow("My Image",image)
    if cv2.waitKey(0)==ord("q"):
        break

